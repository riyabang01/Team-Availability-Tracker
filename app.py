import sqlite3
import webbrowser
from threading import Timer
from flask import Flask, render_template, jsonify

app = Flask(__name__)
DB_NAME = "team.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            is_available BOOLEAN NOT NULL DEFAULT 1
        )
    """)

    count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if count == 0:
        sample_users = [
            ("Riya Bang", "Full Stack Developer", True),
            ("Sunita Maheshwari", "MERN Developer", True),
            ("Rahul Sharma", "Frontend Developer", True),
            ("Priya Patel", "Backend Developer", True),
            ("Amit Verma", "UI/UX Designer", False),
            ("Sneha Kulkarni", "QA Engineer", True),
        ]
        conn.executemany(
            "INSERT INTO users (name, role, is_available) VALUES (?, ?, ?)",
            sample_users,
        )
    conn.commit()
    conn.close()


@app.route("/")
def dashboard():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("index.html", users=users)


@app.route("/api/users/<int:user_id>/toggle", methods=["POST"])
def toggle_availability(user_id):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

    if user is None:
        conn.close()
        return jsonify({"error": "User not found"}), 404

    new_status = not bool(user["is_available"])

    conn.execute(
        "UPDATE users SET is_available = ? WHERE id = ?",
        (int(new_status), user_id),
    )
    conn.commit()
    conn.close()

    return jsonify({"id": user_id, "is_available": new_status})


if __name__ == "__main__":
    init_db()
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True, use_reloader=False)
