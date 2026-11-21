import os
import json

from pathlib import Path
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "FlaskDB")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "submissions")

client = None
collection = None

if MONGO_URI:
    client = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000
    )
    collection = client[DB_NAME][COLLECTION_NAME]


@app.route("/")
def home():
    return render_template("index.html")


# Task 1: JSON API
@app.route("/api")
def api():
    try:
        with open(BASE_DIR / "data.json", "r") as file:
            data = json.load(file)

        return jsonify(data)

    except Exception:
        app.logger.exception("Unable to load JSON data")
        return jsonify({"error": "Unable to load data"}), 500


# Task 2: MongoDB form submission
@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not all([name, email, message]):
        return render_template(
            "index.html",
            error="All fields are required."
        )

    try:
        if collection is None:
            raise RuntimeError("MongoDB configuration missing")

        collection.insert_one({
            "name": name,
            "email": email,
            "message": message
        })

        return redirect(url_for("success"))

    except Exception:
        app.logger.exception("MongoDB insertion failed")

        return render_template(
            "index.html",
            error="Unable to submit data. Please try again."
        )


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
