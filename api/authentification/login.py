from flask import *

from database.connector import ConnectionToMySqlServer

my_connection = ConnectionToMySqlServer("root", "root")
my_connection.connect_to_mysql_server()


def login():
    error = None
    current_users = my_connection.get_users()

    if request.method == 'POST':
        user_exist = False
        for user in current_users:
            if user[1] == request.form['username']:
                user_exist = True
                if user[2] != request.form['username_password']:
                    print("Incorect password")
                else:
                    print("Login with SUCCESS")

        if not user_exist:
            print("User doesn't exist")

    return render_template('/login.html', error=error)
