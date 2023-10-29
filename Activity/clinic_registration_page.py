import flet 
from flet import *
from flet_route import Params, Basket
import os

class ClinicRegistrationPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Clinic Login Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        def close_dlg(e):
                dlg_modal.open = False
                page.update()


        dlg_modal = AlertDialog(
                modal=True,
                title=Text("Request Sent"),
                content=Text("Your application will be processed by the administrator.\nOnce the clinic application is approved by the administrator, the username and password will be activated."),
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

        cl = Column(
            spacing=10,
            height=500,
            width=380,
            scroll=ScrollMode.ALWAYS,
        )
        cl.controls.append(
            Container(
                content=Column([
                      Container(
                            content=Column([
                                Container(
                                        content=Column([
                                            Container(
                                                content=Column([
                                                        Container(
                                                            content=Column([
                                                                    Container(
                                                                        content=Column([
                                                                            Container(
                                                                                content=Column([
                                                                                    Container(
                                                                                        content=Column([
                                                                                            Container(
                                                                                                content=Column([
                                                                                                            Container(
                                                                                                                margin=margin.symmetric(horizontal=30),
                                                                                                                alignment=alignment.center,
                                                                                                                content=TextField(label="Name of clinic",
                                                                                                                                bgcolor="white",
                                                                                                                                color="black")
                                                                                                            ),
                                                                                                            Container(
                                                                                                                margin=margin.symmetric(horizontal=30),
                                                                                                                alignment=alignment.center,
                                                                                                                content=TextField(label="Clinic Address",
                                                                                                                                bgcolor="white",
                                                                                                                                color="black")
                                                                                                            )
                                                                                                        ])
                                                                                                    ),
                                                                                                    Container(
                                                                                                        content=Row([
                                                                                                            Container(
                                                                                                                bgcolor="White",
                                                                                                                margin=margin.only(left=30),
                                                                                                                content=Dropdown(
                                                                                                                    #border_color="BLACK",
                                                                                                                    width=148,
                                                                                                                    color="grey",
                                                                                                                    label="State",
                                                                                                                    options=[
                                                                                                                        dropdown.Option("Perlis"),
                                                                                                                        dropdown.Option("Kedah"),
                                                                                                                        dropdown.Option("Penang"),
                                                                                                                        dropdown.Option("Perak"),
                                                                                                                        dropdown.Option("Kuala Lumpur"),
                                                                                                                        dropdown.Option("Selangor"),
                                                                                                                        dropdown.Option("Negeri Sembilan"),
                                                                                                                        dropdown.Option("Melaka"),
                                                                                                                        dropdown.Option("Johor"),
                                                                                                                        dropdown.Option("Pahang"),
                                                                                                                        dropdown.Option("Terengganu"),
                                                                                                                        dropdown.Option("Kelantan"),
                                                                                                                        dropdown.Option("Sarawak"),
                                                                                                                        dropdown.Option("Sabah"),

                                                                                                                    ]
                                                                                                                )
                                                                                                            ),
                                                                                                            Container(
                                                                                                                width=148,
                                                                                                                content=TextField(label="City",
                                                                                                                                bgcolor="white",
                                                                                                                                color="black")
                                                                                                            )
                                                                                                        ])
                                                                                                    )
                                                                                                ])
                                                                                            ),
                                                                                            Container(
                                                                                                content=Column([
                                                                                                    Container(
                                                                                                        margin=margin.symmetric(horizontal=30),
                                                                                                        content=TextField(label="Tel",
                                                                                                                                bgcolor="white",
                                                                                                                                color="black")
                                                                                                    ),
                                                                                                    Container(
                                                                                                        margin=margin.symmetric(horizontal=30),
                                                                                                        content=TextField(label="Operation time for clinic (Hours)",
                                                                                                                                bgcolor="white",
                                                                                                                                color="black")
                                                                                                    )
                                                                                                ])
                                                                                            )
                                                                                        ])
                                                                                    ),
                                                                                    Container(
                                                                                        content=Column([
                                                                                            Container(
                                                                                                width=300,
                                                                                                margin=margin.symmetric(horizontal=30),
                                                                                                content=Text("Type of clinic applied for:",
                                                                                                    color="BLACK")
                                                                                            ),
                                                                                            Container(
                                                                                                margin=margin.symmetric(horizontal=30),
                                                                                                bgcolor="White",
                                                                                                content=Dropdown(
                                                                                                    label="Choose your answer here",
                                                                                                    options=[
                                                                                                        dropdown.Option("Private medical clinic"),
                                                                                                        dropdown.Option("Private dental clinic")
                                                                                                    ]
                                                                                                )
                                                                                            )
                                                                                        ])
                                                                                    )
                                                                                ])
                                                                            ),
                                                                            Container(
                                                                                content=Column([
                                                                                    Container(
                                                                                        margin=margin.symmetric(horizontal=30),
                                                                                        content=Text("Type of service provided: ", color="BLACK")
                                                                                    ),
                                                                                    Container(
                                                                                            margin=margin.symmetric(horizontal=30),
                                                                                            bgcolor="White",
                                                                                            content=Dropdown(
                                                                                            label="Choose your answer here",
                                                                                                options=[
                                                                                                    dropdown.Option("General Medication"),
                                                                                                    dropdown.Option("Specialist")
                                                                                                    ]
                                                                                                )
                                                                                            )    
                                                                                        ])
                                                                                    )
                                                                                ])
                                                                            ),
                                                                                ])
                                                                            ),
                                                                            Container(
                                                                                margin=margin.symmetric(horizontal=30),
                                                                                content=Text(
                                                                                        "Account Registration",
                                                                                        weight="BOLD",
                                                                                        size=20,
                                                                                        color="BLACK"
                                                                                )
                                                                            )
                                                                        ])
                                                                    ),
                                                                    Container(
                                                                        content=Column([
                                                                                Container(
                                                                                    margin=margin.symmetric(horizontal=30),
                                                                                    content=TextField(
                                                                                            label="Username",
                                                                                            color="BLACK"
                                                                                    )
                                                                                ),
                                                                                Container(
                                                                                    margin=margin.symmetric(horizontal=30),
                                                                                    content=TextField(
                                                                                            label="Password",
                                                                                            color="BLACK",
                                                                                            password=True, 
                                                                                              can_reveal_password=True,
                                                                                    )
                                                                                )
                                                                        ])
                                                                    )
                                                                ])
                                                            ),
                                                            Container(
                                                                  alignment=alignment.center,
                                                                  content=ElevatedButton(
                                                                        "Confirm",
                                                                        color="BLACK",
                                                                        bgcolor="#3CDAB4",
                                                                        height=50,
                                                                        on_click=open_dlg_modal
                                                                  )
                                                            )
                                                        ])
                                        )
                                    )


        #big container for the white background
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
                                    margin=margin.only(top=50),
                                    content=Image(
                                        src=(os.getcwd()+"/Activity/assets/images/logo.png"),
                                        width=100,
                                        height=100
                                    )
                                ),
                                Container(
                                    alignment=alignment.center,
                                    content=Text("Join Call a Doctor Now!",
                                                color="BLACK",
                                                style=TextThemeStyle.TITLE_MEDIUM,)
                                )
                            ])
                        ),
                        Container(
                            margin=margin.only(top=10),
                            alignment=alignment.center,
                            #bgcolor="Grey300",
                            content=cl,
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
                                    on_click=lambda _:page.go("/ClinicLoginPage"))
            )

        stack = Stack([
            big_container,
            exit_button_container,
        ])

        return View(
            "/ClinicRegistrationPage",
            controls=[
                stack
            ]
        )