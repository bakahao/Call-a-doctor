import json


class Patient:
    def __init__(self, name, email, phoneNo, role):
        self.name = name
        self.email = email
        self.phoneNo = phoneNo
        self.role = role

    def patient_to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phoneNo': self.phoneNo,
            'role' : self.role
        }
    
    def patient_to_json(self):
        jsonStr = json.dumps(self.patient_to_dict(), indent=4)
        return jsonStr