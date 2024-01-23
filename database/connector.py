from tkinter import messagebox

import mysql.connector
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
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")
                self.is_connected = 1
        except Error as e:
            messagebox.showerror(title="Error", message="Invalid login.")

    def create_user(self, username: str, password: str, email: str):
        command = f"INSERT INTO Users (username, username_password, email) VALUES('{username}', '{password}', '{email}')"

        if self.connection.is_connected():
            print(command)

            cursor = self.connection.cursor()
            cursor.execute(command)

            self.connection.commit()
