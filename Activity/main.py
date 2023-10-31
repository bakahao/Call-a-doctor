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
from chat_page import ChatPage
from clinic_login_page import ClinicLoginPage
from clinic_registration_page import ClinicRegistrationPage
from adminPage import AdminPage


def main(page: Page):
    
    app_routes = [
        path(url="/", clear=True, view=LoginPage().view),
        path(url="/signUp", clear=True, view=SignUpPage().view),
        path(url="/PatientHomePage", clear=False, view=PatientHomePage().view),
        path(url="/ClinicList", clear=False, view=ClinicList().view),
        path(url="/ClinicDetails", clear=False, view=ClinicDetails().view),
        path(url="/DoctorDetails", clear=False, view=DoctorDetails().view),
        path(url="/FeedbackPage", clear=False, view=FeedbackPage().view),
        path(url="/RatingPage", clear=False, view=RatingPage().view),
        path(url="/SchedulePage", clear=False, view=SchedulePage().view),
        path(url="/ChatList", clear=False, view=ChatList().view),
        path(url="/ChatPage", clear=False, view=ChatPage().view),
        path(url="/ClinicLoginPage", clear=False, view=ClinicLoginPage().view),
        path(url="/ClinicRegistrationPage", clear=False, view=ClinicRegistrationPage().view),
        path(url="/AdminPage", clear=False, view=AdminPage().view),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target=main)
