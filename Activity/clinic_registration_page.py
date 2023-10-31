import flet 
from flet import *
from flet_route import Params, Basket
import os
from clinic import Clinic
import firebaseHelper

class ClinicRegistrationPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Clinic Login Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        def sign_up_button_onClick(e):
            if (not clinic_name.value or not clinic_address.value or not clinic_state.value or not clinic_city.value
                or not clinic_tel.value or not clinic_operaton_time.value or not clinic_type.value or not clinic_service_type.value
                or not clinic_email.value or not clinic_password.value):
                 print("Please fill in all the blanks")
            else:
                role = "Clinic"
                status = "pending"

                uid = firebaseHelper.signup(clinic_email.value, clinic_password.value)
                clinic = Clinic(clinic_name.value, clinic_address.value, clinic_state.value, clinic_city.value,
                                clinic_tel.value, clinic_operaton_time.value, clinic_type.value, clinic_service_type.value,
                                clinic_email.value, role, status)

                
                jsonClinic = clinic.clinic_to_dict()
                firebaseHelper.saveClinicRequestData(uid, jsonClinic)

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
        clinic_name = TextField(label="Name of clinic",bgcolor="white",color="black")
        clinic_address = TextField(label="Clinic Address",bgcolor="white",color="black")
        clinic_state = Dropdown(
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
                            ])
        clinic_city = TextField(label="City",bgcolor="white",color="black")
        clinic_tel = TextField(label="Tel",bgcolor="white",color="black")
        clinic_operaton_time = TextField(label="Operation time for clinic (Hours)",bgcolor="white",color="black")                    
        clinic_type = Dropdown(label="Choose your answer here",options=[
                        dropdown.Option("Private medical clinic"),
                        dropdown.Option("Private dental clinic")
                        ]
                        )
        clinic_service_type = Dropdown(label="Choose your answer here",
                                       options=[
                                             dropdown.Option("General Medication"),
                                             dropdown.Option("Specialist")
                                             ]
                                            )
        
        clinic_email = TextField(label="E-mail",color="BLACK")
        clinic_password = TextField(label="Password",color="BLACK",password=True, can_reveal_password=True)

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
                                                                                                                content=clinic_name
                                                                                                            ),
                                                                                                            Container(
                                                                                                                margin=margin.symmetric(horizontal=30),
                                                                                                                alignment=alignment.center,
                                                                                                                content=clinic_address
                                                                                                            )
                                                                                                        ])
                                                                                                    ),
                                                                                                    Container(
                                                                                                        content=Row([
                                                                                                            Container(
                                                                                                                bgcolor="White",
                                                                                                                margin=margin.only(left=30),
                                                                                                                content=clinic_state
                                                                                                                ),

                                                                                                            Container(
                                                                                                                width=148,
                                                                                                                content=clinic_city
                                                                                                            )
                                                                                                        ])
                                                                                                    )
                                                                                                ])
                                                                                            ),
                                                                                            Container(
                                                                                                content=Column([
                                                                                                    Container(
                                                                                                        margin=margin.symmetric(horizontal=30),
                                                                                                        content=clinic_tel
                                                                                                    ),
                                                                                                    Container(
                                                                                                        margin=margin.symmetric(horizontal=30),
                                                                                                        content=clinic_operaton_time
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
                                                                                                content=clinic_type
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
                                                                                            content=clinic_service_type
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
                                                                                    content=clinic_email
                                                                                ),
                                                                                Container(
                                                                                    margin=margin.symmetric(horizontal=30),
                                                                                    content=clinic_password
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
                                                                        on_click=sign_up_button_onClick
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
                stack,
            ]
        )