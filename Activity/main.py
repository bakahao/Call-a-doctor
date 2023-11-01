import flet 
from flet import *
import os
from flet_route import Routing, path
from login_page import LoginPage
from signUp_page import SignUpPage
from patient_home_page import PatientHomePage
from clinic_list import ClinicList
from clinic_details import ClinicDetails
from doctor_home_page import DoctorHomePage
from medical_report import MedicalReportPage
from chat import Chat
from chat_page import ChatPage
from appoinment import AppoinmentPage

def main(page: Page):
    
    app_routes = [
        path(url="/", clear=True, view=LoginPage().view),
        path(url="/signUp", clear=True, view=SignUpPage().view),
        path(url="/PatientHomePage", clear=False, view=PatientHomePage().view),
        path(url="/ClinicList", clear=False, view=ClinicList().view),
        path(url="/ClinicDetails", clear=False, view=ClinicDetails().view),
        path(url="/DoctorHomePage", clear=False, view=DoctorHomePage().view),
        path(url="/MedicalReportPage", clear=False, view=MedicalReportPage().view),
        path(url="/Chat", clear=False, view=Chat().view),
        path(url="/ChatPage", clear=False, view=ChatPage().view),
         path(url="/AppoinmentPage", clear=False, view=AppoinmentPage().view)
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target=main)
