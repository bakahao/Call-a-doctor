import json


class Clinic:
    def __init__(self, name=None, address=None, state=None, city=None, phoneNo=None, operationTime=None, 
                 clinicType=None, serviceType=None, email=None, role="Clinic", status="pending"):
        self.name = name
        self.address = address
        self.state = state
        self.city = city
        self.phoneNo = phoneNo
        self.operationTime = operationTime
        self.clinicType = clinicType
        self.serviceType = serviceType
        self.email = email
        #self.password = password
        self.role = role
        self.status = status #Approve/pending/reject

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
            #"password" : self.password,
            "role" : self.role,
            "status" : self.status
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