import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(entry_content, entry_date):
    with connection:#this is important because without it, it will not be commited so i wont be able to see it anywhere
        connection.execute(
            f"INSERT INTO entries VALUES(?, ?);", (entry_content, entry_date)
        )

def get_entries():
    cursor = connection.cursor() # Shorter version: cursor = connection.execute("SELECT * FROM entries;")
    cursor.execute("SELECT * FROM entries;")
    return cursor
