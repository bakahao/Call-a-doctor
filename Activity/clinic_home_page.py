import os
from flet import *
from flet_route import Params, Basket
import flet as ft

clinicUID = ''

class ClinicHomePage:
    def __init__(self):
        pass

    def view(self, page:ft.Page, params:Params, basket:Basket):
        global clinicUID
        clinicUID = params.uid
        page.title = "Clinic Home Page"
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
            width=150,
            height=60,
            margin=margin.symmetric(horizontal=130, vertical=30),
            content=ft.Text("Home",
                            color="BLACK",
                            size=32,
                            text_align=("CENTER"),
                            style=ft.TextThemeStyle.TITLE_MEDIUM)
        )
        exit_button_container = ft.Container(
            width=40,
            height=40,
            margin=margin.symmetric(vertical=35, horizontal=10),
            content=ft.IconButton(
                                icons.EXIT_TO_APP_ROUNDED,
                                icon_color="BLACK",
                                on_click=lambda _:page.go("/ClinicLoginPage"))
        )

        request_container = ft.Container(
            width=400,
            height=150,
            margin=margin.symmetric(vertical=110, horizontal=20),
            bgcolor="#FFD0D0",
            content=ft.ElevatedButton(
                bgcolor="#FFD0D0",
                content = ft.Column([ 
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Image(
                            src=os.getcwd() + "/Activity/assets/images/request.png",
                            width=80,
                            height=80,),
                        ),
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Text(value="REQUEST", color="Black",text_align="Center", size=24)
                        ),            
                    ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                style = ft.ButtonStyle(
                shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=0),},),
                on_click=lambda _:page.go("/requestPage")
            ),
        )

        doctor_list_container = ft.Container(
            width=400,
            height=150,
            margin=margin.symmetric(vertical=270, horizontal=20),
            bgcolor="#95ED87",
            content=ft.ElevatedButton(
                bgcolor="#95ED87",
                content = ft.Column([ 
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Image(
                            src=os.getcwd() + "/Activity/assets/images/doctorList.png",
                            width=80,
                            height=80,),
                        ),
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Text(value="DOCTOR LIST", color="Black",text_align="Center", size=24)
                        ),            
                    ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                style = ft.ButtonStyle(
                shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=0),},),
                on_click=lambda _:page.go("/clinicDoctorListPage")
            ),
        )

        doctor_status_container = ft.Container(
            width=400,
            height=150,
            margin=margin.symmetric(vertical=430, horizontal=20),
            bgcolor="#B9F5FD",
            content=ft.ElevatedButton(
                bgcolor="#B9F5FD",
                content = ft.Column([ 
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Image(
                            src=os.getcwd() + "/Activity/assets/images/doctor.png",
                            width=80,
                            height=80,),
                        ),
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Text(value="DOCTOR STATUS", color="Black",text_align="Center", size=24)
                        ),            
                    ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                style = ft.ButtonStyle(
                shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=0),},),
            ),
        )

        doctor_registration_container = ft.Container(
            width=400,
            height=150,
            margin=margin.symmetric(vertical=590, horizontal=20),
            bgcolor="#BCCCE4",
            content=ft.ElevatedButton(
                bgcolor="#BCCCE4",
                content = ft.Column([ 
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Image(
                            src=os.getcwd() + "/Activity/assets/images/doctorRegistration.png",
                            width=80,
                            height=80,),
                        ),
                    ft.Container(
                        alignment = alignment.center,
                        content=ft.Text(value="DOCTOR REGISTRATION", color="Black",text_align="Center", size=24)
                        ),            
                    ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                style = ft.ButtonStyle(
                shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=0),},),
                on_click=lambda _:page.go("/doctorRegistration")
            ),
        )

        stack = ft.Stack([big_container,
                        title_container,
                        title_text_container,
                        exit_button_container,
                        request_container,
                        doctor_list_container,
                        doctor_status_container,
                        doctor_registration_container,
                        ])

        return ft.View(
            "/clinicHomePage/:uid",
            controls=[
                stack
            ]
        )