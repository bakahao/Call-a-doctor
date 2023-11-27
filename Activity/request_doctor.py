import json


class RequestDoctor:
    def __init__(self, user_email=None, clinic_uid=None):
        self.user_email = user_email
        self.clinic_uid = clinic_uid #clinic uid

    def request_to_dict(self):
        return {
            "user_email": self.user_email,
            "clinic_uid" : self.clinic_uid,
        }
    
    def dict_to_request(self, cdict):
        self.user_email = cdict['user_email']
        self.clinic_uid = cdict['clinic_uid']
        