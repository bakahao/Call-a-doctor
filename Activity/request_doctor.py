import json


class RequestDoctor:
    def __init__(self, clinic_uid=None, date=None, time=None, status='pending', symptom=None, address=None):
        self.clinic_uid = clinic_uid
        self.date = date
        self.time = time
        self.status = status
        self.symptom = symptom
        self.address = address
        
    def request_to_dict(self):
        return {
            "clinic_uid" : self.clinic_uid,
            "date" : self.date,
            "time" : self.time,
            "status" : self.status,
            "symptom" : self.symptom,
            "address" : self.address
        }
    
    def dict_to_request(self, cdict):
        self.clinic_uid = cdict['clinic_uid']
        self.date = cdict['date']
        self.time = cdict['time']
        self.status = cdict['status']
        self.symptom = cdict['symptom']
        self.address = cdict['address']
        