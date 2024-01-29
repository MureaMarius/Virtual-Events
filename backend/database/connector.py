import mysql.connector
from backend.utilities import validations
from mysql.connector import Error
from backend.utilities import constants


class ConnectionToMySqlServer:
    def __init__(self, username: str, password: str):
        self.is_connected = 0
        self.username = username
        self.password = password
        self.connection = None

    def connect_to_mysql_server(self):
        try:
            self.connection = mysql.connector.connect(host=constants.DB_CONSTANTS.DB_HOST,
                                                      database=constants.DB_CONSTANTS.DB_DATABASE,
                                                      user=self.username,
                                                      password=self.password)
            if self.connection.is_connected():
                print(constants.DB_CONSTANTS.DB_SUCCESSFULLY_LOGIN)
                self.is_connected = 1

                self.check_if_table_exists()
        except Error as e:
            print("Invalid login.")

    def check_if_table_exists(self):
        tables = ["users", "events"]

        for table in tables:
            command = (
                f"SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{constants.DB_CONSTANTS.DB_DATABASE}' "
                f"AND TABLE_NAME = '{table}'")

            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(command)

                table_exists = cursor.fetchall()
                if len(table_exists) == 0:
                    print(f"Table {table} doesn't exists! Creating table...")
                    if table == "users":
                        command = constants.DB_CONSTANTS.DB_CREATE_USERS_TABLE
                    elif table == "events":
                        command = constants.DB_CONSTANTS.DB_CREATE_EVENTS_TABLE

                    cursor.execute(command)
                else:
                    print(f"Table {table} exists!")

    def create_user(self, username: str, password: str, email: str):
        current_users = self.get_users()
        new_id = len(current_users)

        message = validations.check_users(username, email, current_users)
        if message is not None:
            return message

        command = f"INSERT INTO Users (id, username, username_password, email) VALUES({new_id + 1}, '{username}', '{password}', '{email}')"
        if self.connection.is_connected():
            print(command)

            cursor = self.connection.cursor()
            cursor.execute(command)

            self.connection.commit()

        return "Success"

    def get_users(self):
        command = "SELECT * FROM Users"

        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute(command)

            return cursor.fetchall()
