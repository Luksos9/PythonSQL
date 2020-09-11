# PythonSQL
Projects using Python and databases (SQLite, PostgreSQL). PollApplication is most advanced of them.

# Short descriptions of programs

## Diary App

> This program gives user 4 options: 
1) To add a new log entry
2) To view your entries
3) To delete entry
4) To Exit 

> All data is stored in created "data.db". JournalWithPythonSQL is very similiar, but this one im going to improve soon.

## JournalWithPythonSQL

> This program gives user 3 options: 
1) To add new entry, so he can store what he had learned and when
2) To view the entries that he made
3) To exit

> It stores all data in data.db file so after closing the program, data is not lost.

## MovieWatchList

> Program keeps track of movies the user is intrested in, and their release dates which he can input by himself.

> Stores which movie the user has already watched

> Adds new users to keep track of their watched movies separately

1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add new user.
7) Search for a movie.
8) Exit.

## MovieWatchListPostgreSQL

> This program is a child of its previous MovieWatchList. The difference between them is mostly that this one uses PostgreSQL as database.

> Main goal with this duplication was practicing switching between SQLite (sqlite3 module) and PostgreSQL (pycopg2) and solidyfying PostgreSQL knowledge.

## PollApplication

> Features of this application:

1) **Create polls** - User enters poll title (for example Django vs Flask or PC vs Console), then name of the owner/creator of the poll, and options to vote (for example: Django, Flask, something else, wait it isn't spanish class?). When user leaves option empty by pressing enter it ends adding options (user is informed about that)

2) **List open polls** - Shows user all polls that were created and stored in database. It shows id, name of poll and creator of the poll.

3) **Vote on a poll** - Prompts user to enter poll which he would he like to vote on (user enters id; he gets it from option 2), then it displays all options to vote in that poll, after choosing option user can enter his name.

4) **Show poll votes** - First asks user to enter which poll, after choosing poll by user it displays all options with % of total votes they got, then ask user if he wants to see who voted for what, if yes shows all users and time when they voted (converting by UTC so it supports different locations)

5) **Select a random winner from a poll option** - It asks user to enter the poll id, then which of the options is winning option, after that it selects a random winner among voters for that option.

6) **Exit** - After inputting 6 program closes.

## Contact
Created by [@Luksos9](https://github.com/Luksos9)
**E-mail**: *lukaszszumilas9@wp.pl*, [@linkedIn](https://www.linkedin.com/in/łukasz-szumilas-5b48821aa/) - feel free to contact me!

# Visit directory with each program for more info about them
