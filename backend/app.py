from flask import Flask, jsonify, request
from flask_cors import CORS
from firebase_admin import firestore
from config.firebase_config import initialize_firebase

app = Flask(__name__)

CORS(app)
db = initialize_firebase()


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
    
    doc_ref = db.collection('users').document(data.get('username'))
    doc_ref.set(data)
    return jsonify({"message": "Data written successfully"})






if __name__ == '__main__':
    app.run(debug=True)


