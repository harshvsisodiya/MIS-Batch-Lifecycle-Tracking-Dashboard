"""
Seed script - populates the database with sample batch data for testing
Run this before starting the app: python scripts/seed_data.py
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import database as db

db.init_db()

BATCH_DATA = [
    {
        "name": "TAG-2026-DEL-0101: Delhi Skill Assessment Drive",
        "owner": "Rahul Verma",
        "deadline": 7,
        "history": [
            ("2026-08-22 09:35:14", "Initiated"),
            ("2026-08-22 17:15:20", "In Progress"),
            ("2026-08-24 11:42:08", "Under Review"),
            ("2026-08-25 15:20:45", "Completed"),
            ("2026-08-26 11:35:14", "Closed"),
        ],
    },
    {
        "name": "FK-CAT-QC-901: North Zone Seller Catalog QC",
        "owner": "Neha Gupta",
        "deadline": 5,
        "history": [
            ("2026-08-22 10:12:45", "Initiated"),
            ("2026-08-23 11:30:10", "In Progress"),
            ("2026-08-24 16:45:22", "Under Review"),
            ("2026-08-26 12:15:05", "Completed"),
            ("2026-08-27 08:12:45", "Closed"),
        ],
    },
    {
        "name": "KYC-VERIF-B102: Aadhaar e-KYC Verification Hub",
        "owner": "Amit Patel",
        "deadline": 3,
        "history": [
            ("2026-08-23 09:45:30", "Initiated"),
            ("2026-08-24 10:15:12", "In Progress"),
            ("2026-08-25 14:30:44", "Under Review"),
            ("2026-08-26 16:20:18", "Completed"),
            ("2026-08-27 05:45:30", "Closed"),
        ],
    },
    {
        "name": "INV-RECON-MUM: Q1 Logistics Invoice Reconciliation",
        "owner": "Priya Nair",
        "deadline": 10,
        "history": [
            ("2026-08-23 11:20:10", "Initiated"),
            ("2026-08-25 11:20:10", "In Progress"),
            ("2026-08-27 23:20:10", "Under Review"),
            ("2026-08-29 15:20:10", "Completed"),
            ("2026-08-30 23:20:10", "Closed"),
        ],
    },
    {
        "name": "TAG-EXAM-RJ-204: Rajasthan Tech Assessor Evaluators",
        "owner": "Rahul Verma",
        "deadline": 7,
        "history": [
            ("2026-08-24 09:15:00", "Initiated"),
            ("2026-08-25 09:15:00", "In Progress"),
            ("2026-08-26 21:15:00", "Under Review"),
            ("2026-08-28 21:15:00", "Completed"),
            ("2026-08-30 09:15:00", "Closed"),
        ],
    },
    {
        "name": "SELLER-ONB-BLR: South Seller Portal Onboarding",
        "owner": "Vikram Singh",
        "deadline": 5,
        "history": [
            ("2026-08-24 10:45:15", "Initiated"),
            ("2026-08-25 22:45:15", "In Progress"),
            ("2026-08-27 22:45:15", "Under Review"),
            ("2026-08-29 22:45:15", "Completed"),
            ("2026-08-30 22:45:15", "Closed"),
        ],
    },
    {
        "name": "AUDIT-SOP-PUN: Pune Hub Facility Compliance Audit",
        "owner": "Divya Iyer",
        "deadline": 8,
        "history": [
            ("2026-08-25 09:30:20", "Initiated"),
            ("2026-08-26 09:30:20", "In Progress"),
            ("2026-08-28 01:30:20", "Under Review"),
            ("2026-08-30 01:30:20", "Completed"),
            ("2026-08-30 21:30:20", "Closed"),
        ],
    },
    {
        "name": "GGL-MKT-VLD: Local Merchant Data Validation - Jaipur",
        "owner": "Pooja Sharma",
        "deadline": 6,
        "history": [
            ("2026-08-25 11:00:00", "Initiated"),
            ("2026-08-26 05:00:00", "In Progress"),
            ("2026-08-27 11:00:00", "Under Review"),
            ("2026-08-28 23:00:00", "Completed"),
            ("2026-08-29 23:00:00", "Closed"),
        ],
    },
    {
        "name": "FIN-SETTLE-HYD: Courier COD Settlement Cycle 03",
        "owner": "Suresh Kumar",
        "deadline": 4,
        "history": [
            ("2026-08-26 09:15:30", "Initiated"),
            ("2026-08-27 01:15:30", "In Progress"),
            ("2026-08-27 21:15:30", "Under Review"),
            ("2026-08-28 21:15:30", "Completed"),
            ("2026-08-29 15:15:30", "Closed"),
        ],
    },
    {
        "name": "DOC-OCR-KOL: Eastern Region Document Digitization",
        "owner": "Meera Mukherjee",
        "deadline": 5,
        "history": [
            ("2026-08-26 10:00:00", "Initiated"),
            ("2026-08-27 16:00:00", "In Progress"),
            ("2026-08-29 16:00:00", "Under Review"),
            ("2026-08-31 20:00:00", "Completed"),
            ("2026-09-01 22:00:00", "Closed"),
        ],
    },
    {
        "name": "TAG-2026-UP-0312: Lucknow Assessor Panel Certification",
        "owner": "Rahul Verma",
        "deadline": 7,
        "history": [
            ("2026-08-31 10:15:00", "Initiated"),
            ("2026-09-01 10:15:00", "In Progress"),
            ("2026-09-02 22:15:00", "Under Review"),
            ("2026-09-04 14:15:00", "Completed"),
        ],
    },
    {
        "name": "VEND-BGV-CHE: Tamil Nadu Vendor Background Checks",
        "owner": "Divya Iyer",
        "deadline": 6,
        "history": [
            ("2026-09-01 09:40:00", "Initiated"),
            ("2026-09-02 05:40:00", "In Progress"),
            ("2026-09-03 11:40:00", "Under Review"),
            ("2026-09-04 23:40:00", "Completed"),
        ],
    },
    {
        "name": "BPO-QA-NOIDA: Customer Support Quality Scorecards",
        "owner": "Ankit Joshi",
        "deadline": 4,
        "history": [
            ("2026-08-30 11:30:00", "Initiated"),
            ("2026-08-31 05:30:00", "In Progress"),
            ("2026-09-01 05:30:00", "Under Review"),
            ("2026-09-02 09:30:00", "Completed"),
        ],
    },
    {
        "name": "TAG-CERT-MP-105: MP Vocational Assessor Audit",
        "owner": "Amit Patel",
        "deadline": 7,
        "history": [
            ("2026-09-02 09:30:00", "Initiated"),
            ("2026-09-03 13:30:00", "In Progress"),
            ("2026-09-05 13:30:00", "Under Review"),
        ],
    },
    {
        "name": "TAX-GST-RECON-GJ: Gujarat Region GST Return Cross-Audit",
        "owner": "Pooja Sharma",
        "deadline": 5,
        "history": [
            ("2026-09-03 10:00:00", "Initiated"),
            ("2026-09-04 10:00:00", "In Progress"),
            ("2026-09-05 22:00:00", "Under Review"),
        ],
    },
    {
        "name": "LOGIS-SLA-BLR: Bengaluru Warehousing TAT Audit",
        "owner": "Vikram Singh",
        "deadline": 4,
        "history": [
            ("2026-08-28 09:15:00", "Initiated"),
            ("2026-08-30 09:15:00", "In Progress"),
            ("2026-09-01 21:15:00", "Under Review"),
        ],
    },
    {
        "name": "MED-CLAIM-CHG: Chandigarh Insurance Claim Verification",
        "owner": "Suresh Kumar",
        "deadline": 5,
        "history": [
            ("2026-09-04 11:20:00", "Initiated"),
            ("2026-09-05 05:20:00", "In Progress"),
            ("2026-09-06 05:20:00", "Under Review"),
        ],
    },
    {
        "name": "TAG-2026-HAR-0401: Haryana Sector Skill Assessment",
        "owner": "Neha Gupta",
        "deadline": 7,
        "history": [
            ("2026-09-05 09:30:00", "Initiated"),
            ("2026-09-06 15:30:00", "In Progress"),
        ],
    },
    {
        "name": "ECOM-RETURN-DEL: North Hub Return Order Validation",
        "owner": "Ankit Joshi",
        "deadline": 4,
        "history": [
            ("2026-09-06 10:00:00", "Initiated"),
            ("2026-09-07 06:00:00", "In Progress"),
        ],
    },
    {
        "name": "ASSET-INV-MUM: Mumbai Data Center Hardware Audit",
        "owner": "Priya Nair",
        "deadline": 5,
        "history": [
            ("2026-08-30 11:00:00", "Initiated"),
            ("2026-08-31 23:00:00", "In Progress"),
        ],
    },
    {
        "name": "TRANS-DATA-KOL: Eastern Logistics Fleet Telemetry Batch",
        "owner": "Meera Mukherjee",
        "deadline": 6,
        "history": [
            ("2026-09-06 14:15:00", "Initiated"),
            ("2026-09-07 08:15:00", "In Progress"),
        ],
    },
    {
        "name": "TAG-2026-RAJ-0502: Jaipur District IT Assessor Onboarding",
        "owner": "Rahul Verma",
        "deadline": 7,
        "history": [
            ("2026-09-07 09:30:00", "Initiated"),
        ],
    },
    {
        "name": "PAYROLL-OPS-AUG: Pan-India Contractor Payout Batch",
        "owner": "Pooja Sharma",
        "deadline": 5,
        "history": [
            ("2026-09-08 10:15:00", "Initiated"),
        ],
    },
    {
        "name": "API-SYNC-GATEWAY: Payment Gateway Settlement Batch #88",
        "owner": "Amit Patel",
        "deadline": 3,
        "history": [
            ("2026-09-08 14:45:00", "Initiated"),
        ],
    },
    {
        "name": "SOP-COMP-ANNUAL: Amity Partner Training Audit 2026",
        "owner": "Divya Iyer",
        "deadline": 10,
        "history": [
            ("2026-09-09 09:15:00", "Initiated"),
        ],
    },
]


def seed():
    conn = db.get_conn()
    conn.execute("DELETE FROM status_log")
    conn.execute("DELETE FROM batches")
    conn.commit()
    conn.close()

    for item in BATCH_DATA:
        created_time = item["history"][0][0]
        final_status = item["history"][-1][1]

        conn = db.get_conn()
        cur = conn.execute(
            "INSERT INTO batches (name, owner, sop_deadline_days, created_at, current_status) VALUES (?, ?, ?, ?, ?)",
            (item["name"], item["owner"], item["deadline"], created_time, final_status)
        )
        bid = cur.lastrowid

        prev = None
        for ts, status in item["history"]:
            conn.execute(
                "INSERT INTO status_log (batch_id, old_status, new_status, changed_at) VALUES (?, ?, ?, ?)",
                (bid, prev, status, ts)
            )
            prev = status

        conn.commit()
        conn.close()

    stats = db.compute_stats()
    print(f"Done! Seeded {len(BATCH_DATA)} batches.")
    print(f"Distribution: {dict(stats['distribution'])}")
    print(f"Avg cycle time: {stats['avg_cycle_hours']} hrs")
    print(f"SOP compliance: {stats['compliance_pct']}%")


if __name__ == "__main__":
    seed()
