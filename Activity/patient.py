import json


class Patient:
    def __init__(self, name=None, email=None, phoneNo=None, role="patient"):
        self.name = name
        self.email = email
        self.phoneNo = phoneNo
        self.role = role

    def patient_to_dict(self):
        return {
            "name" : self.name,
            "email": self.email,
            "phoneNo": self.phoneNo,
            "role": self.role
        }
    
    def dict_to_patient(self, pdict):
        self.name = pdict['name']
        self.email = pdict['email']
        self.phoneNo = pdict['phoneNo']
        self.role = pdict['role']

    def patient_to_json(self):
        jsonStr = json.dumps(self.patient_to_dict(), indent=4)
        return jsonStr
    
    