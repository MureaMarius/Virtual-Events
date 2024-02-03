class Db_constants:
    DB_SUCCESSFULLY_LOGIN = "You successfully logged in to the DATABASE"

    DB_USERS_TABLE = "users"
    DB_EVENTS_TABLE = "events"

    DB_CREATE_USERS_TABLE = (
        "CREATE TABLE users(id int NOT NULL AUTO_INCREMENT, username varchar(255), username_password varchar(255), email varchar(255),"
        "interes_area varchar(255), event_id int, PRIMARY KEY (id), FOREIGN KEY (event_id) REFERENCES events(event_id))")
    DB_CREATE_EVENTS_TABLE = (
        "CREATE TABLE events(event_id int NOT NULL AUTO_INCREMENT, domain varchar(255), name_of_event varchar(255), "
        "max_number_of_participants int, current_number_of_participants int, PRIMARY KEY (event_id))")


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
    USER_DELETE_STATUS = "User deleted with SUCCESS"
    LOGIN_SUCCESSFULLY = "Login with SUCCESS"

    NO_USERS_IN_DB = "There are no users in the DB"
    USER_CANT_BE_REGISTERED = "Current user can't be registered to some events from his domain area"


class Events_constants:
    EVENT_CREATION_STATUS = "Event created with SUCCESS"
    EVENT_IS_FULL = "Selected event is full"
    NO_USERS_REGISTERED = "There are no users registered at this event"
    NUMBER_OF_PARTICIPANTS_EXCEDEED = "Number of participants exceeded"
    EVENT_DELETED = "Even deleted with SUCCESS"
    NO_EVENTS_IN_DB = "There are no events in the DB"
    NO_EVENTS_IN_DB_WITH_SPECIFIC_DOMAIN = "There are no events in the DB with this specific domain"


class Status_codes:
    STATUS_OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


