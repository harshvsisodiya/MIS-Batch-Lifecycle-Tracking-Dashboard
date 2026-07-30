import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "mis_dashboard.db")

STAGES = ["Initiated", "In Progress", "Under Review", "Completed", "Closed"]

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.executescript('''
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
    ''')
    conn.commit()
    conn.close()
