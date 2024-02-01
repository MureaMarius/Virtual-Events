from utilities import constants
from application import my_connection


def get_events():
    command = "SELECT * FROM events"

    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)

        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        return cursor.fetchall()


def get_events_by_domain(domain: str):
    command = f"SELECT event_id FROM events WHERE domain = '{domain}'"

    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)

        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        return cursor.fetchall()


def get_users_registered_at_event(event_id: int):
    command = (f"SELECT users.username, users.email, events.domain, events.name_of_event "
               f"FROM users INNER JOIN events ON users.event_id = events.event_id WHERE events.event_id = {event_id}")

    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)
        try:
            with my_connection.connection.cursor() as cursor:
                cursor.execute(command)

            return cursor.fetchall()
        except Exception as e:
            print("Error occurred: ", e)

    return constants.Events_constants.NO_USERS_REGISTERED, constants.Status_codes.STATUS_OK


class Events:
    def __init__(self, domain: str, name_of_event: str, max_number_of_participants: int,
                 current_number_of_participants):
        self.domain = domain
        self.name_of_event = name_of_event
        self.max_number_of_participants = max_number_of_participants
        self.current_number_of_participants = current_number_of_participants

    def create_event(self):
        current_events = get_events()
        new_id = len(current_events)

        command = (f"INSERT INTO events (event_id, domain, name_of_event, max_number_of_participants, "
                   f"current_number_of_participants) VALUES({new_id + 1},"
                   f"'{self.domain}', '{self.name_of_event}', {self.max_number_of_participants}, {self.current_number_of_participants})")

        if my_connection.is_connected:
            print("DB will be updated with the following command: ", command)

            cursor = my_connection.connection.cursor()
            cursor.execute(command)

            my_connection.connection.commit()

        return constants.Events_constants.EVENT_CREATION_STATUS
