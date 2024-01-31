import json

from main import app
from instances.Events import Events
from flask import request, jsonify


@app.route('/create_event', methods=['POST'])
def create_event():
    record = json.loads(request.data)

    domain, name_of_event, max_number_of_participants, current_number_of_participants = (
        record['domain'], record['name_of_event'],
        record['max_number_of_participants'],
        record['current_number_of_participants'])
    event_creation_status = Events(domain, name_of_event, max_number_of_participants,
                                   current_number_of_participants).create_event()

    return jsonify(event_creation_status)


@app.route('/get_users_for_event', methods=['GET'])
def get_all_users_registered_at_event():
    pass
