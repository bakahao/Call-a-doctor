import json


class Patient:
    def __init__(self, name=None, email=None, phoneNo=None, address=None, role="patient"):
        self.name = name
        self.email = email
        self.phoneNo = phoneNo
        self.address = address
        self.role = role

    def patient_to_dict(self):
        return {
            "name" : self.name,
            "email": self.email,
            "phoneNo": self.phoneNo,
            "address": self.address,
            "role": self.role
        }
    
    def dict_to_patient(self, pdict):
        self.name = pdict['name']
        self.email = pdict['email']
        self.phoneNo = pdict['phoneNo']
        self.address = pdict['address']
        self.role = pdict['role']

    def patient_to_json(self):
        jsonStr = json.dumps(self.patient_to_dict(), indent=4)
        return jsonStr
    
    