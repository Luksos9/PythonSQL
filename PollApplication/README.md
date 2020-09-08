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