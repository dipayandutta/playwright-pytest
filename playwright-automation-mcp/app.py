import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)

DB_PATH = "users.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        existing = conn.execute(
            "SELECT id FROM users WHERE username = ?", ("admin",)
        ).fetchone()
        if not existing:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("admin", generate_password_hash("admin")),
            )
        conn.commit()


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        with get_db() as conn:
            user = conn.execute(
                "SELECT * FROM users WHERE username = ?", (username,)
            ).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session["user"] = username
            flash("Login Successfull", "success")
            return redirect(url_for("login"))
        flash("Invalid credentials", "danger")
    return render_template("index.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
