import json


class Clinic:
    def __init__(self, name=None, address=None, state=None, city=None, phoneNo=None, operationTime=None, 
                 clinicType=None, serviceType=None, email=None, role="Clinic", status="pending", doctorList = False):
        self.name = name
        self.address = address
        self.state = state
        self.city = city
        self.phoneNo = phoneNo
        self.operationTime = operationTime
        self.clinicType = clinicType
        self.serviceType = serviceType
        self.email = email
        self.role = role
        self.status = status #Approve/pending/reject
        self.doctorList = doctorList

    def clinic_to_dict(self):
        return {
            "name" : self.name,
            "address" : self.address,
            "state" : self.state,
            "city" : self.city,
            "phoneNo" : self.phoneNo,
            "operationTime" : self.operationTime,
            "clinicType" : self.clinicType,
            "serviceType" : self.serviceType,
            "email" : self.email,
            "role" : self.role,
            "status" : self.status,
            "doctorList": self.doctorList
        }
    
    def dict_to_clinic(self, cdict):
        self.name = cdict['name']
        self.address = cdict['address']
        self.state = cdict['state']
        self.city = cdict['city']
        self.phoneNo = cdict['phoneNo']
        self.operationTime = cdict['operationTime']
        self.clinicType = cdict['clinicType']
        self.serviceType = cdict['serviceType']
        self.email = cdict['email']
        self.role = cdict['role']
        self.status = cdict['status']
        self.doctorList = cdict['doctorList']

