
from flask import Flask, request, jsonify
from model import Users
from database import db_session

app = Flask(__name__)

@app.route('/clients', methods=['POST'])
def create_user():
    try:
        user_name = request.json['name']
        user = Users(user_name=user_name)
        db_session.add(user)
        db_session.commit()
        return jsonify({"message": "User created", "id": user.id, "name":user.user_name}), 201
    except KeyError:
        return jsonify({"error": "Invalid request data"}), 400

@app.route('/client/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(user_id):
    user = db_session.get(Users, user_id)

    if user is None:
        return jsonify({"message": "User does not exist"}), 404

    if request.method == 'GET':
        return jsonify({"message": "User does exist", "name": user.user_name})

    elif request.method == 'PUT':
        try:
            user.name = request.json['name']
            db_session.commit()
            return jsonify({"message": "Name changed", "current_name": user.user_name})
        except KeyError:
            return jsonify({"error": "Invalid request data"}), 400
    
    elif request.method == 'DELETE':
        db_session.delete(user)
        db_session.commit()
        return jsonify({"message": "User removed", "id": user.id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080, debug=True)
