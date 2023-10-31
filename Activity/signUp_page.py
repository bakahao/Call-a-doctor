import flet 
from flet import *
from flet_route import Params, Basket
import os
import pyrebase
from functools import partial
import firebase_admin 
from firebase_admin import credentials
from patient import Patient
import firebaseHelper

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
        password_textfield = TextField(label="Enter password", color="BLACK")
        phone_textfield = TextField(label="Enter phone number", color="BLACK")

        def close_dlg(e):
                dlg_modal.open = False
                page.go("/")
                page.update


        dlg_modal = AlertDialog(
                modal=True,
                title=Text("Congratulation"),
                content=Text("Registration Successfully"),
                actions=[
                    TextButton("Okay", on_click=close_dlg),
                ],
                actions_alignment=MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )

        def open_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()


        def sign_up_clicked(e):
            if not password_textfield.value or not email_textfield.value or not name_textfield.value or not phone_textfield.value:
                #password_textfield.error_text = "Please enter your password"
                print("ERROR MESSAGESSSS")
            else:
                email_value = email_textfield.value
                password_value = password_textfield.value
                phone_value = phone_textfield.value
                name_value = name_textfield.value
                role = "Patient"

                uid = firebaseHelper.signup(email_value, password_value)
                pat = Patient(name_value, email_value, phone_value, role)
                jsonPat = pat.patient_to_dict()
                firebaseHelper.saveUserData(uid, jsonPat)
                open_dlg_modal(e)


            
        register = Container(
                    content=Column([
                        Container(
                            content= 
                                Column([
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



