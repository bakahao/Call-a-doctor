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
        return user.uid
    except:
        return None


#For testing only
# email = 'testing@gmail.com'
# passw = '123456'
# try:
#     print("e")
#     #user = auth.get_user_by_email(email)
#     print(auth.get_user_by_email(email))
#     print("ee")
#     token = authenticate(email, passw)
#     print(token)
      #decode the token to json format
#     print(auth.verify_id_token(token))
    
# except:
#     print('error')