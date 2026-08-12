from flask import Flask, render_template, request, redirect, url_for, jsonify
import database as db

app = Flask(__name__)
db.init_db()

@app.route("/")
def dashboard():
    stats = db.compute_stats()
    return render_template("dashboard.html", stats=stats, stages=db.STAGES)

@app.route("/api/stats")
def api_stats():
    return jsonify(db.compute_stats())

@app.route("/batches")
def batches():
    rows = db.all_batches()
    enriched = []
    for b in rows:
        enriched.append({
            "batch": b,
            "stage_index": db.STAGES.index(b["current_status"]),
            "health": db.batch_health(b["id"]),
        })
    return render_template("batches.html", batches=enriched, stages=db.STAGES)

@app.route("/batches/new", methods=["GET", "POST"])
def new_batch():
    if request.method == "POST":
        name = request.form["name"].strip()
        owner = request.form["owner"].strip()
        deadline = int(request.form.get("sop_deadline_days", 7))
        if name and owner:
            db.create_batch(name, owner, deadline)
        return redirect(url_for("batches"))
    return render_template("add_batch.html")

@app.route("/batches/<int:batch_id>/advance", methods=["POST"])
def advance(batch_id):
    db.advance_batch(batch_id)
    return redirect(url_for("batches"))

@app.route("/batches/<int:batch_id>")
def batch_detail(batch_id):
    b = db.get_batch(batch_id)
    log = db.get_status_log(batch_id)
    stage_index = db.STAGES.index(b["current_status"]) if b else 0
    health = db.batch_health(batch_id)
    return render_template("batch_detail.html", batch=b, log=log, stages=db.STAGES, stage_index=stage_index, health=health)

if __name__ == "__main__":
    app.run(debug=True)
