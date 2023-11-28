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

def savePatientMedicalReportData(uid , medicalReport):
    try:
        ref = db.reference("PatientMedicalReport")
        user_ref = ref.child(uid)
        user_ref.set(medicalReport)
    except:
        print("Error in savePatientMedicalReportData")
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

def getPatientRequestDoctorDictData(uid):
    try:
        ref = db.reference("PatientRequestDoctor")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error in getPatientRequestDoctorDictData")

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

def getClinicDataByEmail(email, specificPath):
    try:
        ref = db.reference("ClinicRequest")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        return user_ref.child(specificPath).get()
    except:
        print("Error")

def getPatientRequestDoctorDataByEmail(email, specificPath):
    try:
        ref = db.reference("PatientRequestDoctor")
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
        print("Error in getClinicDictData")

def getPatientMedReportDictData(uid):
    try:
        ref = db.reference("PatientMedicalReport")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error in getPatientMedReportDictData")

def getPatientRequestDoctorDictData(uid):
    try:
        ref = db.reference("PatientRequestDoctor")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error in getPatientRequestDoctorDictData")



def getPrescriptionDictData(uid):
    try:
        ref = db.reference("Prescription")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error in getPrescriptionDictData")

def getClinicRDictData(uid):
    try:
        ref = db.reference("ClinicRequest")
        user_ref = ref.child(uid)
        return user_ref.get()
    except:
        print("Error")
    
def getReviewDictData(clinic_uid, user_uid):
    try:
        ref = db.reference("Review")
        user_ref = ref.child(clinic_uid).child(user_uid)
        return user_ref.get()
    except:
        print("Error in getReviewDictData")



def getClinicDoctorListUID(uid):
    try:
        ref = db.reference("Clinic")
        user_ref = ref.child(uid).child('doctorList')
        return user_ref.get()
    except:
        print("Error in getClinicDoctorListUID")


def getClinicDictDataLen():
    ref = db.reference('Clinic')
    dictL = ref.get()
    return dictL

def getClinicRDictDataLen():
    ref = db.reference('ClinicRequest')
    dictL = ref.get()
    return dictL

def getPatientRequestDoctorDataLen():
    ref = db.reference('PatientRequestDoctor')
    dictL = ref.get()
    return dictL

def getReviewDataLenByUID(clinicUID):
    ref = db.reference('Review').child(clinicUID)
    dictL = ref.get()
    return dictL


def getClinicDoctorDataLenByUID(uid):
    ref = db.reference('Clinic').child(uid).child('doctorList')
    dictL = ref.get()
    return dictL



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

def updateClinicDataByEmail(email, specificDict):
    try:
        ref = db.reference("ClinicRequest")
        uid = getUserUIDByEmail(email)
        user_ref = ref.child(uid)
        user_ref.update(specificDict)
    except:
        print("Error in updateClinicDataByEmail")

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
        print("Error in saveUserRequestDoctorData")

def saveClinicData(uid, requestClinicRequestDict):
    try:
        ref = db.reference("Clinic")
        user_ref = ref.child(uid)
        user_ref.set(requestClinicRequestDict)
    except:
        print("Error in saveClinicData()")

def saveReviewData(clinic_uid,user_uid, requestReviewDict):
    try:
        ref = db.reference("Review")
        user_ref = ref.child(clinic_uid).child(user_uid)
        user_ref.set(requestReviewDict)
    except:
        print("Error in saveReviewData()")

def updatePatientDoneAppoinmentDataByID(patientUID, specificDict):
            try:
                ref = db.reference("PatientRequestDoctor")
                user_ref = ref.child(patientUID)
                user_ref.update(specificDict)
            except:
                print("Error")

def updateClinicRequestDataByID(clinicUID, specificDict):
            try:
                ref = db.reference("ClinicRequest")
                user_ref = ref.child(clinicUID)
                user_ref.update(specificDict)
            except:
                print("Error")


 
