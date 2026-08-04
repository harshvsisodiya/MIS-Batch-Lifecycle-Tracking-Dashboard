from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)
db.init_db()

@app.route("/")
def dashboard():
    return "Dashboard"

@app.route("/batches")
def batches():
    rows = db.all_batches()
    return render_template("batches.html", batches=rows, stages=db.STAGES)

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

if __name__ == "__main__":
    app.run(debug=True)
