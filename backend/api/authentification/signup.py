import json

from backend.database.connector import ConnectionToMySqlServer
from backend.utilities import validations, constants
from flask import request, jsonify

my_connection = ConnectionToMySqlServer(constants.DB_CONSTANTS.DB_USERNAME, constants.DB_CONSTANTS.DB_PASSWORD)
my_connection.connect_to_mysql_server()


def create_user():
    record = json.loads(request.data)

    username = record['username']
    password = record['username_password']
    email = record['email']

    if validations.password_validation(password):
        was_created = my_connection.create_user(username, password, email)

        if was_created == "Success":
            print("User was created with success")
        else:
            print(was_created)
    else:
        print("Password must contain the following:"
              "* A lowercase letter"
              "* A capital (uppercase) letter"
              "* A number"
              "* Minimum 10 characters"
              "* A special character")

    return jsonify(record)
