Peaches_Studio
Week 5 Solo Project using: HTML, CSS, Python, Flask, PostgreSQL and the psycopg library. Practising TDD, RESTful routes and CRUD database interactions.

My Brief - Gym
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP
The app should allow the user to create and edit Members.
The app should allow the user to create and edit Lessons.
The app should allow the user to book members on specific lessons.
The app should show a list of all upcoming lessons.
The app should show all members that are booked in for a particular lesson.

My Extensions
Classes have a maximum capacity, and users can only be added while there is space remaining.
Ensure a member can only be booked for each lesson once.
The user can give members Deluxe or Standard membership. Standard members can only be signed up for a maximum of 3 classes a week, Deluxe have no limit.
Show all lessons a member is booked in for.
Show capacity and remaining space for a selected lesson.
Delete members, lessons and bookings.

To Access, first clone the repository and run the below commands.

Terminal 1: 
- flask run (open a window with http://127.0.0.1:5000/ if this has not happened automatically)

Terminal 2:
- psql -d peaches_studio -f db/peaches_studio.sql
- python3 console.py

Enjoy! Let me know if you have any questions or feedback.
