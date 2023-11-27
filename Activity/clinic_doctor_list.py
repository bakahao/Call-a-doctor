import os
from flet import *
import flet as ft
from flet_route import Params, Basket
import firebaseHelper
import clinic_home_page
from doctor import Doctor

class ClinicDoctorListPage:
    def __init__(self):
        pass

    def view(self, page:ft.Page, params:Params, basket:Basket):
        page.title = "Doctor List"
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



        def doctorList():
            doctor = []
            for i in firebaseHelper.getClinicDoctorList(clinic_home_page.clinicUID):
                doc = Doctor()
                doc.dict_to_doctor(firebaseHelper.getUserDictData(i))
                doctor.append(
                    ft.Container(
                        border_radius=40,
                        width=400,
                        height=90,
                        bgcolor="#3CDAB4",
                        content=ft.ElevatedButton(
                            width=400,
                            height=90,
                            bgcolor="#3CDAB4",
                            content= ft.Column([
                                ft.Container(
                                    alignment=alignment.top_left,
                                    content=ft.Text(
                                        value="Doctor Name: " + doc.name, color="Black", text_align="Left", size=14
                                    ) 
                                ),
                                ft.Container(
                                    alignment=alignment.bottom_left,
                                    content=ft.Text(
                                        value="Department: " + doc.department, color="Black", text_align="Left", size=14
                                    )
                                ),
                                ft.Container(
                                    alignment=alignment.bottom_left,
                                    content=ft.Text(
                                        value="Length of Service: " + doc.lenOfSvc + "  years", color="Black", text_align="Left", size=14
                                    )
                                ),
                                ft.Container(
                                    alignment=alignment.bottom_left,
                                    content=ft.Text(
                                        value="Status: " + doc.status, color="Black", text_align="Left", size=14
                                    )
                                )
                        ],
                        spacing=1,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        )
                        )
                    )
                )
            return doctor
            
        doctor_list_row = ft.Container(
            width=400,
            margin=margin.symmetric(vertical=110, horizontal=20),
            content=ft.Column(
                doctorList(),
                spacing=10,
            )
        )

        stack = ft.Stack([big_container,
                        title_container,
                        title_text_container,
                        back_button_container,
                        doctor_list_row,
                        ])

        return ft.View(
            "/clinicDoctorListPage",
            controls=[
                stack
            ]
        )


        