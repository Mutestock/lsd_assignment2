-- Add down migration script here
CREATE TABLE IF NOT EXISTS people_m2m_check_ins(
    people_id INTEGER NOT NULL,
    check_in_id INTEGER NOT NULL
)

