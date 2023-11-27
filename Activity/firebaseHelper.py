import firebase_admin
from firebase_admin import credentials, db, auth
import os
from patient import Patient
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
    
def saveClinicRequestData(uid , clinicRequest):
    try:
        ref = db.reference("ClinicRequest")
        user_ref = ref.child(uid)
        user_ref.set(clinicRequest)
    except:
        print("Error")

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

def getClinicDataByEmail(email, status):
    try:
        ref = db.reference("ClinicRequest")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        return user_ref.child(status).get()
    except:
        print("Error")

def getClinicDictData(uid):
    try:
        ref = db.reference("ClinicRequest")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error")

def getClinicDictDataLen():
    ref = db.reference('ClinicRequest')
    dictL = ref.get()
    return dictL
    #print(len(dictL))

#Update user's specific data. For example, specificDict = {'status' : 'Online'} will update 
#the user status to online
def updateClinicDataByEmail(email, specificDict):
    try:
        ref = db.reference("ClinicRequest")
       return user_ref.child(specificPath).get()
    except:
        print("Error")

#Update user's specific data. For example, specificDict = {'status' : 'Online'} will update 
#the user status to online
def updateUserSDataByEmail(email, specificDict):
    try:
        ref = db.reference("Users")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        user_ref.update(specificDict)
    except:
        print("Error")

#delete clinic dictionary
def deleteClinicDataByEmail(email):
    try:
        ref = db.reference("ClinicRequest")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        return user_ref.delete()
    except:
        print("Error")

def deleteClinic(email):
    try:
        uid = getUserUIDByEmail(email)
        auth.delete_user(uid)
    except:
        return None
    
def saveUserRequestDoctorData(uid , requestDoctorDict):
    try:
        ref = db.reference("PatientRequestDoctor")
        user_ref = ref.child(uid)
        user_ref.set(requestDoctorDict)
    except:
        print("Error")

def getRequestDoctorUIDByEmail(email):
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except:
        print("Error")

 
