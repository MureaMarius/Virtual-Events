import mysql.connector
from utilities import validations
from mysql.connector import Error


class ConnectionToMySqlServer:
    def __init__(self, username: str, password: str):
        self.is_connected = 0
        self.username = username
        self.password = password
        self.connection = None

    def connect_to_mysql_server(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='virtual_events',
                                                      user=self.username,
                                                      password=self.password)
            if self.connection.is_connected():
                print("You successfully logged in.")
                self.is_connected = 1
        except Error as e:
            print("Invalid login.")

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