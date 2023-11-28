import firebase_admin
from firebase_admin import credentials, db, auth
import os
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

def saveUserDataEmail(email , userDict):
    try:
        uid = getUserUIDByEmail(email)
        ref = db.reference("Users")
        user_ref = ref.child(uid)
        user_ref.set(userDict)
    except:
        print("Error")

def saveClinicData(uid, clinicDict):
    try:
        ref = db.reference("Clinic")
        clinic_ref = ref.child(uid)
        clinic_ref.set(clinicDict)
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

def determineClinicDoctorRole(email):
    try:
        ref = db.reference("Users")
        clinic_ref = db.reference("Clinic")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        clinic = clinic_ref.child(uid)
        user_role = user_ref.child("role").get()
        result = user_role if user_role is not None else clinic.child("role").get()
        return result
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

def getClinicSDataByEmail(email, specificPath):
    try:
        ref = db.reference("ClinicRequest")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        return user_ref.child(specificPath).get()
    except:
        print("Error")

def getClinicDictData(uid):
    try:
        ref = db.reference("Clinic")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error")

def getClinicRDictData(uid):
    try:
        ref = db.reference("ClinicRequest")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error")

def getClinicDictDataLen():
    ref = db.reference('Clinic')
    dictL = ref.get()
    return dictL
    #print(len(dictL))

#Update user's specific data. For example, specificDict = {'status' : 'Online'} will update 
#the user status to online
def updateClinicDataByEmail(email, specificDict):
    try:
        ref = db.reference("ClinicRequest")
        uid = getUserUIDByEmail(email)
        clinic_ref = ref.child(uid)
        clinic_ref.update(specificDict)
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

def getClinicSDataUID(uid, specificPath):
    try:
        ref = db.reference("Clinic")
        clinic_ref = ref.child(uid)
        return clinic_ref.child(specificPath).get()
    except:
        print('error')

def clinicAddDoctor(clinicUID, doctorEmail):
    try:
        ref = db.reference("Clinic")
        clinic_ref = ref.child(clinicUID)
        if (getClinicSDataUID(clinicUID, 'doctorList') == False):
            clinic_ref.update({'doctorList':True})
        
        doctorUID = getUserUIDByEmail(doctorEmail)
        clinicDoctor_ref = clinic_ref.child('doctorList')
        clinicDoctor_ref.child(doctorUID).set(True)
    except:
        print('error')

def getClinicDoctorList(clinicUID):
    try:
        ref = db.reference("Clinic")
        clinic_ref = ref.child(clinicUID)
        clinic_docL_ref = clinic_ref.child("doctorList")
        return clinic_docL_ref.get()
    except:
        print("Error")

def getPatientRequest(uid):
    try:
        ref = db.reference("PatientRequestDoctor")
        request_query = ref.get()
        # Filter requests based on the specified clinic UID or doctor UID
        filtered_requests = {patient_uid: request_details for patient_uid, request_details in request_query.items() if request_details.get("clinic_uid") == uid}
        return filtered_requests
    except:
        print("Error")

def getSPatientRequest(puid):
    try:
        ref = db.reference("PatientRequestDoctor")
        request_details = ref.child(puid)
        return request_details.get()
    except:
        print("Error")

def updatePatientRequest(uid, dict):
    try:
        ref = db.reference("PatientRequestDoctor")
        req_ref = ref.child(uid)
        req_ref.update(dict)
    except:
        print("Error")

def updatePatientRequestStatus(uid, status):
    try:
        ref = db.reference("PatientRequestDoctor")
        req_ref = ref.child(uid)
        req_ref.update({"status": status})
    except:
        print("Error")

def updatePatientRequestReason(uid, reason):
    try:
        ref = db.reference("PatientRequestDoctor")
        req_ref = ref.child(uid)
        req_ref.update({"reason": reason})
    except:
        print("Error")

def updatePatientRequestDoctor(uid, doctorUID):
    try:
        ref = db.reference("PatientRequestDoctor")
        req_ref = ref.child(uid)
        req_ref.update({"doctor_uid": doctorUID})
    except:
        print("Error")

def deleteClinicDoctor(clinicUID, doctorUID):
    try:
        userRef = db.reference("Users")
        clinicRef = db.reference("Clinic")

        userRef.child(doctorUID).delete()
        clinicRef.child(clinicUID).child("doctorList").child(doctorUID).delete()
        auth.delete_user(doctorUID)
        return "The user delete completed"
    except:
        return "Something went wrong! :<"