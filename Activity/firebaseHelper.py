import firebase_admin
from firebase_admin import credentials, db, auth
import os
from doctor import Doctor
import requests

cred = credentials.Certificate(os.getcwd() + "\Activity\serviceAccount.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://calladoctor-200ba-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

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
        return user.uid
    except:
        return None

#save data to realtime db
def saveUserData(uid , userDict):
    try:
        ref = db.reference("Users")
        user_ref = ref.child(uid)
        user_ref.set(userDict)
    except:
        print("Error")

def getUserDictData(uid):
    try:
        ref = db.reference("Users")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error")

#Get user's uid by email
def getUserUIDByEmail(email):
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except:
        print("Error")

#Get user's role using email
def getUserRoleByEmail(email):
    try:
        ref = db.reference("Users")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        return user_ref.child("role").get()
    except:
        print("Error")

#Get specific data from user. For example, getUserSDataByEmail(email, 'phoneNo') -> it will return user phoneNo
def getUserSDataByEmail(email, specificPath):
    try:
        ref = db.reference("Users")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        return user_ref.child(specificPath).get()
    except:
        print("Error")