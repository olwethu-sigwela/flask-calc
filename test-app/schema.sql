DROP TABLE IF EXISTS calcs;

CREATE TABLE calcs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL,
    operation TEXT NOT NULL,
    answer FLOAT NOT NULL
);