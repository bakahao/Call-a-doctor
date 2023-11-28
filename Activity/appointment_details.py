import flet
from flet import *
from flet_route import Params, Basket
import os
import firebaseHelper
from patient import Patient
import flet as ft

class AppointmentDetails:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Appointment Details Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        uid = params.uid
        patientUID = params.patientUID
        firebaseHelper.getUserDictData(patientUID)
        patient = Patient()
        name = firebaseHelper.getUserDictData(patientUID)['name']
        email = firebaseHelper.getUserDictData(patientUID)['email']
        phone = firebaseHelper.getUserDictData(patientUID)['phoneNo']
        address = firebaseHelper.getPatientRequestDoctorDictData(patientUID)['address']
        date = firebaseHelper.getPatientRequestDoctorDictData(patientUID)['date']
        time = firebaseHelper.getPatientRequestDoctorDictData(patientUID)['time']

        appointment_details = Container(
                            border_radius=20,
                            width=400,
                            top=120,
                            left=20,
                            right=20,
                            bgcolor="#7FFFD4",
                            data=patientUID,
                            padding=10,
                            content=ft.Column([
                                    ft.Container(
                                        alignment=alignment.top_left,
                                        content=ft.Text(
                                            value="Patient Details: " , color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.top_left,
                                        content=ft.Text(
                                            value="Patient Name: " + name, color="Black", text_align="Left", size=16
                                        ) 
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Email: " +  email, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Phone: " + phone , color="Black", text_align="Left", size=16
                                        )
                                    )
                            ],
                            spacing=10,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            )
                        )
        
        patient_details = Container(
                            border_radius=20,
                            width=400,
                            top=300,
                            left=20,
                            right=20,
                            bgcolor="#7FFFD4",
                            data=patientUID,
                            padding=10,
                            content=ft.Column([
                                    ft.Container(
                                        alignment=alignment.top_left,
                                        content=ft.Text(
                                            value="Appoinment Details: " , color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.top_left,
                                        content=ft.Text(
                                            value="Date: " + date, color="Black", text_align="Left", size=16
                                        ) 
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Time: " +  time, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Address: " + address , color="Black", text_align="Left", size=16
                                        )
                                    )
                            ],
                            spacing=10,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            )
                        )
        
        def done_button_onClick(e):
            firebaseHelper.updateDoctorDoneAppoinmentDataByID(patientUID,{"doctor_done_appointment":True})
            close_dlg_modal(e)
            page.update()

        def open_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def close_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()


        dlg_modal = AlertDialog(
            modal = True,
            title=Text("Confirmation"),
            content=Text("Did you done the appointment?"),
            actions=[
                TextButton("Yes", on_click=done_button_onClick),
                TextButton("No", on_click=close_dlg_modal)
                
        ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        
        done_button=Container(
            width=190,
            height=45,
            margin=margin.only(left=90, top=500),
            content=ElevatedButton("Done Appointment", color="BLACK", bgcolor="#7FFFD4", on_click=open_dlg_modal
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
                    exit_button_container,
                    appointment_details,
                    patient_details,
                    done_button
                     
        ])

                        
        return View(
                "/AppointmentDetails/:uid/:patientUID",
                controls=[
                stack
            ]
        )