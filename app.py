import os
import re
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-before-deploying")
DB_PATH = os.environ.get("DB_PATH", "killua_users.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                identifier TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        identifier = request.form.get("identifier", "").strip()
        password = request.form.get("password", "")
        if not identifier or not password:
            flash("Preenche os dois campos.")
            return render_template("login.html")

        # This is a KILLUA Login account, not a Facebook or other third-party login.
        with get_db() as db:
            user = db.execute(
                "SELECT * FROM users WHERE identifier = ?", (identifier,)
            ).fetchone()

            if user:
                if not check_password_hash(user["password_hash"], password):
                    flash("Dados incorretos. Tenta novamente.")
                    return render_template("login.html")
            else:
                db.execute(
                    "INSERT INTO users (identifier, password_hash) VALUES (?, ?)",
                    (identifier, generate_password_hash(password))
                )

        session["identifier"] = identifier
        return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/home")
def home():
    if "identifier" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", identifier=session["identifier"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
