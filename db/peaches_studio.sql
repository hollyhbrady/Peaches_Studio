DROP TABLE bookings;
DROP TABLE members;
DROP TABLE lessons;

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    capacity INT,
    category VARCHAR(225),
    day VARCHAR(225),
    time INT,
    duration INT
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    membership VARCHAR(225)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
);
