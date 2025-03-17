from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from firebase_admin import firestore
from config.firebase_config import initialize_firebase
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from datetime import timedelta
app = Flask(__name__)

CORS(app,origins=['http://localhost:3000'])
db = initialize_firebase()


load_dotenv("secret_key.env")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)   
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return jsonify({"message": "Flask API is running!"})


@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    if not data:
        return jsonify({"message": "No data provided"}), 400

    if not data.get('username'):
        return jsonify({"message": "Username is required"}), 400
    
    if not data.get('password'):
        return jsonify({"message": "Password is required"}), 400
    
    if db.collection('users').document(data.get('username')).get().exists:
        return jsonify({"message": "Username already exists"}), 400
    
    hashed_password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
    data['password'] = hashed_password
    doc_ref = db.collection('users').document(data.get('username'))
    doc_ref.set(data)
    return jsonify({"message": "Data written successfully"})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user_ref = db.collection('users').document(username)
    user_doc = user_ref.get()

    if not user_doc.exists:
        return jsonify({"message": "Invalid username or password"}), 401
    
    user_data = user_doc.to_dict()
    if not bcrypt.check_password_hash(user_data.get('password'), password):
        return jsonify({"message": "Invalid username or password"}), 401
    
    access_token = create_access_token(identity=username)
    response = make_response(jsonify({"message": "Logged in successfully"}))
    response.set_cookie(
        "access_token",
        access_token,
        httponly=True,  # 🔹 JavaScript CANNOT access this cookie
        secure=True,    # 🔹 Only works on HTTPS (enable in production)
        samesite="None"  # 🔹 Prevents CSRF attacks
    )
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)


