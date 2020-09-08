import os
from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

DATABASE_PROMPT = "Enter the DATABASE_URI value or leave empty to load from .env file: "

database_uri = input(DATABASE_PROMPT)
if not database_uri:
    load_dotenv()
    database_uri = os.environ["DATABASE_URI"]

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=database_uri)


@contextmanager
def get_connection():
    connection = pool.getconn()

    try:
        yield connection
    finally:
        pool.putconn(connection)


"""Notice that created SimpleConnectionPool class is good for simple threaded applications in Python.

If making multi-threaded applications, psycopg2 has a threaded connection pool class that you can use instead."""
