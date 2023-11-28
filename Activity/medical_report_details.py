import flet
from flet import *
from flet_route import Params, Basket
import os
import firebaseHelper
from patient import Patient
import flet as ft

class MedicalReportDetails:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Medical Report Details Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        uid =params.uid
        patientUID = params.patientUID

        firebaseHelper.getUserDictData(patientUID)
        patient = Patient()
        name = firebaseHelper.getUserDictData(patientUID)['name']
        email = firebaseHelper.getUserDictData(patientUID)['email']
        phone = firebaseHelper.getUserDictData(patientUID)['phoneNo']
        allergies = firebaseHelper.getPatientMedicalReportDictData(patientUID).get('allergies')
        gender = firebaseHelper.getPatientMedicalReportDictData(patientUID).get('gender')
        current_med_condition = firebaseHelper.getPatientMedicalReportDictData(patientUID).get('current_med_condition')
        current_medical = firebaseHelper.getPatientMedicalReportDictData(patientUID).get('current_medication')
        pre_med_condition = firebaseHelper.getPatientMedicalReportDictData(patientUID).get('previous_med_condition')
        past_medical = firebaseHelper.getPatientMedicalReportDictData(patientUID).get('past_medication')
        present_illness = firebaseHelper.getPatientMedicalReportDictData(patientUID).get('present_illness')

        def onAaddPrescriptionClick(e):
            page.go(f"/PrescriptionPage/{uid}/{e.control.data}")

        addButton = ElevatedButton("Add Prescription", bgcolor="white", color="black", on_click=onAaddPrescriptionClick)

    
        medical_report_details = Container(
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
                                            value="Gender: " + gender , color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Allergies: " +  allergies, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Current Medical Condition: " + current_med_condition, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Current Medical: " + current_medical, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Previous Medical Condition: " + pre_med_condition, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Past Medical: " + past_medical, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Present Illness: " + present_illness, color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment= alignment.center,
                                        content = addButton
                                    )
                                    
                            ],
                            spacing=10,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
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
            width=150,
            height=50,
            margin=margin.symmetric(horizontal=130, vertical=30),
            content=Text("Medical Report",
                            color="BLACK",
                            size=15,
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
                                            on_click=lambda _:page.go(f"/MedicalReportPage/{uid}")
                                            )
                    )
        
        stack = Stack([big_container,
                    title_container,
                    title_text_container,
                    exit_button_container  ,
                    medical_report_details               
        ])
                
        return View(
            "/MedicalReportDetails/:uid/:patientUID",
            controls=[
            stack
        ]
    )