from flask import render_template, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from . import application
from .db import get_db_connection, close_db_connection  # Correct import



users = {
    "testuser": {"password": "testpassword"}
}

@application.route('/')
def home():
    return render_template('index.html')


@application.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    user = users.get(username, None)
    # print("user from top",user)
    # exit()
    if user and user["password"] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@application.route('/api/items', methods=['GET'])
@jwt_required()
def get_items():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    close_db_connection(connection)
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user, items=items), 200

@application.route('/api/items/<int:item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    close_db_connection(connection)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@application.route('/api/items', methods=['POST'])
@jwt_required()
def create_item():
    new_item = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (new_item["name"], new_item["description"]))
    connection.commit()
    close_db_connection(connection)
    return jsonify(new_item), 201
