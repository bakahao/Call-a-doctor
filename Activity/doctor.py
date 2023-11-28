import json

class Doctor:
    def __init__(self, name=None, email=None, phoneNo=None, department=None, lenOfSvc=None, clinic=None,status="Online"):
        self.name = name
        self.role = 'Doctor'
        self.email = email
        self.phoneNo = phoneNo
        self.department = department
        self.lenOfSvc = lenOfSvc
        self.status = status
        self.clinic = clinic

    def doctor_to_dict(self):
        return {
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'phoneNo': self.phoneNo,
            'department': self.department,
            'lenOfSvc' : self.lenOfSvc,
            'status' : self.status,
            'clinic' : self.clinic
        }
    
    def dict_to_doctor(self, doctor_dict):
        self.name = doctor_dict['name']
        self.role = doctor_dict['role']
        self.email = doctor_dict['email']
        self.phoneNo = doctor_dict['phoneNo']
        self.department = doctor_dict['department']
        self.lenOfSvc = doctor_dict['lenOfSvc']
        self.status = doctor_dict['status']
        self.clinic = doctor_dict['clinic']
