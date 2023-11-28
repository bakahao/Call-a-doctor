import os
from flet import *
import flet as ft
from flet_route import Params, Basket
from doctor import Doctor
import clinic_home_page
import firebaseHelper

class ClinicAddDoctorPage:
    def __init__(self):
        pass


    def view(self, page:ft.Page, params:Params, basket:Basket):
        #name = str(params.name)
        doc = params.name
        print(doc)

        page.title = "Doctor Registration"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        def show_error_dlg(errorMessage):
            error_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Error"),
                content=ft.Text(errorMessage),
                actions=[
                    ft.TextButton("Confirm", on_click=lambda _: close_dlg(error_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                #on_dismiss=lambda e: print("Modal dialog dismissed!"),
                open=False
            )
            page.dialog = error_dlg
            error_dlg.open = True
            page.update()

        def show_success_dlg(successMessage):
            success_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Complete"),
                content=ft.Text(successMessage),
                actions=[
                    ft.TextButton("Confirm", on_click=lambda _: close_dlg_pagego(success_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                #on_dismiss=lambda _: print("Modal dialog dismissed!"),
                open=False
            )
            page.dialog = success_dlg
            success_dlg.open = True
            page.update()

        def close_dlg(dlg_modal):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()

        def close_dlg_pagego(dlg_modal):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()
            page.go(f"/clinicHomePage/{clinic_home_page.clinicUID}")


        nameTextField = ft.TextField(label="Doctor Name:", color="BLACK", border_radius=20, bgcolor='white', value=params.name, read_only=True)
        departmentTextField = ft.TextField(label="Department:", color="BLACK", border_radius=20, bgcolor='white')
        lengthOfSvcTextField = ft.TextField(label="Length of service(years)", color="BLACK", border_radius=20, bgcolor='white')

        def onClickAdd(e):
            name = nameTextField.value
            email = params.email
            password = params.password
            phoneNo = params.phoneNo
            department = departmentTextField.value
            lenOfSvc = lengthOfSvcTextField.value
            clinic = clinic_home_page.clinicUID

            if (department and lenOfSvc):
                doctor = Doctor(name, email, phoneNo, department, lenOfSvc, clinic)
                firebaseHelper.signup(email, password)
                firebaseHelper.saveUserDataEmail(email, doctor.doctor_to_dict())
                firebaseHelper.clinicAddDoctor(clinic, email)
                show_success_dlg("The doctor registered successfully")
            else:
                show_error_dlg("All field must be fill")

        form_container = ft.Container(
            bgcolor="#B9F5FD",
            height="350",
            width="400",
            margin=margin.only(top=120, left=20, right=20, bottom=300),
            border_radius=20,
            alignment=alignment.center,
            content=ft.Column([
                    ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=15, right = 10, left=10),
                        content=nameTextField,
                    ),
                    ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=10, right = 10, left=10),
                        content=departmentTextField,
                    ),
                    ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=10, right = 10, left=10),
                        content=lengthOfSvcTextField,
                    ),
                    ft.ElevatedButton(
                        content=ft.Text(
                            value='Sign Up',
                            size=20,
                            color='Black'
                        ),
                        height=40,
                        width=140,
                        bgcolor='#6DE3C7',
                        on_click=onClickAdd
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        #big container for the white background
        big_container = ft.Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
            alignment=alignment.center,
            content=form_container
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
            margin=ft.margin.only(top=20),
            alignment=alignment.center,
            content=ft.Text("Add Doctor",
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


        stack = ft.Stack([big_container,
                        title_container,
                        title_text_container,
                        back_button_container,
                        ])

        return ft.View(
            "/clinicAddDoctorPage/:name/:email/:password/:phoneNo",
            controls=[
                stack
            ]
        )
