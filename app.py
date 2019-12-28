#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request

app = Flask(__name__)

rooms = [
    {
        'id': 1,
        'title': u'Playadito',
        'description': u'Room number 1', 
        'available': True
    },
    {
        'id': 2,
        'title': u'Cruz Malta',
        'description': u'Room number 2', 
        'available': True
    }
]

@app.route('/api/v1.0/rooms', methods=['GET'])
def get_rooms():
    return jsonify({'rooms': rooms})

@app.route('/api/v1.0/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    room = [room for room in rooms if room['id'] == room_id]
    if len(room) == 0:
        abort(404)
    return jsonify({'room': room[0]})

@app.route('/api/v1.0/rooms', methods=['POST'])
def create_room():
    if not request.json or not 'title' in request.json:
        abort(400)
    room = {
        'id': rooms[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'available': True
    }
    rooms.append(room)
    return jsonify({'room': room}), 201

@app.route('/api/v1.0/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    room = [room for room in rooms if room['id'] == room_id]
    if len(room) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'available' in request.json and type(request.json['available']) is not bool:
        abort(400)
    room[0]['title'] = request.json.get('title', room[0]['title'])
    room[0]['description'] = request.json.get('description', room[0]['description'])
    room[0]['available'] = request.json.get('available', room[0]['available'])
    return jsonify({'room': room[0]})

@app.route('/api/v1.0/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    room = [room for room in rooms if room['id'] == room_id]
    if len(room) == 0:
        abort(404)
    rooms.remove(room[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)