import json


class MedicalReport:
    def __init__(self, gender=None, previous_med_condition=None, current_med_condition=None, allergies=None, past_medication=None, current_medication=None, 
                 present_illness=None):
        self.gender = gender
        self.previous_med_condition = previous_med_condition
        self.current_med_condition = current_med_condition
        self.allergies = allergies
        self.past_medication = past_medication
        self.current_medication = current_medication
        self.present_illness = present_illness

    def report_to_dict(self):
        return {
            "gender" : self.gender,
            "previous_med_condition" : self.previous_med_condition,
            "current_med_condition" : self.current_med_condition,
            "allergies" : self.allergies,
            "past_medication" : self.past_medication,
            "current_medication" : self.current_medication,
            "present_illness" : self.present_illness,
        }
    
    def dict_to_report(self, cdict):
        self.gender = cdict['gender']
        self.previous_med_condition = cdict['previous_med_condition']
        self.current_med_condition = cdict['current_med_condition']
        self.allergies = cdict['allergies']
        self.past_medication = cdict['past_medication']
        self.current_medication = cdict['current_medication']
        self.present_illness = cdict['present_illness']
    