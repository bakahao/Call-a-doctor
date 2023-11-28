import flet
from flet import *
from flet_route import Params, Basket
import os
import firebaseHelper
from patient import Patient
import flet as ft

class AppointmentPage:
    def __init__(self):
        pass
        
    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Appointment Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        def open_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()
            page.go("/Appoinment")

        def close_dlg_modal(e):
            dlg_modal.open = False
            page.go()
            page.update()

        dlg_modal = AlertDialog(
            modal = True,
            title=Text("Please confirm"),
            content=Text("Do you really want to accept this appoinment"),
            actions=[
                TextButton("Yes", on_click=close_dlg_modal),
                TextButton("No", on_click=close_dlg_modal),
        ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        uid = params.uid

        def onAppoinmentClick(e):
            page.go(f"/AppointmentDetails/{uid}/{e.control.data}")

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
                date = firebaseHelper.getPatientRequestDoctorDictData(patientUID)['date']
                time = firebaseHelper.getPatientRequestDoctorDictData(patientUID)['time']

                if firebaseHelper.getPatientRequestDoctorDictData(patientUID)['status'] == 'Approved':
                    appoinmentButton.append(
                        Container(
                            border_radius=20,
                            width=400,
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
                                            value="Date: " +  date, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Time: " + time, color="Black", text_align="Left", size=16
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
            #width=150,
            #height=60,
            margin=margin.symmetric(horizontal=130, vertical=35),
            content=Text("Appointment",
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
                    exit_button_container,
                    
                         
                            
        ])
        
       
        return View(
            "/AppointmentPage/:uid",
            controls=[
            stack
        ]
    )

