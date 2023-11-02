import flet 
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import authenticate
import firebaseHelper


class LoginPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Login Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False
        
        email_textfield = TextField(label="Enter E-mail", color="BLACK")
        password_textfield = TextField(label="Enter Password", password=True, can_reveal_password=True, color="BLACK")

        def sign_in_clicked(e):
            email = email_textfield.value
            password = password_textfield.value

            id_token = authenticate(email, password)

            if id_token:
                user_role = firebaseHelper.getUserRoleByEmail(email)
                if user_role == 'Patient':
                    page.go(f"/PatientHomePage/{email}")
                elif user_role == 'Admin':
                    page.go("/AdminPage")
                
            else:
                print("Authentication failed. Please check your email and password.")
            



        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
            content=Column([
                        Container(
                            content=Column([
                                Container(
                                    content=Column([
                                        Container(
                                            content=Column([
                                                Container(
                                                    margin=margin.only(top=130),
                                                    alignment=alignment.center,
                                                    content=Image(
                                                        src=(os.getcwd()+"/Activity/assets/images/logo.png"),
                                                        width=150,
                                                        height=150,
                                                    )
                                                ),
                                                Container(
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Welcome to Call a Doctor!",
                                                        style=TextThemeStyle.TITLE_MEDIUM,
                                                        size=20,
                                                        color=colors.BLACK,
                                                        text_align="CENTER"
                                                    )
                                                )
                                            ])
                                        ),
                                        Container(
                                            content=Column([
                                                Container(
                                                    margin=margin.symmetric(horizontal=10),
                                                    alignment=alignment.center,
                                                    content=email_textfield
                                                ),
                                            Container(
                                                margin=margin.symmetric(horizontal= 10),
                                                alignment=alignment.center,
                                                content=password_textfield
                                            )
                                            ])
                                            
                                        )
                                        
                                    ])
                                ),
                                Container(
                                    content=Column([
                                        Container(
                                            margin=margin.only(top=10),
                                            alignment=alignment.center,
                                            content= ElevatedButton("Sign In", bgcolor="#3CDAB4", color="BLACK",
                                                                    width=100, height=40,on_click=sign_in_clicked)
                                        ),
                                        Container(
                                            alignment=alignment.center,
                                            content= ElevatedButton("Sign Up", bgcolor="#DA3C45", color="White",
                                                                    width=100, height=40, on_click=lambda _:page.go("/signUp"))
                                        )
                                    ])
                                )
                            ])
                                ),
                                Container(
                                    content=Column([
                                        Container(
                                            margin=margin.symmetric(vertical=20),
                                            alignment=alignment.center,
                                            content=Container(
                                                    content=(TextButton("Switch to Clinic/Doctor View",on_click=lambda _:page.go("/ClinicLoginPage")))
                                                )
                                        )
                                    ])
                                )   
                            ])
                        )

        stack = Stack([big_container])

    
        return View(
            "/",
            controls=[
                stack
            ]
        )



        


