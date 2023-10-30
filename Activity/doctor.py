import json

class Doctor:
    def __init__(self, name, email, phoneNo, department, lenOfSvc):
        self.name = name
        self.email = email
        self.phoneNo = phoneNo
        self.department = department
        self.lenOfSvc = lenOfSvc

    def doctor_to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phoneNo': self.phoneNo,
            'department': self.department,
            'lenOfSvc' : self.lenOfSvc
        }
    
    def doctor_to_json(self):
        jsonStr = json.dumps(self.doctor_to_dict(), indent=4)
        return jsonStr