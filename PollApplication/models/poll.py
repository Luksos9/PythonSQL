from typing import List
from connection_pool import get_connection
from models.option import Option
import pollDatabase

"""This creates a class whose objects we can use to interact with the system in a bit of an easier way.
   Now I am able to, for example, create poll objects for example:
   newPoll = Poll('PC or Console', 'Lukasz', 3) # 3 is id made coming from database"""


class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.id = _id
        self.title = title
        self.owner = owner

    def __str__(self):  # string representation for poll object, so i can print it
        return f"{self.id}: {self.title} (created by {self.owner})"

    def __repr__(self):
        return f"Poll({self.name!r}, {self.owner!r}, {self.id!r}"  # Poll('title, 'owner', 1)

    def save(self):
        with get_connection() as connection:
            new_poll_id = pollDatabase.create_poll(connection, self.title, self.owner)
            self.id = new_poll_id

    def add_option(self, option_text: str):
        Option(option_text, self.id).save()

    @property  # It allows to access poll.options instead poll.options(), adding to get familiar with this shortcut
    def options(self) -> List[Option]:
        with get_connection() as connection:
            options = pollDatabase.get_poll_options(connection, self.id)
            return [Option(option[1], option[2], option[0]) for option in options]

    # It returns a Poll object
    @classmethod
    def get(cls, poll_id: int) -> "Poll":
        with get_connection() as connection:
            poll = pollDatabase.get_poll(connection, poll_id)
            return cls(poll[1], poll[2], poll[0])

    # Returns a List of Polls
    @classmethod
    def all(cls) -> List["Poll"]:
        with get_connection() as connection:
            polls = pollDatabase.get_poll(connection)
            return [cls(poll[1], poll[2], poll[0]) for poll in polls]

    # Returns latest Poll object
    @classmethod
    def latest(cls) -> "Poll":
        with get_connection() as connection:
            poll = pollDatabase.get_latest_poll(connection)
            return cls(poll[1], poll[2], poll[0])
