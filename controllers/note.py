from flask import Blueprint, request, jsonify
from services.csv_service import add_note, get_note, update_note, delete_note

note_router = Blueprint('note_router', __name__)

@note_router.route('/note', methods=['POST'])
def create_note():
    note_data = request.get_json()
    result = add_note(note_data)
    return jsonify(result)

@note_router.route('/note/<note_id>', methods=['GET'])
def read_note(note_id):
    result = get_note(note_id)
    return jsonify(result)

@note_router.route('/note/<note_id>', methods=['PUT'])
def update_note_route(note_id):
    note_data = request.get_json()
    result = update_note(note_id, note_data)
    return jsonify(result)

@note_router.route('/note/<note_id>', methods=['DELETE'])
def delete_note_route(note_id):
    result = delete_note(note_id)
    return jsonify(result)