from flask import Flask, request, jsonify

from model import Users
from database import db_session

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def items():
    user = Users(name=request.json['name'])
    db_session.add(user)
    db_session.commit()
    return jsonify({"message": "User created", "id": user.id}), 201

@app.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def item(user_id):
    if request.method == 'GET':
        user = db_session.get(Users, user_id)
        if user:
            return jsonify({"message": "User found", "name": user.name})
        else:
            return jsonify({"message": "User not found"}), 404
    
    elif request.method == 'PUT':
        user = db_session.get(Users, user_id)
        if user is None:
            return jsonify({"message": "User not found"}), 404

        user.name = request.json['name']
        db_session.commit()

        return jsonify({"message": "Name updated", "new_name": user.name})
    
    elif request.method == 'DELETE':
        user = db_session.get(Users, user_id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        
        db_session.delete(user)
        db_session.commit()

        return jsonify({"message": "User deleted", "id": user.id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
