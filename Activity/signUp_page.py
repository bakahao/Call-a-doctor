import flet 
from flet import *
from flet_route import Params, Basket
import os


class SignUpPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Sign Up"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

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
                                                content=TextField(label="Enter Full Name (Same as IC)", color="BLACK")
                                                ),
                                                Container(
                                                    Container(
                                                        alignment=alignment.center,
                                                        margin=margin.symmetric(horizontal= 10),
                                                        content=TextField(label="Enter E-mail", color="BLACK")
                                                    )
                                                )
                                            ])
                                        ),
                                        Container(
                                            Container(
                                                margin=margin.symmetric(horizontal= 10),
                                                content=TextField(label="Enter phone number", color="BLACK")
                                            )
                                        )
                                    ])
                                ),
                                Container(
                                    margin=margin.symmetric(horizontal= 10),
                                    content=TextField(label="Enter password", color="BLACK")
                                )
                            ])
                        ),
                        Container(
                            alignment=alignment.center,
                            margin=margin.only(top=10),
                            content= ElevatedButton("Sign Up", bgcolor="#3CDAB4", color="BLACK", height=40)
                        )
                    ])
                    )
                ])
            )


        def SignUp_button_clicked(e):
            print("Sign Up clicked time(s)")
            page.update()


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



