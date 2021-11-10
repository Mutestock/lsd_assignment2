-- Add up migration script here
CREATE TABLE IF NOT EXISTS people(
    id SERIAL PRIMARY KEY NOT NULL,
    is_teacher BOOLEAN NOT NULL,
    username VARCHAR(255) NOT NULL,
    pwd VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL
)


