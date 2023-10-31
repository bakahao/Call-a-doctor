import firebase_admin
from firebase_admin import credentials, db, auth
import os

def database():
    cred = credentials.Certificate(os.getcwd() + "\Activity\serviceAccount.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL' : 'https://calladoctor-200ba-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
