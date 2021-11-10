-- Add up migration script here
CREATE TABLE IF NOT EXISTS check_ins(
    id SERIAL PRIMARY KEY NOT NULL,
    check_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    check_end TIMESTAMP NOT NULL, 
    note VARCHAR(255)
);
