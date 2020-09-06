from typing import List
from connections import create_connection
from models import Option
import pollDatabase

"""This creates a class whose objects we can use to interact with the system in a bit of an easier way.
   Now I am able to, for example, create poll objects for example:
   newPoll = Poll('PC or Console', 'Lukasz', 3) # 3 is id made coming from database"""


class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.id = _id
        self.title = title
        self.owner = owner

    def __repr__(self):
        return f"Poll({self.name!r}, {self.owner!r}, {self.id!r}"  # Poll('title, 'owner', 1)

    def save(self):
        connection = create_connection()
        new_poll_id = pollDatabase.create_poll(connection, self.title, self.owner)
        connection.close()
        self.id = new_poll_id

    def add_option(self, option_text: str):
        Option(option_text, self.id).save()

    @property  # It allows to access poll.options instead poll.options(), adding to get familiar with this shortcut
    def options(self) -> List[Option]:
        connection = create_connection()
        options = pollDatabase.get_poll_options(connection, self.id)
        connection.close()
        return [Option(option[1], option[2], option[0]) for option in options]

    # It returns a Poll object
    @classmethod
    def get(cls, poll_id: int) -> "Poll":
        connection = create_connection()
        poll = pollDatabase.get_poll(connection, poll_id)
        connection.close()
        return cls(poll[1], poll[2], poll[0])

    # Returns a List of Polls
    @classmethod
    def all(cls) -> List["Poll"]:
        connection = create_connection()
        polls = pollDatabase.get_poll(connection)
        connection.close()
        return [cls(poll[1], poll[2], poll[0]) for poll in polls]

    # Returns latest Poll object
    @classmethod
    def latest(cls) -> "Poll":
        connection = create_connection()
        poll = pollDatabase.get_latest_poll(connection)
        connection.close()
        return cls(poll[1], poll[2], poll[0])
