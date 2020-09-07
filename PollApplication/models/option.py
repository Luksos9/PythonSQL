from typing import List
from connections import create_connection
import pollDatabase


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r}"

    def save(self):
        connection = create_connection()
        new_option_id = pollDatabase.add_option(connection, self.text, self.poll_id)
        connection.close()
        self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> "Option":
        connection = create_connection()
        poll = pollDatabase.get_option(connection, option_id)
        connection.close()
        return cls(poll[1], poll[2], poll[0])

    def vote(self, username: str):
        connection = create_connection()
        pollDatabase.add_poll_vote(connection, username, self.id)
        connection.close()

    @property
    def votes(self) -> List[pollDatabase.vote]:
        connection = create_connection()
        votes = pollDatabase.get_votes_for_option(connection, self.id)
        connection.close()
        return votes