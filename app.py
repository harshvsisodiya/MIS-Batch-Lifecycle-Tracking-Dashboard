from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return "MIS Dashboard"

if __name__ == "__main__":
    app.run(debug=True)
