import flet
from flet import *
from flet_route import Params, Basket
import os
import flet as ft
import firebaseHelper
from patient import Patient

class MedicalReportPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Medical Report Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        uid = params.uid
        patient = Patient()
        
        def onAppoinmentClick(e):
            page.go(f"/MedicalReportDetails/{uid}/{e.control.data}")
        
        # Create an elevated button for appoinment
        def createAppointmentButton():
            appoinmentButton=[]
            for patientUID, request_details in firebaseHelper.getPatientRequestDoctor(uid).items():
                firebaseHelper.getUserDictData(patientUID)
                patient = Patient()
                patient.dict_to_patient(firebaseHelper.getUserDictData(patientUID))  
                name = patient.name
                phone = patient.phoneNo
                email = patient.email
                symptoms = firebaseHelper.getPatientRequestDoctorDictData(patientUID).get('symptom')
            
                if firebaseHelper.getPatientRequestDoctorDictData(patientUID)['status'] == 'Approved':
                    appoinmentButton.append(
                        Container(
                            border_radius=20,
                            width=400,
                            height=90,
                            bgcolor="#3CDAB4",
                            on_click=onAppoinmentClick,
                            data=patientUID,
                            padding=10,
                            content=ft.Column([
                                    ft.Container(
                                        alignment=alignment.top_left,
                                        content=ft.Text(
                                            value="Patient Name: " + name, color="Black", text_align="Left", size=16
                                        ) 
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Symptom: " +  symptoms, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Phone: " + phone, color="Black", text_align="Left", size=16
                                        )
                                    ),
                            ],
                            spacing=1,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            )
                        )
                    )
                    
            return appoinmentButton
            
        appoinment_button_list_row = ft.Container(
            width=400,
            margin=margin.symmetric(vertical=110, horizontal=20),
            content=ft.Column(
                createAppointmentButton(),
                spacing=10,
            )
        )
            


        """for patientUID, request_details in firebaseHelper.getPatientRequestDoctor(uid).items():
            print(f"Patient UID: {patientUID}")
            print("Request Details:")
            print("  Clinic UID:", request_details.get("clinic_uid"))
            print("  User Email:", request_details.get("user_email"))

            createAppointmentButton(patientUID)"""


        #big container for the white background
        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20
        )

    

        title_container = Container(
            width=400,
            height=100,
            bgcolor="#3CDAB4",
            border_radius=BorderRadius(
                top_left=20,
                top_right=20,
                bottom_left=50,
                bottom_right=50
            )
        )

        title_text_container = Container(
            width=150,
            height=60,
            margin=margin.symmetric(horizontal=130, vertical=30),
            content=Text("Patient List",
                            color="BLACK",
                            size=16,
                            text_align=("CENTER"),
                            style=TextThemeStyle.TITLE_MEDIUM)
        )
        
        exit_button_container = Container(
                        width=40,
                        height=40,
                        margin=margin.symmetric(vertical=35, horizontal=10),
                        content=IconButton(
                                            icons.EXIT_TO_APP_ROUNDED,
                                            icon_color="BLACK",
                                            on_click=lambda _:page.go(f"/DoctorHomePage/{uid}")
                                            )
                    )
        
        stack = Stack([big_container,
                    title_container,
                    title_text_container,
                    appoinment_button_list_row,
                    exit_button_container                 
        ])
                
        return View(
            "/MedicalReportPage/:uid",
            controls=[
            stack
        ]
    )

"""page.add(stack)
        page.update()

if __name__ == '__main__':
    app(target=PatientHomePage().view)
    """

