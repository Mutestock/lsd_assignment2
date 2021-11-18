-- Add up migration script here
CREATE TABLE IF NOT EXISTS people_m2m_groups(
    people_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL
)
