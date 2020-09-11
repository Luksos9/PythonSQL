## PollApplication

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Screenshots](#screenshots)
* [What I Learned](#what-i-learned)
* [Technologies](#technologies)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General Info

Purpose of this project increasing my Python, Databases, Object oriented programming (OOP), Mathplotlib, Datatime and some more knowledge by using all of that in this project.
It has many useful functions that let you create, display, vote on Polls and more like displaying votes % on charts, selecting random winner, checking who voted and when regardless of location which will be converted to local time. In Program i used OOP and made Poll and Option classes, what gave much maintability for the Application. I added connection polling for better efficiency. Also used matplotlip to display (or save as file) data of votes from database and stored it in chartHandling directory.

## Setup

This program uses PostgreSQL, so in file: _.env.example_ in environmental variable DATA_URL= ,there should be putted a URL link to Postgre database. I didn't share mine to make it safe from changes, as if i didn't everyone could then go into it and delete all it's content.

## Features

1) **Create polls** - User enters poll title (for example Django vs Flask or PC vs Console), then name of the owner/creator of the poll, and options to vote (for example: Django, Flask, something else, wait it isn't spanish class?). When user leaves option empty by pressing enter it ends adding options (user is informed about that)

2) **List open polls** - Shows user all polls that were created and stored in database. It shows id, name of poll and creator of the poll.

3) **Vote on a poll** - Prompts user to enter poll which he would he like to vote on (user enters id; he gets it from option 2), then it displays all options to vote in that poll, after choosing option user can enter his name.

4) **Show poll votes** - First asks user to enter which poll, after choosing poll by user it displays all options with % of total votes they got, then ask user if he wants to see who voted for what, if yes shows all users and time when they voted (converting by UTC so it supports different locations)

5) **Select a random winner from a poll option** - It asks user to enter the poll id, then which of the options is winning option, after that it selects a random winner among voters for that option.

6) **Exit** - After inputting 6 program closes.

## Screenshots



## What i Learned?

1) I Learned Nested Queries (to select latest poll for example)

2) I learned about SQL functions (Mathmematical functions, Aggregate functions etc.)

3) How to write different queries to select, insert, create what i need.

4) How to read Postgre Documentation and importance of it.

5) How to add type hinting to this application and why (avoiding some bugs with hints given)

6) Object oriented programming and how to represent  content of my application with classes and why its useful and pros and cons of it (maintability, efficiency impact)

7) How connection pooling works and its efficiency impact. (i was using psycopg2.pool module)

8) How to use contex menager to reduce duplication and improve code.

9) Using datetime library, converting dates from different UTC's.

10) How to change something in database and propagate that change throughout entire application.
(by figuring out new data for user to interact with, then adding necessary flow like:
changing database interaction function, queries, model that's using that, changing user facing code).

11) Using matplotlib library to display charts (bar, pie ,line) also neatly formatting them and saving into file. 

## Technologies

* Python  - version 3.8.5
* git     - version 2.27.0.windows.1
* PyCharm - 2020.1.4
* psycopg2-binary
* python-dotenv
* matplotlib
* Windows 10
* ElephantSQL

## Status
Project is: _not finished_.
I want to add: to allow users to vote throught the internet

## Inspiration
Project inspired by Jose Salvatierra.Founder of Teclado and Software Engineer.
Based on his Udemy course: The Complete Python/PostgreSQL Course 2.0.

I found this course really valuable and helpful in developing my Python and databases skills.
Sincere thanks to the autor.

## Contact
Created by [@Luksos9](https://github.com/Luksos9)

**E-mail**: *lukaszszumilas9@wp.pl*, [@linkedIn](https://www.linkedin.com/in/łukasz-szumilas-5b48821aa/) - feel free to contact me!
