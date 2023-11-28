import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *

class FeedbackPage:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Feedback Page")

        cl = Column(
                    spacing=10,
                    height=250,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
        
        user_email = params.email

        try:
            clinicUID = getPatientRequestDoctorDataByEmail(user_email, "clinic_uid")
            
        except:
            print("No request found")
        
        try:
            assignedDoctor = getPatientRequestDoctorDataByEmail(user_email, "doctor_uid")
        except:
            print("No assigned Doctor")

        try:
            button_text = Text(getClinicDictData(clinicUID)['name'], color="BLACK")
            cl.controls.append(Container(
                        content=ElevatedButton(bgcolor="#AFF7E5", width=400, on_click=lambda _:page.go(f"/RatingPage/{user_email}"),
                                               content=Container(
                                                   width=350,
                                                   content=button_text
                                               )))
            )
        except:
            print("No review need to rate")

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
                                                content=Text("Feedback",
                                                color="BLACK",
                                                size=32,
                                                text_align=("CENTER"),
                                                style=TextThemeStyle.TITLE_MEDIUM,
                                                )
                                            )
                                        ),
                                ])
                            ),
                            Container(
                                margin=margin.symmetric(horizontal=20),
                                content=Text("Waiting for Review", size=24, color="BLACK", style=TextThemeStyle.TITLE_SMALL, weight="BOLD")
                            )
                        ])
                    ),
                    Container(
                        margin=margin.symmetric(horizontal=20),
                        content=cl
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
                                    on_click=lambda _:page.go(f"/PatientHomePage/{user_email}"))
            )


        stack = Stack([
                big_container,
                exit_button_container,
        
        ])
        return View(
            "/FeedbackPage/:email",
            controls=[
                stack
            ]
        )