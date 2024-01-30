import json

from main import app
from instances.user import get_users, User
from flask import request, jsonify, render_template


@app.route('/create_user', methods=['POST'])
def create_user():
    record = json.loads(request.data)
    username, password, email = record['username'], record['username_password'], record['email']

    user_is_created = User(username, password, email).create_user()

    if user_is_created is not True:
        print(user_is_created)

    return jsonify(record)


@app.route('/login', methods=['GET'])
def login():
    error = None
    current_users = get_users()

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

    return render_template('/templates/login.html', error=error)
