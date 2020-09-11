import sqlite3

connection = sqlite3.connect('data.db')

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS diary (
    id INTEGER PRIMARY KEY,
    entry_date TEXT,
    entry TEXT);"""

ADD_ENTRY = "INSERT INTO diary (entry, entry_date) VALUES (?,?);"

VIEW_ENTRIES = "SELECT * FROM diary;"

DELETE_ENTRY = "DELETE FROM diary WHERE id = ?;"


def create_table():
    with connection:
        connection.execute(CREATE_TABLE)



def add_entry(entry, entry_date):
    with connection:
        connection.execute(ADD_ENTRY, (entry, entry_date))



def view_entries():
    with connection:
        cursor = connection.execute(VIEW_ENTRIES)
        return cursor


def delete_entry(entry_number):
    with connection:
        connection.execute(DELETE_ENTRY, (entry_number,))

def close_conn():
    connection.close()

