import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        course TEXT,
        marks TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert(name, roll, course, marks):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students VALUES (NULL, ?, ?, ?, ?)",
        (name, roll, course, marks)
    )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
