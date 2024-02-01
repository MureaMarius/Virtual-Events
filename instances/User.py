import random

from utilities import constants, validations
from application import my_connection
from instances.Events import get_events_by_domain


def get_users():
    command = "SELECT * FROM users"

    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)

        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        return cursor.fetchall()


def get_user_id(username: str, email: str):
    command = f"SELECT id FROM users WHERE username = '{username}' and email = '{email}'"
    if my_connection.is_connected:
        print("DB will be interrogated with the following command: ", command)

        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        return cursor.fetchall()


def update_user(interes_area: str, username: str, email: str):
    command = f"UPDATE users SET interes_area = '{interes_area}' WHERE username = '{username}' and email = '{email}'"

    if my_connection.is_connected:
        print("DB will be updated with the following command: ", command)
        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        my_connection.connection.commit()

    return constants.Users_constants.USER_UPDATE_STATUS


def register_user(interes_area: str, username: str):
    events_id = get_events_by_domain(interes_area)
    if len(events_id) == 0:
        return constants.Users_constants.USER_CANT_BE_REGISTERED
    else:
        selected_id = events_id[random.randint(0, len(events_id) - 1)][0]

        command = f"UPDATE users SET event_id = '{selected_id}' WHERE username = '{username}'"
        if my_connection.is_connected:
            print("DB will be updated with the following command: ", command)
            cursor = my_connection.connection.cursor()
            cursor.execute(command)

            my_connection.connection.commit()

        return constants.Users_constants.USER_UPDATE_STATUS


def register_user_to_specific_event(event_id: int, username: str):
    command = f"UPDATE users SET event_id = '{event_id}' WHERE username = '{username}'"
    if my_connection.is_connected:
        print("DB will be updated with the following command: ", command)
        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        my_connection.connection.commit()

    return constants.Users_constants.USER_UPDATE_STATUS


class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

    def create_user(self):
        current_users = get_users()
        new_id = len(current_users)

        username_email_verification = validations.check_users(self.username, self.email, current_users)
        password_verification = validations.password_validation(self.password)

        if username_email_verification is not True:
            return username_email_verification, constants.Status_codes.BAD_REQUEST

        if password_verification is not True:
            return constants.Users_constants.INVALID_PASSWORD_CREATION_MESSAGE, constants.Status_codes.BAD_REQUEST

        command = (f"INSERT INTO users (id, username, username_password, email) VALUES({new_id + 1}, "
                   f"'{self.username}', '{self.password}', '{self.email}')")
        if my_connection.is_connected:
            print("DB will be updated with the following command: ", command)

            try:
                with my_connection.connection.cursor() as cursor:
                    cursor.execute(command)

                my_connection.connection.commit()
            except Exception as e:
                print("Error occurred: ", e)

        return constants.Users_constants.USER_CREATION_STATUS, constants.Status_codes.CREATED

    def check_user(self):
        current_users = get_users()

        for user in current_users:
            if user[1] == self.username:
                if user[2] != self.password:
                    return constants.Users_constants.INVALID_PASSWORD_LOGIN_MESSAGE, constants.Status_codes.UNAUTHORIZED
                else:
                    return constants.Users_constants.LOGIN_SUCCESSFULLY, constants.Status_codes.STATUS_OK

        return constants.Users_constants.INVALID_USERNAME_LOGIN_MESSAGE, constants.Status_codes.UNAUTHORIZED

    def delete_user(self):
        user_id = get_user_id(self.username, self.email)[0][0]
        command = f"DELETE FROM users WHERE id = {user_id}"

        if my_connection.is_connected:
            print("DB will be updated with the following command: ", command)
            cursor = my_connection.connection.cursor()
            cursor.execute(command)

            my_connection.connection.commit()

        return constants.Users_constants.USER_DELETE_STATUS
