import flet
from flet import *
from flet_route import Params, Basket
import os
from clinic import Clinic
from patient import Patient
from firebaseHelper import *

class DoctorDetails:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
            page.window_width=400
            page.window_height=850
            page.window_resizable = False
            page.title=("Doctor Details Page")

            clinicD = getClinicDictData(params.uid)
            cli = Clinic()
            cli.dict_to_clinic(clinicD)
            
            clinic_uid = params.uid
            user_email = params.email
            user_uid = getUserUIDByEmail(user_email)

        
            big_container = Container(
                width=400,
                    height=750,
                    bgcolor="white",
                    border_radius=20,
                    content=Column([
                        Container(
                            width=400,
                            height=100,
                            bgcolor="#3CDAB4",
                            border_radius=BorderRadius(
                            top_left=20,
                            top_right=20,
                            bottom_left=50,
                            bottom_right=50,
                            ),
                            content=Container(
                                    margin=margin.only(top=30),
                                    content=Text("Details",
                                    color="BLACK",
                                    size=32,
                                    text_align=("CENTER"),
                                    style=TextThemeStyle.TITLE_MEDIUM,
                                    )
                                )
                            ),
                    ])
            )
            display_doctor_scroll_bar=Column(
                            spacing=20,
                            scroll=ScrollMode.HIDDEN,
                    )
            
        
                

            exit_button_container = Container(
                    width=40,
                    height=40,
                    margin=margin.symmetric(vertical=35, horizontal=10),
                    content=IconButton(
                                        icons.EXIT_TO_APP_ROUNDED,
                                        icon_color="BLACK",
                                        on_click=lambda _:page.go(f"/ClinicDetails/{clinic_uid}/{user_email}")
                                        )
                )
            
            

            stack = Stack([
                        big_container,
                        exit_button_container,
                        ])
            
            return View(
                "/DoctorDetails/:uid/:email",
                controls=[
                    stack
                ]
            )