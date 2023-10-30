import firebase_admin
from firebase_admin import credentials, db, auth
import os
from doctor import Doctor

cred = credentials.Certificate(os.getcwd() + "\Activity\serviceAccount.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://calladoctor-200ba-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

#For testing only
name = 'Foong Yuh Chung'
email = 'p21013579@student.newinti.edu.my'
password = '123456'
phoneNo = '0123456789'
department = 'Gynecology and Obstetrics'
lenOfSvc = 17
user = auth.get_user_by_email(email=email)
uid = user.uid
print(uid)
doc = Doctor(name, email, phoneNo, department, lenOfSvc)
jsonDoc = doc.doctor_to_dict()
print(jsonDoc)

#Save data to database
ref = db.reference('Users')
user_ref = ref.child(uid)
user_ref.set(jsonDoc)

#Retrieve data from database
print(user_ref.child('role').get())

doc2 = Doctor()
doc2.dict_to_doctor(user_ref.get())
print(doc2.doctor_to_dict())