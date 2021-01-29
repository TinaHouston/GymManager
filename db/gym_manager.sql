DROP TABLE bookings;
DROP TABLE members;
DROP TABLE sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INT
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    capacity BOOL,
    time VARCHAR(225),
    date VARCHAR(225)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) on DELETE CASCADE
);