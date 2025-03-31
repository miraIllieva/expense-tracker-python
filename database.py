import sqlite3

def create_connection():
    conn = sqlite3.connect("expenses.db")  #database file
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("Database and table created successfully.")
