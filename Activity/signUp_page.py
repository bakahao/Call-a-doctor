import flet 
from flet import *
from flet_route import Params, Basket
import os
from functools import partial
import firebase_admin 
from firebase_admin import credentials
from patient import Patient
import firebaseHelper
import flet as ft
import re

class SignUpPage:
    def __init__(self):
        pass


    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Sign Up"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        name_textfield = TextField(label="Enter Full Name (Same as IC)", color="BLACK")
        email_textfield = TextField(label="Enter E-mail", color="BLACK")
        password_textfield = TextField(label="Enter password", color="BLACK", can_reveal_password=True, password=True)
        phone_textfield = TextField(label="Enter phone number", color="BLACK")
        address_textfield = TextField(label="Enter address", color="BLACK")

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
            page.go("/")
            page.update()

        def sign_up_clicked(e):
            if not password_textfield.value or not email_textfield.value or not name_textfield.value or not phone_textfield.value or not address_textfield.value:
                show_error_dlg("All field must be fill")
            else:
                email_value = email_textfield.value
                password_value = password_textfield.value
                phone_value = phone_textfield.value
                name_value = name_textfield.value
                address_value = address_textfield.value
                role = "Patient"

                # Email validation using a regular expression
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email_value):
                    show_error_dlg("Invalid email format")
                # Phone number validation
                elif not (phone_value.startswith("0") and 10 <= len(phone_value) <= 11):
                    show_error_dlg("Invalid phone number format")
                # Password validation
                elif len(password_value) < 6:
                    show_error_dlg("Password must be at least 6 characters")
                elif firebaseHelper.getUserUIDByEmail(email_value):
                    show_error_dlg("The email has been used!")
                else:
                    uid = firebaseHelper.signup(email_value, password_value)
                    pat = Patient(name_value, email_value, phone_value, address_value, role)
                    jsonPat = pat.patient_to_dict()
                    firebaseHelper.saveUserData(uid, jsonPat)
                    show_success_dlg("Registered successfully")


            
        register = Container(
                    content=Column([
                        Container(
                            content=Column([
                                 Container(
                                      content=Column([
                                            Container(
                                                content=Column([
                                                    Container(
                                                        alignment=alignment.center,
                                                        content=Column([
                                                            Container(
                                                                margin=margin.symmetric(horizontal=10),
                                                                content=name_textfield
                                                                ),
                                                                Container(
                                                                    alignment=alignment.center,
                                                                    margin=margin.symmetric(horizontal= 10),
                                                                    content=email_textfield
                                                                )
                                                            ])
                                                        ),
                                                            Container(
                                                                margin=margin.symmetric(horizontal= 10),
                                                                content=phone_textfield
                                                        )
                                                    ])
                                                ),
                                                Container(
                                                    margin=margin.symmetric(horizontal= 10),
                                                    content=address_textfield
                                                )
                                            ])
                                 ),
                                 Container(
                                      margin=margin.symmetric(horizontal = 10),
                                      content=password_textfield
                                 )
                            ]) 
                                
                        ),
                        Container(
                            alignment=alignment.center,
                            margin=margin.only(top=10),
                            content= ElevatedButton("Sign Up", bgcolor="#3CDAB4", color="BLACK", height=40,
                                                    on_click=sign_up_clicked)
                        )
                    ])
                    )

        

        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
            content=Column([
                Container(
                    content=Column([
                        Container(
                            alignment=alignment.center,
                            margin=margin.only(top=100),
                            content=Image(
                                src=(os.getcwd()+"/Activity/assets/images/logo.png"),
                                width=150,
                                height=150
                            )
                        ),
                        Container(
                            alignment=alignment.center,
                            content=Text("Register as a patient",
                                        color="BLACK",
                                        style=TextThemeStyle.TITLE_MEDIUM,)
                        )
                    ])
                ),
                Container(
                    register
                )
                
                ])
            )



        exit_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=10),
                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go("/"))
            )


        stack = Stack([big_container,
                        exit_button_container])
        
        return View(
            "/signUp",
            controls=[
                stack
            ]
        )


