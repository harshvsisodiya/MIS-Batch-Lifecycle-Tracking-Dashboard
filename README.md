# MIS Batch Lifecycle Tracking Dashboard

Amity BCA Major Project (ETMJ100)

## About

A Flask web app that tracks batches through 5 stages:
**Initiated → In Progress → Under Review → Completed → Closed**

It calculates status distribution, average cycle time, and SOP compliance rate
from the transition history. Based on how operations teams track work in real life.

## How to run

```bash
pip install -r requirements.txt
python scripts/seed_data.py   # seeds 25 sample batches
python app.py                 # starts at http://127.0.0.1:5000
```

## Project structure

```
mis-dashboard/
├── app.py               # flask routes
├── database.py          # db schema + queries + metrics
├── requirements.txt
├── mis_dashboard.db     # sqlite db (auto-created)
├── scripts/
│   └── seed_data.py     # sample data seeder
├── static/css/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── batches.html
│   ├── batch_detail.html
│   └── add_batch.html
└── docs/                # university docs, guidelines etc
```

## Database schema

```
batches: id, name, owner, sop_deadline_days, created_at, current_status
status_log: id, batch_id (FK), old_status, new_status, changed_at
```

The `status_log` table records every stage transition so we can calculate
how long each batch took and whether it met the SOP deadline.

## Metrics (from database.py compute_stats)

1. **Status distribution** — how many batches are in each stage right now
2. **Average cycle time** — mean hours from creation to closure
3. **SOP compliance** — % of closed batches that finished within their deadline

```
T_avg = (1/N) * Σ (t_closed - t_created)
Compliance = (on_time_count / total_closed) × 100%
```

## Tips for the report

- Run the seeder and take screenshots of the dashboard — use those as figures
- Note down the actual numbers (cycle time, compliance %) from your run
- If you want more realistic data, create batches through the UI over a few days
