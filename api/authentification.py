import json

from main import app
from instances.user import User, update_user
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
    login_status = User(username, password, "").check_user()

    return jsonify(login_status)


@app.route('/update_user', methods=['PUT'])
def update_user_info():
    interes_area, number_of_events, username, email = (request.form['interes_area'], request.form['number_of_events'],
                                                       request.form['username'], request.form['email'])

    update_status = update_user(interes_area, int(number_of_events), username, email)

    return jsonify(update_status)