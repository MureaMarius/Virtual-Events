import json
from flask import Flask, request, jsonify, render_template

from database.connector import ConnectionToMySqlServer

app = Flask(__name__)

my_connection = ConnectionToMySqlServer("root", "root")
my_connection.connect_to_mysql_server()


@app.route('/', methods=['POST'])
def create_user():
    record = json.loads(request.data)

    username = record['username']
    password = record['username_password']
    email = record['email']
    my_connection.create_user(username, password, email)

    return jsonify(record)
