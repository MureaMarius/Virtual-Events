from utilities import constants, validations
from application import my_connection


def get_users():
    command = "SELECT * FROM Users"

    if my_connection.is_connected:
        cursor = my_connection.connection.cursor()
        cursor.execute(command)

        return cursor.fetchall()


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

        command = (f"INSERT INTO Users (id, username, username_password, email) VALUES({new_id + 1}, "
                   f"'{self.username}', '{self.password}', '{self.email}')")
        if my_connection.is_connected:
            print(command)

            cursor = my_connection.connection.cursor()
            cursor.execute(command)

            my_connection.connection.commit()

        return True