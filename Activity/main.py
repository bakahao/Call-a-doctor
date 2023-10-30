import flet 
from flet import *
import os
from flet_route import Routing, path
from login_page import LoginPage
from signUp_page import SignUpPage
from patient_home_page import PatientHomePage
from clinic_list import ClinicList
from clinic_details import ClinicDetails
from clinic_home_page import ClinicHomePage
from request_page import RequestPage
from doctorRegistration import DoctorRegistrationPage

def main(page: Page):
    
    app_routes = [
        path(url="/", clear=True, view=LoginPage().view),
        path(url="/signUp", clear=True, view=SignUpPage().view),
        path(url="/PatientHomePage", clear=False, view=PatientHomePage().view),
        path(url="/ClinicList", clear=False, view=ClinicList().view),
        path(url="/ClinicDetails", clear=False, view=ClinicDetails().view),
        path(url="/clinicHomePage", clear=False, view=ClinicHomePage().view),
        path(url="/requestPage", clear=False, view=RequestPage().view),
        path(url='/doctorRegistration', clear=False, view=DoctorRegistrationPage().view)
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target=main)
