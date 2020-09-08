from typing import List
from connection_pool import get_connection
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
        with get_connection() as connection:
            new_option_id = pollDatabase.add_option(connection, self.text, self.poll_id)
            self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> "Option":
        with get_connection() as connection:
            poll = pollDatabase.get_option(connection, option_id)
            return cls(poll[1], poll[2], poll[0])

    def vote(self, username: str):
        with get_connection() as connection:
            pollDatabase.add_poll_vote(connection, username, self.id)

    @property
    def votes(self) -> List[pollDatabase.vote]:
        with get_connection() as connection:
            votes = pollDatabase.get_votes_for_option(connection, self.id)
            return votes