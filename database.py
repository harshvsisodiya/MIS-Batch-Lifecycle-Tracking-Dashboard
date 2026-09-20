import os
import sqlite3
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "mis_dashboard.db")

STAGES = ["Initiated", "In Progress", "Under Review", "Completed", "Closed"]


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS batches (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            name              TEXT NOT NULL,
            owner             TEXT NOT NULL,
            sop_deadline_days INTEGER NOT NULL DEFAULT 7,
            created_at        TEXT NOT NULL,
            current_status    TEXT NOT NULL DEFAULT 'Initiated'
        );

        CREATE TABLE IF NOT EXISTS status_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_id    INTEGER NOT NULL REFERENCES batches(id),
            old_status  TEXT,
            new_status  TEXT NOT NULL,
            changed_at  TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_status_log_batch ON status_log(batch_id);
    """)
    conn.commit()
    conn.close()


def next_stage(current):
    idx = STAGES.index(current)
    if idx + 1 < len(STAGES):
        return STAGES[idx + 1]
    return None


def create_batch(name, owner, sop_deadline_days):
    conn = get_conn()
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    cur = conn.execute(
        "INSERT INTO batches (name, owner, sop_deadline_days, created_at, current_status) VALUES (?, ?, ?, ?, ?)",
        (name, owner, sop_deadline_days, now, STAGES[0])
    )
    batch_id = cur.lastrowid
    conn.execute(
        "INSERT INTO status_log (batch_id, old_status, new_status, changed_at) VALUES (?, NULL, ?, ?)",
        (batch_id, STAGES[0], now)
    )
    conn.commit()
    conn.close()
    return batch_id


def advance_batch(batch_id):
    conn = get_conn()
    row = conn.execute("SELECT * FROM batches WHERE id = ?", (batch_id,)).fetchone()
    if not row:
        conn.close()
        return False

    nxt = next_stage(row["current_status"])
    if not nxt:
        conn.close()
        return False

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        "INSERT INTO status_log (batch_id, old_status, new_status, changed_at) VALUES (?, ?, ?, ?)",
        (batch_id, row["current_status"], nxt, now)
    )
    conn.execute("UPDATE batches SET current_status = ? WHERE id = ?", (nxt, batch_id))
    conn.commit()
    conn.close()
    return True


def all_batches():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM batches ORDER BY id DESC").fetchall()
    conn.close()
    return rows


def get_batch(batch_id):
    conn = get_conn()
    row = conn.execute("SELECT * FROM batches WHERE id = ?", (batch_id,)).fetchone()
    conn.close()
    return row


def get_status_log(batch_id):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM status_log WHERE batch_id = ? ORDER BY changed_at ASC",
        (batch_id,)
    ).fetchall()
    conn.close()
    return rows


def batch_health(batch_id):
    """green = on time, amber = in progress, red = overdue"""
    conn = get_conn()
    b = conn.execute("SELECT * FROM batches WHERE id = ?", (batch_id,)).fetchone()
    if not b:
        conn.close()
        return None

    created = datetime.strptime(b["created_at"], "%Y-%m-%d %H:%M:%S")
    deadline = created + timedelta(days=b["sop_deadline_days"])

    if b["current_status"] == "Closed":
        row = conn.execute(
            "SELECT changed_at FROM status_log WHERE batch_id = ? AND new_status = 'Closed' ORDER BY changed_at DESC LIMIT 1",
            (batch_id,)
        ).fetchone()
        conn.close()
        if not row:
            return "green"
        closed_at = datetime.strptime(row["changed_at"], "%Y-%m-%d %H:%M:%S")
        return "green" if closed_at <= deadline else "red"
    else:
        conn.close()
        now = datetime.utcnow()
        return "red" if now > deadline else "amber"


def compute_stats():
    conn = get_conn()
    batches = conn.execute("SELECT * FROM batches").fetchall()

    distribution = {s: 0 for s in STAGES}
    for b in batches:
        distribution[b["current_status"]] += 1

    closed = [b for b in batches if b["current_status"] == "Closed"]
    cycle_times = []
    on_time = 0

    for b in closed:
        row = conn.execute(
            "SELECT changed_at FROM status_log WHERE batch_id = ? AND new_status = 'Closed' ORDER BY changed_at DESC LIMIT 1",
            (b["id"],)
        ).fetchone()
        if not row:
            continue

        t_created = datetime.strptime(b["created_at"], "%Y-%m-%d %H:%M:%S")
        t_closed = datetime.strptime(row["changed_at"], "%Y-%m-%d %H:%M:%S")
        hours = (t_closed - t_created).total_seconds() / 3600
        cycle_times.append(hours)

        deadline = t_created + timedelta(days=b["sop_deadline_days"])
        if t_closed <= deadline:
            on_time += 1

    avg_hours = sum(cycle_times) / len(cycle_times) if cycle_times else 0
    compliance = (on_time / len(closed) * 100) if closed else 0

    conn.close()
    return {
        "total_batches": len(batches),
        "distribution": distribution,
        "avg_cycle_hours": round(avg_hours, 1),
        "closed_count": len(closed),
        "on_time_count": on_time,
        "compliance_pct": round(compliance, 1),
    }
