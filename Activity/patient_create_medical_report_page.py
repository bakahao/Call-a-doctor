import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *
from medicalReportClass import MedicalReport

class PatientCreateMedicalReportPage:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Patient Create Medical Report Page")


        cl = Column(
                    spacing=10,
                    height=510,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
        email = params.email
        user_uid = getUserUIDByEmail(email)

        gender = Dropdown(label="Select your gender", color="GREY",
                                       options=[
                                             dropdown.Option("Male"),
                                             dropdown.Option("Female")
                                             ])
        previousMedicalCondition = TextField(label="Enter your previous medical condition",bgcolor="white",color="black")
        currentMedicalCondition = TextField(label="Enter your current medical condition",bgcolor="white",color="black")
        allergies = TextField(label="Enter your allergies",bgcolor="white",color="black")
        past_medication = TextField(label="Enter your past medication",bgcolor="white",color="black")
        current_medication = TextField(label="Enter your current medication",bgcolor="white",color="black")
        present_illness = TextField(label="Discribe your current health issue, symptopms, and any progression",bgcolor="white",color="black")

        def confirm_onClick(e):
            try:
                pMedReport = MedicalReport(gender.value,previousMedicalCondition.value,currentMedicalCondition.value,allergies.value,past_medication.value,
                                           current_medication.value,present_illness.value)
                jsonMedReport = pMedReport.report_to_dict()
                savePatientMedicalReportData(user_uid, jsonMedReport)
            except:
                print("Error in confirm_onClick medReport")

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
                                                margin=margin.symmetric(horizontal=20),
                                                content=gender
                                            ),
                                            Container(
                                                margin=margin.symmetric(horizontal=20),
                                                content=previousMedicalCondition
                                            )
                                        ])
                                    ),
                                    Container(
                                            margin=margin.symmetric(horizontal=20),
                                            content=Column([
                                                Container(
                                                    content=currentMedicalCondition
                                                ),
                                                Container(
                                                    content=allergies
                                                )
                                            ])
                                        ),
                                ])
                            ),
                            Container(
                                margin=margin.symmetric(horizontal=20),
                                content=Column([
                                    Container(
                                        content=past_medication
                                    ),
                                    Container(
                                        content=current_medication
                                    )
                                ])
                            )
                        ])
                    ),
                    Container(
                        margin=margin.symmetric(horizontal=20),
                        content=Column([
                            Container(
                                content=present_illness
                            ),
                            Container(
                                alignment=alignment.center,
                                content=ElevatedButton(
                                "Confirm",
                                color="BLACK",
                                bgcolor="#3CDAB4",
                                height=50,
                                on_click=confirm_onClick
                            ))
                        ])
                    )
                ])
                    
            )
        )
        big_container=Container(
                width=400,
                height=750,
                bgcolor="white",
                border_radius=20,
                content=Column([
                    Container(
                        alignment=alignment.center,
                        content=Container(
                                content=Container(
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
                                    content=Text("Create M. Report",
                                    color="BLACK",
                                    size=32,
                                    text_align=("CENTER"),
                                    style=TextThemeStyle.TITLE_MEDIUM,
                                        )
                                    )
                                )
                            ),
                        
                    ),
                    Container(
                        alignment=alignment.center,
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
                                    on_click=lambda _:page.go(f"/PatientMedicalReportPage/{email}"))
            )

        
        stack = Stack([big_container,
                    exit_button_container,
                    
                    ])

        return View(
            "/PatientCreateMedicalReportPage/:email",
            controls=[
                stack
            ]
        )
    
