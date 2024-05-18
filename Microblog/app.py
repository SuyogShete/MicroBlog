import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin-suyog:Suyog%409552@cluster0.rdc03ve.mongodb.net/")
app.db = client.testDB

entries = []

@app.route('/', methods=["GET", "POST"])
def home():
    # print([e for e in app.db.test.find({})])
    if request.method == "POST":
        entry_content = request.form.get("content")
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        formated_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %d")
        app.db.test.insert_one({"content" : entry_content, "date" : formated_date})

    data = app.db.test.find({})

    entries = [(entry["content"], entry["date"]) for entry in data]

    return render_template("index.html", entries=entries)

