#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request
from flask_cors import CORS

rooms = [
   {
      "id": 0,
      "name": "Playadito",
      "location": {
         "name": "Vicente Lopez",
         "floor": 2
      },
      "image": "https://www.deliargentina.es/wp-content/uploads/2019/01/Yerba-Mate-Argentina-Playadito-Kilo.png",
      "timeSlot": [
         {
            "timeFrom": "10:00",
            "timeTo": "10:30",
            "owner": None,
            "locked": False
         },
         {
            "timeFrom": "10:30",
            "timeTo": "11:00",
            "owner": "gaston",
            "locked": False
         }
      ]
   },
   {
      "id": 2,
      "name": "CBSé",
      "location": {
         "name": "Vicente Lopez",
         "floor": 2
      },
      "timeSlot": [
         {
            "timeFrom": "10:00",
            "timeTo": "10:30",
            "owner": "gaston",
            "locked": False
         },
         {
            "timeFrom": "10:30",
            "timeTo": "11:00",
            "owner": None,
            "locked": False
         }
      ]
   },
   {
      "id": 3,
      "name": "La Tranquera",
      "location": {
         "name": "Vicente Lopez",
         "floor": 2
      },
      "timeSlot": [
         {
            "timeFrom": "10:00",
            "timeTo": "10:30",
            "owner": None,
            "locked": False
         },
         {
            "timeFrom": "10:30",
            "timeTo": "11:00",
            "owner": None,
            "locked": False
         },
         {
            "timeFrom": "11:00",
            "timeTo": "11:30",
            "owner": None,
            "locked": False
         }
      ]
   },
   {
      "id": 5,
      "name": "Taragüí",
      "location": {
         "name": "Vicente Lopez",
         "floor": 2
      },
      "timeSlot": [
         {
            "timeFrom": "12:00",
            "timeTo": "13:00",
            "owner": None,
            "locked": False
         }
      ]
   },
   {
      "id": 6,
      "name": "Cruz de malta",
      "location": {
         "name": "Almagro",
         "floor": 1
      },
      "timeSlot": [
         {
            "timeFrom": "12:00",
            "timeTo": "12:30",
            "owner": None,
            "locked": False
         },
         {
            "timeFrom": "12:30",
            "timeTo": "13:00",
            "owner": None,
            "locked": False
         }
      ]
   },
   {
      "id": 7,
      "name": "Rosamonte",
      "location": {
         "name": "Almagro",
         "floor": 1
      },
      "timeSlot": [
         {
            "timeFrom": "12:00",
            "timeTo": "12:30",
            "owner": None,
            "locked": False
         },
         {
            "timeFrom": "12:30",
            "timeTo": "13:00",
            "owner": None,
            "locked": False
         }
      ]
   },
   {
      "id": 8,
      "name": "Adelgamate",
      "location": {
         "name": "Vicente Lopez",
         "floor": 5
      },
      "timeSlot": [
         {
            "timeFrom": "12:00",
            "timeTo": "12:30",
            "owner": None,
            "locked": False
         },
         {
            "timeFrom": "12:30",
            "timeTo": "13:00",
            "owner": None,
            "locked": False
         }
      ]
   },
   {
      "id": 9,
      "name": "Nobleza Gaucha",
      "location": {
         "name": "Vicente Lopez",
         "floor": 2
      },
      "timeSlot": [
         {
            "timeFrom": "12:00",
            "timeTo": "12:30",
            "owner": None,
            "locked": False
         },
         {
            "timeFrom": "12:30",
            "timeTo": "13:00",
            "owner": None,
            "locked": False
         }
      ]
   }
]

app = Flask(__name__)
cors = CORS(app)

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
    if not request.json or not 'name' in request.json:
        abort(400)
    room = {
        'id': rooms[-1]['id'] + 1,
        'available': True,
        'name': request.json['name'],
        'location': request.json.get('location'),
        'image': request.json.get('image'),
        'timeSlot': request.json.get('timeSlot')
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
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'available' in request.json and type(request.json['available']) is not bool:
        abort(400)
    room[0]['name'] = request.json.get('name', room[0]['name'])
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
    app.run(debug=True, host='0.0.0.0')

