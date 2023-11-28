import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *
from clinic import Clinic
from request_doctor import RequestDoctor
from patient import Patient
import firebaseHelper
from date_textField import Youdate


class RequestDoctorPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
            page.window_width=400
            page.window_height=850
            page.window_resizable = False
            page.title=("Request Doctor For Dental Clinic Details Page")

            clinicD = getClinicDictData(params.uid)
            cli = Clinic()

            try:
                cli.dict_to_clinic(clinicD)
            except TypeError:
                print("Error: clinicD is None in ClinicDetails")
            
            clinic_uid = params.uid
            user_email = params.email
            user_uid = getUserUIDByEmail(user_email)
            
            symptom = TextField(label="Describe your symptom",bgcolor="white",color="GREY", disabled=False)
                 
            date = Youdate()
            date.set_page(page)
            status = 'pending'
            def confirm_clicked(e):
                try:     
                    req= RequestDoctor(clinic_uid, date.tf.value, date.tf_time.value, status, symptom.value, address.value)
                    jsonReqDoctor = req.request_to_dict()
                    firebaseHelper.saveUserRequestDoctorData(user_uid, jsonReqDoctor)
                except TypeError as e:
                    print("Only can request doctor a time before admin process your request!")

            address = TextField(label="Enter in your home address",bgcolor="white",color="GREY", disabled=False)

            big_container = Container(
                 content = Column([
                      Container(
                            width=400,
                            height=750,
                            bgcolor="white",
                            border_radius=20,
                            content=Column([
                                 Container(
                                      content = Column([
                                        Container(
                                            content=Column([
                                                Container(
                                                    content = Column([
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
                                                                            content=Text("Request Details",
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
                                                                alignment=alignment.center,
                                                                content=symptom   
                                                            )
                                                        ])
                                                    ),
                                                    Container(
                                                        margin=margin.symmetric(horizontal=20),
                                                        content=date.build()
                                                    )
                                                ])
                                            ),
                                            Container(
                                                 margin=margin.symmetric(horizontal=20),
                                                 content=address
                                            )
                                        ])
                                    ),
                                    Container(
                                         alignment=alignment.center,
                                         content = ElevatedButton(
                                                    "Confirm",
                                                    color="BLACK",
                                                    bgcolor="#3CDAB4",
                                                    height=50,
                                                    on_click=confirm_clicked
                                                )
                                    )
                                ])
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
                                        on_click=lambda _:page.go(f"/ClinicDetails/{clinic_uid}/{user_email}")
                                        )
                )
            



            stack = Stack([big_container,
                           exit_button_container
                        ])
            
            return View(
                "/RequestDoctorPage/:uid/:email",
                controls=[
                    stack
                ]
            )