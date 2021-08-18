-- create
CREATE TABLE IF NOT EXISTS users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(64)  NOT NULL,
    password VARCHAR(128) NOT NULL
);

-- create
CREATE TABLE IF NOT EXISTS models
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name  VARCHAR(64) NOT NULL,
    description TEXT
);

-- create
CREATE TABLE IF NOT EXISTS docs
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    title   VARCHAR(64) NOT NULL,
    content TEXT        NOT NULL
);

-- create
CREATE TABLE IF NOT EXISTS attachments
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    src         VARCHAR(1024) NOT NULL,
    description VARCHAR(128)
);

-- create
CREATE TABLE IF NOT EXISTS user_model
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id INTEGER,
    model_id   INTEGER,
    FOREIGN KEY (creator_id) REFERENCES users (id),
    FOREIGN KEY (model_id) REFERENCES models (id)
);

-- create
CREATE TABLE IF NOT EXISTS model_docs
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id   INTEGER,
    model_id INTEGER,
    FOREIGN KEY (doc_id) REFERENCES docs (id),
    FOREIGN KEY (model_id) REFERENCES models (id)
);

-- create
CREATE TABLE IF NOT EXISTS user_docs
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id INTEGER,
    doc_id     INTEGER,
    FOREIGN KEY (creator_id) REFERENCES users (id),
    FOREIGN KEY (doc_id) REFERENCES docs (id)
);

-- create
CREATE TABLE IF NOT EXISTS model_attachment
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id      INTEGER,
    attachment_id INTEGER,
    FOREIGN KEY (model_id) REFERENCES models (id),
    FOREIGN KEY (attachment_id) REFERENCES attachments (id)
);

