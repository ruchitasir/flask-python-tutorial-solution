from flask import Flask, redirect, render_template, request
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["tutorial"]
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", page="home")

@app.route("/operators", methods=("GET", "POST"))
def operators():
    if request.method == "GET":
        operators = list(db.operators.find())
        return render_template("operators.html", operators=operators, page="operators")
    else:
        db.operators.insert_one({
            "name": request.form["name"],
            "description": request.form["description"],
            "symbol": request.form["symbol"],
            "example": request.form["example"],
            "uses": request.form["uses"]
        })
        return redirect("/operators")

@app.route("/loops")
def loops():
    return render_template("loops.html", page="loops")
    
app.run()
