DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS watch_list;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email_address TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE watch_list ( -- different sql db, not implemented yet
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  author_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  movie_yr TEXT NOT NULL,
  movie_desc TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);