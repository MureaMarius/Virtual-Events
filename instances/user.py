from utilities import constants, validations
from application import my_connection


def get_users():
    command = "SELECT * FROM users"

    if my_connection.is_connected:
        print("DB will be interogated with the following command: ", command)

        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        return cursor.fetchall()


def get_user_id(username: str, email: str):
    command = f"SELECT id FROM users WHERE username = '{username}' and email = '{email}'"
    if my_connection.is_connected:
        print("DB will be interogated with the following command: ", command)

        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        return cursor.fetchall()


def update_user(interes_area: str, number_of_events: int, username: str, email: str):
    command = (f"UPDATE users SET interes_area = '{interes_area}', number_of_events = {number_of_events} WHERE "
               f"username = '{username}' and email = '{email}'")

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
            return username_email_verification

        if password_verification is not True:
            return constants.Users_constants.INVALID_PASSWORD_CREATION_MESSAGE

        command = (f"INSERT INTO users (id, username, username_password, email) VALUES({new_id + 1}, "
                   f"'{self.username}', '{self.password}', '{self.email}')")
        if my_connection.is_connected:
            print("DB will be updated with the following command: ", command)

            cursor = my_connection.connection.cursor()
            cursor.execute(command)

            my_connection.connection.commit()

        return constants.Users_constants.USER_CREATION_STATUS

    def check_user(self):
        current_users = get_users()

        for user in current_users:
            if user[1] == self.username:
                if user[2] != self.password:
                    return constants.Users_constants.INVALID_PASSWORD_LOGIN_MESSAGE
                else:
                    return constants.Users_constants.LOGIN_SUCCESSFULLY

        return constants.Users_constants.INVALID_USERNAME_LOGIN_MESSAGE
