from firestore.settings import BASE_DIR, FIREBASE_ORM_BUCKET_NAME
import firebase_admin
from firebase_admin import firestore, credentials, storage
import os

cred = credentials.Certificate(os.path.join(BASE_DIR, ".json/certificate.json"))
firebase_admin.initialize_app(cred, {"storageBucket": FIREBASE_ORM_BUCKET_NAME})

db = firestore.client()
store = storage.bucket()
