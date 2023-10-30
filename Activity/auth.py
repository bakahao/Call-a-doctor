import firebase_admin
from firebase_admin import credentials, auth
import os
import requests

cred = credentials.Certificate(os.getcwd() + "\Activity\serviceAccount.json")
firebase_admin.initialize_app(cred)

#check email password if correct return userid token
def authenticate(email,password):
  auth_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key="
  api_key = "AIzaSyB9SImywC8_r5EMTTjw1gmHCC1pKtwbEl8"
  
  payload = {
      "email": email,
      "password": password,
      "returnSecureToken": True
  }
  
  response = requests.post(auth_url + api_key, json=payload)
  
  if response.status_code == 200:
      id_token = response.json()["idToken"]
      return id_token
  else:
      return None

#create user with email password
def signup(email, password):
    try:
        user = auth.create_user(email = email, password = password)
        print("Register successfully")
        return user.uid
    except:
        print("Email already exist")
        return None