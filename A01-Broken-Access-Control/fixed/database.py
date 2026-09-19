import sqlite3

DATABASE = "lab.db"


def init_db():
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    users = [
        (1, "tony", "tony123", "tony@lab.local"),
        (2, "antony", "antony123", "antony@lab.local")
    ]

    conn.executemany(
        "INSERT OR IGNORE INTO users (id, username, password, email) VALUES (?, ?, ?, ?)",
        users
    )

    conn.commit()
    conn.close()


def get_user(user_id):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    user = conn.execute(
        "SELECT id, username, email FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    conn.close()

    return user