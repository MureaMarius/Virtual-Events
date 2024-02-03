import os

import mysql.connector
from mysql.connector import Error
from utilities import constants


class ConnectionToMySqlServer:
    def __init__(self, username: str, password: str):
        self.is_connected = 0
        self.username = username
        self.password = password
        self.connection = None

    def connect_to_mysql_server(self):
        try:
            self.connection = mysql.connector.connect(host=os.environ.get("DB_HOST"),
                                                      database=os.environ.get("DB_DATABASE"),
                                                      user=self.username,
                                                      password=self.password)
            if self.connection.is_connected():
                print(constants.Db_constants.DB_SUCCESSFULLY_LOGIN)
                self.is_connected = 1

                self.check_if_table_exists()
        except Error as e:
            print("Invalid login.")

    def check_if_table_exists(self):
        tables = ["events", "users"]

        for table in tables:
            db = os.environ.get("DB_DATABASE")
            command = (
                f"SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{db}' "
                f"AND TABLE_NAME = '{table}'")

            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(command)

                table_exists = cursor.fetchall()
                if len(table_exists) == 0:
                    print(f"Table {table} doesn't exists! Creating table...")
                    if table == "users":
                        command = constants.Db_constants.DB_CREATE_USERS_TABLE
                    elif table == "events":
                        command = constants.Db_constants.DB_CREATE_EVENTS_TABLE

                    print(f"Table {table} is created with the following command: ", command)
                    cursor.execute(command)
                else:
                    print(f"Table {table} exists!")