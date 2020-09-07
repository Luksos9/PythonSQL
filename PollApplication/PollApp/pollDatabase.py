from typing import List, Tuple
from psycopg2.extras import execute_values

# Type hints for this app
Poll = Tuple[int, str, str]
Option = Tuple[int, str, int]
vote = Tuple[str, int]
PollResults = Tuple[int, str, int, float]

CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls
(id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"""
CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES polls (id));"""
CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes
(username TEXT, option_id INTEGER, FOREIGN KEY(option_id) REFERENCES options(id));"""

SELECT_POLL = "SELECT * FROM polls WHERE id = %s;"
SELECT_ALL_POLLS = "SELECT * FROM polls;"
SELECT_POLL_OPTIONS = "SELECT * FROM options WHERE poll_id = %s;"
SELECT_LATEST_POLL = """SELECT * FROM polls
JOIN options ON polls.id = options.poll_id
WHERE polls.id = (
    SELECT id FROM polls ORDER BY id DESC LIMIT 1
);"""
SELECT_POLL_VOTE_DETAILS = """SELECT
    options.id,
    options.option_text,
    COUNT(votes.option_id) AS vote_count,
    COUNT(votes.option_id) / SUM(COUNT(votes.option_id)) OVER() * 100.0 AS vote_percentage
FROM options
LEFT JOIN votes ON options.id = votes.option_id
WHERE options.poll_id = %s
GROUP BY options.id;"""
SELECT_RANDOM_VOTE = "SELECT * FROM votes WHERE option_id = %s ORDER BY RANDOM() LIMIT 1;"

INSERT_POLL_RETURN_ID = "INSERT INTO polls (title, owner_username) VALUES (%s, %s) RETURNING id;"
INSERT_OPTION = "INSERT INTO options (option_text, poll_id) VALUES %s;"
INSERT_VOTE = "INSERT INTO votes (username, option_id) VALUES (%s, %s);"


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)


# -- polls --

def create_poll(connection, title: str, owner: str, options: List[str]):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_POLL_RETURN_ID, (title, owner))

            poll_id = cursor.fetchone()[0]
            option_values = [(option_text, poll_id) for option_text in options]

            execute_values(cursor, INSERT_OPTION, option_values)


def get_poll(connection, poll_id: int) -> Poll:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL, (poll_id,))
            return cursor.fetchone()


def get_polls(connection) -> List[Poll]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()


def get_latest_poll(connection) -> List[PollWithOption]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_LATEST_POLL)
            return cursor.fetchall()


def get_poll_options(connection, poll_id: int) -> List[Option]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_OPTIONS, (poll_id,))
            return cursor.fetchall()


# -- options --

def get_option(connection, option_id: int) -> Option:
    pass


def add_option(connection, option_text, poll_id: int):
    pass

# -- votes --

def get_votes_for_option(connection, option_id: int) -> List[vote]:
    pass

def get_poll_and_vote_results(connection, poll_id: int) -> List[PollResults]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_VOTE_DETAILS, (poll_id,))
            return cursor.fetchall()


def get_random_poll_vote(connection, option_id: int) -> vote:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_RANDOM_VOTE, (option_id,))
            return cursor.fetchone()


def add_poll_vote(connection, username: str, option_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id))
