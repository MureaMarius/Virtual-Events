class Db_constants:
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    DB_HOST = "localhost"
    DB_DATABASE = "virtual_events"
    DB_SUCCESSFULLY_LOGIN = "You successfully logged in to the DATABASE"

    DB_USERS_TABLE = "users"
    DB_EVENTS_TABLE = "events"

    DB_CREATE_USERS_TABLE = ("CREATE TABLE users(id int PRIMARY KEY, username varchar(255), username_password varchar(255), email varchar(255), "
                             "interes_area varchar(255), number_of_events int)")
    DB_CREATE_EVENTS_TABLE = "CREATE TABLE events(id int PRIMARY KEY, name varchar(255), participants int)"


class Users_constants:
    INVALID_USER_MESSAGE = "Username already used -- try another one"
    INVALID_EMAIL_MESSAGE = "Email already used -- try another one"
    INVALID_PASSWORD_CREATION_MESSAGE = "Password must contain the following:" + \
                                        "* A lowercase letter" + \
                                        "* A capital (uppercase) letter" + \
                                        "* A number" + \
                                        "* Minimum 10 characters" + \
                                        "* A special character"
    INVALID_USERNAME_LOGIN_MESSAGE = "Username doesn't exists"
    INVALID_PASSWORD_LOGIN_MESSAGE = "Incorrect password"

    USER_CREATION_STATUS = "User created with SUCCESS"
    USER_UPDATE_STATUS = "User updated with SUCCESS"
    LOGIN_SUCCESSFULLY = "Login with SUCCESS"

