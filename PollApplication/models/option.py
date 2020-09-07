from typing import List
from connection_pool import pool
import pollDatabase


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id

    def __str__(self) -> str:
        return f"{self.id}: {self.text}"

    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r}"

    def save(self):
        connection = pool.getconn()
        new_option_id = pollDatabase.add_option(connection, self.text, self.poll_id)
        pool.putconn(connection)
        self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> "Option":
        connection = pool.getconn()
        poll = pollDatabase.get_option(connection, option_id)
        pool.putconn(connection)
        return cls(poll[1], poll[2], poll[0])

    def vote(self, username: str):
        connection = pool.getconn()
        pollDatabase.add_poll_vote(connection, username, self.id)
        pool.putconn(connection)

    @property
    def votes(self) -> List[pollDatabase.vote]:
        connection = pool.getconn()
        votes = pollDatabase.get_votes_for_option(connection, self.id)
        pool.putconn(connection)
        return votes