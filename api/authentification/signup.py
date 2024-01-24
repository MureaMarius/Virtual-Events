import json
from flask import Flask, request, jsonify

from database.connector import ConnectionToMySqlServer
from main import app

my_connection = ConnectionToMySqlServer("root", "root")
my_connection.connect_to_mysql_server()


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    record = json.loads(request.data)

    username = record['username']
    password = record['username_password']
    email = record['email']
    my_connection.create_user(username, password, email)

    return jsonify(record)