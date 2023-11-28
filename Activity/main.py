import flet 
from flet import *
import os
import calendar
import datetime
from flet_route import Routing, path
from login_page import LoginPage
from signUp_page import SignUpPage
from patient_home_page import PatientHomePage
from clinic_list import ClinicList
from clinic_details import ClinicDetails
from doctor_list import DoctorDetails
from feedback_page import FeedbackPage
from rating_page import RatingPage
from schedule_page import SchedulePage
from chat_list import ChatList
from patient_chat_page import ChatPage
from clinic_login_page import ClinicLoginPage
from clinic_registration_page import ClinicRegistrationPage
from adminPage import AdminPage
from clinic_request_details import ClinicRequestDetails
from doctor_home_page import DoctorHomePage
from medical_report import MedicalReportPage
from chat import Chat
from appointment import AppointmentPage
from clinic_home_page import ClinicHomePage
from request_page import RequestPage
from doctorRegistration import DoctorRegistrationPage
from clinic_add_doctor import ClinicAddDoctorPage
from clinic_doctor_list import ClinicDoctorListPage
from clinic_view_request_details import RequestDetailsPage
from request_doctor_page import RequestDoctorPage
from date_textField import Youdate
from patient_prescription_page import PatientPrescriptionPage
from patient_medical_report_page import PatientMedicalReportPage
from patient_create_medical_report_page import PatientCreateMedicalReportPage
from voice import Voice
from appointment_details import AppointmentDetails
from medical_history import MedicalHistory
from medical_report_details import MedicalReportDetails
from prescription import Prescription
from doctor_home_page import DoctorHomePage
from medical_report import MedicalReportPage
from chat import Chat
from chat_page import ChatPage

def main(page: Page):
    
    app_routes = [
        path(url="/", clear=True, view=LoginPage().view),
        path(url="/signUp", clear=True, view=SignUpPage().view),
        path(url="/PatientHomePage/:email", clear=False, view=PatientHomePage().view),
        path(url="/ClinicList/:email", clear=False, view=ClinicList().view),
        path(url="/ClinicDetails/:uid/:email", clear=False, view=ClinicDetails().view),
        path(url="/DoctorDetails/:uid/:email", clear=False, view=DoctorDetails().view),
        path(url="/FeedbackPage/:email", clear=False, view=FeedbackPage().view),
        path(url="/RatingPage/:email", clear=False, view=RatingPage().view),
        path(url="/SchedulePage/:email", clear=False, view=SchedulePage().view),
        path(url="/ChatList/:email", clear=False, view=ChatList().view),
        path(url="/ClinicLoginPage", clear=False, view=ClinicLoginPage().view),
        path(url="/ClinicRegistrationPage", clear=False, view=ClinicRegistrationPage().view),
        path(url="/AdminPage", clear=False, view=AdminPage().view),
        path(url="/ClinicRequestDetails/:uid", clear=False, view=ClinicRequestDetails().view),
        path(url="/DoctorHomePage/:uid", clear=False, view=DoctorHomePage().view),
        path(url="/MedicalReportPage/:uid", clear=False, view=MedicalReportPage().view),
        path(url="/Chat/:uid", clear=False, view=Chat().view),
        path(url="/ChatPage/:uid/:patientUID", clear=False, view=ChatPage().view),
        path(url="/AppointmentPage/:uid", clear=False, view=AppointmentPage().view),
        path(url="/AppointmentDetails/:uid/:patientUID", clear=False, view=AppointmentDetails().view),
        path(url="/clinicHomePage/:uid", clear=False, view=ClinicHomePage().view),
        path(url='/clinicAddDoctorPage/:name/:email/:password/:phoneNo', clear=False, view=ClinicAddDoctorPage().view),
        path(url='/clinicDoctorListPage', clear=False, view=ClinicDoctorListPage().view),
        path(url="/requestDetailsPage/:uid", clear=False, view=RequestDetailsPage().view),
        path(url="/PatientChatPage/:email", clear=False, view=ChatPage().view),
        path(url="/clinicHomePage", clear=False, view=ClinicHomePage().view),
        path(url="/requestPage", clear=False, view=RequestPage().view),
        path(url='/doctorRegistration', clear=False, view=DoctorRegistrationPage().view),
        path(url='/RequestDoctorPage/:uid/:email', clear=False, view=RequestDoctorPage().view),
        path(url='/PatientPrescriptionPage/:email', clear=False, view=PatientPrescriptionPage().view),
        path(url='/PatientMedicalReportPage/:email', clear=False, view=PatientMedicalReportPage().view),
        path(url='/PatientCreateMedicalReportPage/:email', clear=False, view=PatientCreateMedicalReportPage().view),
        path(url='/PrescriptionPage/:uid/:patientUID', clear=False, view=Prescription().view),
        path(url='/VoicePage/:uid/:patientUID', clear=False, view=Voice().view),
        path(url='/MedicalHistory/:uid', clear=False, view=MedicalHistory().view),
        path(url='/MedicalReportDetails/:uid/:patientUID', clear=False, view=MedicalReportDetails().view)
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target=main)
