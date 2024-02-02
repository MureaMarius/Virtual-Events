from utilities import constants
from application import my_connection


def get_events():
    command = "SELECT * FROM events"

    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)

        try:
            with my_connection.connection.cursor() as cursor:
                cursor.execute(command)

                return cursor.fetchall(), constants.Status_codes.STATUS_OK
        except Exception as e:
            print("Error occurred: ", e)

    return constants.Events_constants.NO_EVENTS_IN_DB, constants.Status_codes.STATUS_OK


def get_events_by_domain(domain: str):
    command = f"SELECT event_id FROM events WHERE domain = '{domain}'"

    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)

        try:
            with my_connection.connection.cursor() as cursor:
                cursor.execute(command)

                return cursor.fetchall(), constants.Status_codes.STATUS_OK
        except Exception as e:
            print("Error occurred: ", e)

    return constants.Events_constants.NO_EVENTS_IN_DB_WITH_SPECIFIC_DOMAIN, constants.Status_codes.STATUS_OK


def get_users_registered_at_event(event_id: int):
    command = (f"SELECT users.username, users.email, events.domain, events.name_of_event "
               f"FROM users INNER JOIN events ON users.event_id = events.event_id WHERE events.event_id = {event_id}")

    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)
        try:
            with my_connection.connection.cursor() as cursor:
                cursor.execute(command)

                users = cursor.fetchall()
                if len(users) > 0:
                    return users, constants.Status_codes.STATUS_OK
        except Exception as e:
            print("Error occurred: ", e)

    return constants.Events_constants.NO_USERS_REGISTERED, constants.Status_codes.STATUS_OK


def check_if_event_is_full(event_id: int):
    command = (f"SELECT max_number_of_participants, current_number_of_participants FROM events "
               f"WHERE event_id = {event_id}")

    if my_connection.is_connected:
        try:
            with my_connection.connection.cursor() as cursor:
                cursor.execute(command)
                event_details = cursor.fetchall()

                max_number_of_participants, current_number_of_participants = event_details[0], event_details[1]
                if current_number_of_participants == max_number_of_participants:
                    return True
        except Exception as e:
            print("Error occurred: ", e)

    return False


def increase_number_of_participants(event_id: int):
    global command
    command = f"SELECT current_number_of_participants FROM events WHERE event_id = {event_id}"

    if my_connection.is_connected:
        try:
            with my_connection.connection.cursor() as cursor:
                cursor.execute(command)
                current_number_of_participants = cursor.fetchall()[0][0]

                command = (f"UPDATE events SET current_number_of_participants = {current_number_of_participants + 1} "
                           f"WHERE event_id = {event_id}")

                cursor.execute(command)
                my_connection.connection.commit()

        except Exception as e:
            print("Error occurred: ", e)

    return True


def delete_user(event_id: int):
    global command
    command = f"SELECT id FROM users WHERE event_id = {event_id}"

    if my_connection.is_connected:
        try:
            with my_connection.connection.cursor() as cursor:
                cursor.execute(command)
                users_id = cursor.fetchall()[0]

                for user_id in users_id:
                    command = f"UPDATE users SET event_id = null WHERE id = {user_id}"

                    cursor.execute(command)
                    my_connection.connection.commit()

                command = f"DELETE FROM events WHERE event_id = {event_id}"
                cursor.execute(command)
                my_connection.connection.commit()
        except Exception as e:
            print("Error occurred: ", e)

    return constants.Events_constants.EVENT_DELETED, constants.Status_codes.STATUS_OK


class Events:
    def __init__(self, domain: str, name_of_event: str, max_number_of_participants: int,
                 current_number_of_participants):
        self.domain = domain
        self.name_of_event = name_of_event
        self.max_number_of_participants = max_number_of_participants
        self.current_number_of_participants = current_number_of_participants

    def create_event(self):
        command = (f"INSERT INTO events (domain, name_of_event, max_number_of_participants, "
                   f"current_number_of_participants) VALUES('{self.domain}', '{self.name_of_event}', "
                   f"{self.max_number_of_participants}, {self.current_number_of_participants})")

        if my_connection.is_connected:
            print("DB will be updated with the following command: ", command)

            try:
                with my_connection.connection.cursor() as cursor:
                    cursor.execute(command)
                    my_connection.connection.commit()
            except Exception as e:
                print("Error occurred: ", e)

        return constants.Events_constants.EVENT_CREATION_STATUS, constants.Status_codes.STATUS_OK
