import json

from main import app
from instances.User import User, update_user, register_user
from flask import request, jsonify


@app.route('/create_user', methods=['POST'])
def create_user():
    record = json.loads(request.data)
    username, password, email = record['username'], record['username_password'], record['email']
    user_creation_status = User(username, password, email).create_user()

    return jsonify(user_creation_status)


@app.route('/login', methods=['GET'])
def login():
    username, password = request.form['username'], request.form['username_password']

    if username == 'admin' and password == 'admin':
        pass

    login_status = User(username, password, "").check_user()

    return jsonify(login_status)


@app.route('/update_user', methods=['PUT'])
def update_user_info():
    interes_area, username, email = (request.form['interes_area'], request.form['username'], request.form['email'])
    update_status = update_user(interes_area, username, email)

    return jsonify(update_status)


@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    username, email = request.form['username'], request.form['email']
    delete_status = User(username, "", email).delete_user()

    return jsonify(delete_status)


@app.route('/register_user', methods=['PUT'])
def register_user_to_event():
    interes_area, username = request.form['interes_area'], request.form['username']
    registered_status = register_user(interes_area, username)

    return registered_status
