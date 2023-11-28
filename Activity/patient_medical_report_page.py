import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *

class PatientMedicalReportPage:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Patient Medical Report Page")


        cl = Column(
                    spacing=10,
                    height=400,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
        email = params.email
        user_uid = getUserUIDByEmail(email)
        try:
            medReportDict = getPatientMedReportDictData(user_uid)
            userDict = getUserDictData(user_uid)
            user_name = userDict['name']
            address = userDict['address']
            phone = userDict['phoneNo']
            gender = medReportDict['gender']
            allergies = medReportDict['allergies']
            past_med_condition = medReportDict['previous_med_condition']
            current_med_condition = medReportDict['current_med_condition']
            past_medication = medReportDict['past_medication']
            current_medication = medReportDict['current_medication']
            present_illness = medReportDict['present_illness']
        

            button_text = Text(f"Patient Name: {user_name}\nAddress: {address}\nPhoneNo: {phone}\nGender: {gender}\nAllergies: {allergies}\nPrevious Medical Condition: {past_med_condition}\nCurrent Medical Condition: {current_med_condition}\nPast Medication: {past_medication}\nCurrent Medication: {current_medication}\nPresent Illness: {present_illness}", 
                            color="BLACK", size=18)
            cl.controls.append(Container(
                            alignment=alignment.center,
                            content=Container(
                                width=500,
                                border_radius=20,
                                margin=margin.symmetric(horizontal=10),
                                bgcolor="#AFF7E5",
                                content=Container(
                                    margin=margin.symmetric(horizontal=10),
                                    content=button_text
                                )
                    ))
                                            
                        )
        except:
            print("No medical report")
        big_container=Container(
                width=400,
                height=750,
                bgcolor="white",
                border_radius=20,
                content=Column([
                    Container(
                        alignment=alignment.center,
                        content=Column([
                            Container(
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
                                    content=Text("Medical Report",
                                    color="BLACK",
                                    size=32,
                                    text_align=("CENTER"),
                                    style=TextThemeStyle.TITLE_MEDIUM,
                                        )
                                    )
                                )
                            ),
                        ]),
                    ),
                    Container(
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
                                    on_click=lambda _:page.go(f"/PatientHomePage/{email}"))
            )

        add_button_container = Container(
            width=40,
            height=40,
            margin=margin.only(top=35, left=310),
            content=IconButton(
                                icons.ADD_BOX_ROUNDED,
                                icon_color="BLACK",
                                on_click=lambda _:page.go(f"/PatientCreateMedicalReportPage/{email}"))
        )
        
        stack = Stack([big_container,
                    exit_button_container,
                    add_button_container,
                    ])

        return View(
            "/PatientMedicalReportPage/:email",
            controls=[
                stack
            ]
        )
    
