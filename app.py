from flask import Flask, render_template
import database as db

app = Flask(__name__)
db.init_db()

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/batches")
def batches():
    rows = db.all_batches()
    return render_template("batches.html", batches=rows, stages=db.STAGES)

if __name__ == "__main__":
    app.run(debug=True)
