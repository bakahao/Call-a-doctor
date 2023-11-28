import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *
from review import Review

class PatientPrescriptionPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Rating Page")

        user_email = params.email

        cl = Column(
                    spacing=10,
                    height=250,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
        

        try:
            user_uid = getUserUIDByEmail(user_email)
            pdict = getPrescriptionDictData(user_uid)
            ddict = getUserDictData(pdict['doctorUID'])

            prescription = pdict['prescription']
            doctor_name = ddict['name']
            date = pdict['date']
            patient_name = pdict['patientName']


            rmd_text = Text(f"Patient Name: {patient_name}\nDate: {date}\nDoctor Name: {doctor_name}\nPrescription: {prescription}", color="BLACK")
            cl.controls.append(Container(
                        content=ElevatedButton(width=600,bgcolor="#AFF7E5",
                                               content=Container(
                                                   alignment=alignment.center_left,
                                                   content=rmd_text
                                               ))
                                               ))
        except:
            print('Error in getting prescription data')


        

        big_container = Container(
                width=400,
                height=750,
                bgcolor="white",
                border_radius=20,
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
                                        content=Text("Prescription",
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
                        alignment=alignment.center,
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
                "/PatientPrescriptionPage/:email",
                controls=[
                    stack
                ]
            )