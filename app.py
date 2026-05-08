from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

# 🔑 GEMINI API KEY
API_KEY = "YOUR_GEMINI_API_KEY"


# =========================
# 🗄️ DATABASE INIT
# =========================
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            college TEXT,
            domain TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()


# =========================
# 🏠 HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# 🤖 AI CHAT (GEMINI)
# =========================
@app.route("/chat", methods=["POST"])
def chat():

    user_msg = request.json.get("message")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{
            "parts": [{
                "text": user_msg
            }]
        }]
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        reply = data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print(e)
        reply = "AI error ❌"

    return jsonify({"reply": reply})


# =========================
# 📝 APPLY INTERNSHIP SAVE
# =========================
@app.route("/apply", methods=["POST"])
def apply():

    data = request.json

    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO students (name, email, college, domain)
        VALUES (?, ?, ?, ?)
    """, (
        data["name"],
        data["email"],
        data["college"],
        data["domain"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Application Saved Successfully ✅"})


if __name__ == "__main__":
    app.run(debug=True)
@app.route("/certificate", methods=["POST"])
def certificate():

    data = request.json
    name = data["name"]
    domain = data["domain"]

    file_name = f"{name}_certificate.pdf"

    c = canvas.Canvas(file_name)
    c.setFont("Helvetica-Bold", 20)

    c.drawString(200, 750, "TRAINING TRAINS")
    c.setFont("Helvetica", 14)
    c.drawString(200, 700, "Internship Completion Certificate")

    c.drawString(200, 650, f"Name: {name}")
    c.drawString(200, 620, f"Domain: {domain}")

    c.drawString(200, 580, "Congratulations for completing internship!")

    c.save()

    return jsonify({"message": "Certificate Generated ✅", "file": file_name})