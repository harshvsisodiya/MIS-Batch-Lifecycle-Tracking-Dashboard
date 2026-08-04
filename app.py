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
    return render_template("add_batch.html")

if __name__ == "__main__":
    app.run(debug=True)
