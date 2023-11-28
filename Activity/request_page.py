import os
from flet import *
import flet as ft
from flet_route import Params, Basket
import clinic_home_page
from doctor import Doctor
import firebaseHelper
from patient import Patient

class RequestPage:
    def __init__(self):
        pass


    def view(self, page:ft.Page, params:Params, basket:Basket):
        page.title = "Requests"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        #big container for the white background
        big_container = ft.Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
        )

        title_container = ft.Container(
            width=400,
            height=100,
            bgcolor="#3CDAB4",
            border_radius=ft.BorderRadius(
                top_left=20,
                top_right=20,
                bottom_left=50,
                bottom_right=50
            )
        )

        title_text_container = ft.Container(
            width=400,
            height=60,
            margin=margin.only(top=20),
            alignment=alignment.center,
            content=ft.Text("Request",
                            color="BLACK",
                            size=32,
                            text_align=("CENTER"),
                            style=ft.TextThemeStyle.TITLE_MEDIUM)
        )
        back_button_container = ft.Container(
            width=40,
            height=50,
            margin=margin.symmetric(vertical=30, horizontal=10),
            on_click=lambda _:page.go(f"/clinicHomePage/{clinic_home_page.clinicUID}"),
            content=ft.Image(
                                src="./Activity/assets/images/backSharp.png",),
        )

        def onRequestClick(e):
            page.go(f"/requestDetailsPage/{e.control.data}")

        def patientRequestList():
            patientRequest = []
            for patientUID, request_details in firebaseHelper.getPatientRequest(clinic_home_page.clinicUID).items():
                if (request_details.get('status') != 'Rejected' and request_details.get('status') != 'Approved'):
                    patient = Patient()
                    patient.dict_to_patient(firebaseHelper.getUserDictData(patientUID))
                    patientRequest.append(
                        ft.Container(
                            border_radius=20,
                            width=400,
                            height=90,
                            bgcolor="#3CDAB4",
                            on_click= onRequestClick,
                            data=patientUID,
                            padding=10,
                            content=ft.Column([
                                    ft.Container(
                                        alignment=alignment.top_left,
                                        content=ft.Text(
                                            value="Patient Name: " + patient.name, color="Black", text_align="Left", size=16
                                        ) 
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Status: " + request_details.get("status"), color="Black", text_align="Left", size=16
                                        )
                                    ),
                                    ft.Container(
                                        alignment=alignment.bottom_left,
                                        content=ft.Text(
                                            value="Requesting a doctor", color="Black", text_align="Left", size=16
                                        )
                                    ),
                            ],
                            spacing=1,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            )
                        )
                    )
            return patientRequest
        
        patient_Request_list_row = ft.Container(
            width=400,
            margin=margin.symmetric(vertical=110, horizontal=20),
            content=ft.Column(
                patientRequestList(),
                spacing=10,
            )
        )

        stack = ft.Stack([big_container,
                        title_container,
                        title_text_container,
                        back_button_container,
                        patient_Request_list_row,
                        ])

        return ft.View(
            "/requestPage",
            controls=[
                stack
            ]
        )
        