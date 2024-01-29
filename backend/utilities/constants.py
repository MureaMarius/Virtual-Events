class DB_CONSTANTS:
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    DB_HOST = "localhost"
    DB_DATABASE = "virtual_events"
    DB_SUCCESSFULLY_LOGIN = "You successfully logged in to the DATABASE"

    DB_USERS_TABLE = "users"
    DB_EVENTS_TABLE = "events"

    DB_CREATE_USERS_TABLE = "CREATE TABLE users(id int PRIMARY KEY, username varchar(255), username_password varchar(255), email varchar(255))"
    DB_CREATE_EVENTS_TABLE = "CREATE TABLE events(id int PRIMARY KEY, name varchar(255), participants int)"




