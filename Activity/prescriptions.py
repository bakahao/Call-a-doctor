import json

class Prescriptions:
    def __init__(self, patientName=None, doctorUID=None, email=None, phoneNo=None, gender=None, symptoms=None, prescription=None,  date=None):
        self.patientName = patientName
        self.doctorUID = doctorUID
        self.phoneNo = phoneNo
        self.email = email
        self.gender = gender
        self.symptoms = symptoms
        self.prescription = prescription
        self.date = date
      

    def prescription_to_dict(self):
        return {
            'patientName': self.patientName,
            'doctorUID': self.doctorUID,
            'email': self.email,
            'phoneNo': self.phoneNo,
            'gender' : self.gender,
            'symptoms' : self.symptoms,
            'prescription' : self.prescription,
            'date' : self.date
            
            
        }
    
    def prescription_to_doctor(self, prescription_dict):
        self.patientName = prescription_dict['patientName']
        self.doctorUID = prescription_dict['doctorUID']
        self.email = prescription_dict['email']
        self.phoneNo = prescription_dict['phoneNo']
        self.gender = prescription_dict['gender']
        self.symptoms = prescription_dict['symptoms']
        self.prescription = prescription_dict['prescription']
        self.date = prescription_dict['date']
        
        