import json

from main import app
from instances.Events import Events, get_events, get_users_registered_at_event, delete_user
from flask import request, jsonify


@app.route('/create_event', methods=['POST'])
def create_event():
    record = json.loads(request.data)

    domain, name_of_event, max_number_of_participants, current_number_of_participants = (
        record['domain'], record['name_of_event'],
        record['max_number_of_participants'],
        record['current_number_of_participants'])
    event_creation_status, status_code = Events(domain, name_of_event, max_number_of_participants,
                                                current_number_of_participants).create_event()

    return jsonify(event_creation_status), status_code


@app.route('/get_events', methods=['GET'])
def get_all_events():
    get_events_status, status_code = get_events()

    return jsonify(get_events_status), status_code


@app.route('/get_users_for_event/<int:event_id>', methods=['GET'])
def get_all_users_registered_at_event(event_id: int):
    users_status, status_code = get_users_registered_at_event(event_id)

    return jsonify(users_status), status_code


@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id: int):
    deletion_status, status_code = delete_user(event_id)

    return jsonify(deletion_status), status_code
