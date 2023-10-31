import json


class Clinic:
    def __init__(self, name, address, state, city, phoneNo, operationTime, clinicType, serviceType, email, role, status):
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
    
    def clinic_to_json(self):
        jsonStr = json.dumps(self.clinic_to_dict(), indent=4)
        return jsonStr