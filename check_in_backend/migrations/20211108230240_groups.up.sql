-- Add up migration script here
CREATE TABLE IF NOT EXISTS groups(
    id SERIAL NOT NULL,
    name VARCHAR(255) NOT NULL
)
