import flet 
from flet import *
from flet_route import Params, Basket
import os
import firebaseHelper
import clinic_home_page
import flet as ft
import re

class DoctorRegistrationPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Doctor Registration"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
        )

        small_container = Container(
            width=150,
            height=150,
            bgcolor="transparent",
            margin=margin.symmetric(horizontal="110", vertical="50"),
            content=Image(
                src=(os.getcwd()+"/Activity/assets/images/logo.png"),
                width=100,
                height=100,
                
            ),
        )

        text_container = Container(
            width="400",
            bgcolor="transparent",
            margin=margin.only(top='210'),
            content=Text(
                "DOCTOR REGISTRATION",
                style=TextThemeStyle.TITLE_MEDIUM,
                size=20,
                color=colors.BLACK,
                text_align="CENTER"
            )
        )

        nameTextField = TextField(label="Enter Full Name (Same as IC)", color="BLACK")
        emailTextField = TextField(label="Enter E-mail", color="BLACK")
        phoneTextField = TextField(label="Enter phone number", color="BLACK")
        passwordTextField = TextField(label="Enter password", color="BLACK", password=True, can_reveal_password=True)

        nameTextField_Container = Container(
            width=380,
            height=60,
            margin=margin.symmetric(vertical=250, horizontal= 10),
            content=nameTextField
        )

        emailTextField_Container = Container(
            width=380,
            height=60,
            margin=margin.symmetric(vertical=320, horizontal= 10),
            content=emailTextField
        )

        phoneTextField_Container = Container(
            width=380,
            height=60,
            margin=margin.symmetric(vertical=390, horizontal= 10),
            content=phoneTextField
        )

        passwordTextField_Container = Container(
            width=380,
            height=60,
            margin=margin.symmetric(vertical=460, horizontal= 10),
            content=passwordTextField
        )

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

        def close_dlg(dlg_modal):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()


        def SignUp_button_clicked(e):
            name = nameTextField.value
            email = emailTextField.value
            phoneNo = phoneTextField.value
            password = passwordTextField.value

            if (name and email and phoneNo and password):
                # email format validation using a regular expression
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    show_error_dlg("Invalid email format")
                    return

                # phone number format validation
                if not (phoneNo.startswith("0") and 10 <= len(phoneNo) <= 11):
                    show_error_dlg("Invalid phone number format")
                    return

                # password length validation
                if len(password) < 6:
                    show_error_dlg("Password must be at least 6 characters")
                    return
                
                if(firebaseHelper.getUserUIDByEmail(email)):
                    show_error_dlg("The email has been used!")
                else:
                    page.go(f"/clinicAddDoctorPage/{name}/{email}/{password}/{phoneNo}")
            else:
                show_error_dlg("All field must be fill")



        SignUp_button = Container(
            width=200,
            height=40,
            margin=margin.symmetric(vertical=530, horizontal=100),
            content= ElevatedButton("Next", on_click=SignUp_button_clicked, bgcolor="#3CDAB4", color="BLACK")
        )

        cancel_Button = Container(
            width=200,
            height=40,
            margin=margin.symmetric(vertical=590, horizontal=100),
            content= ElevatedButton("Cancel", on_click=lambda _:page.go(f"/clinicHomePage/{clinic_home_page.clinicUID}"), bgcolor="#F17C7C", color="BLACK")
        )


        stack = Stack([big_container,
                        small_container,
                        text_container,
                        nameTextField_Container,
                        emailTextField_Container,
                        phoneTextField_Container,
                        passwordTextField_Container,
                        SignUp_button,
                        cancel_Button])
        
        return View(
            "/doctorRegistration",
            controls=[
                stack
            ]
        )



