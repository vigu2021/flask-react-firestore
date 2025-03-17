import firebase_admin
from firebase_admin import credentials, firestore
import os

def initialize_firebase():
    """Initializes Firebase Admin SDK and Firestore only once."""
    if not firebase_admin._apps:  # ✅ Prevent multiple initializations
        # 🔹 Correct file path since JSON is in the same folder as this script
        cred_path = os.path.join(os.path.dirname(__file__), "invertible-jet-453116-v6-91d9496e9782.json")

        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        print("🔥 Firebase initialized successfully!")

    return firestore.client()  # ✅ Always return Firestore instance
