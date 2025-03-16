import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase():
    # Initialize Firebase Admin SDK
    # Note: You'll need to place your service account key JSON file in the config directory
    cred = credentials.Certificate("invertible-jet-453116-v6-91d9496e9782.json")
    firebase_admin.initialize_app(cred)
    
    # Initialize Firestore client
    db = firestore.client()
    return db 