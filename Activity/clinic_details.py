import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *
from clinic import Clinic
from request_doctor import RequestDoctor
from patient import Patient
import firebaseHelper

class ClinicDetails:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
            page.window_width=400
            page.window_height=850
            page.window_resizable = False
            page.title=("Clinic Details Page")

            clinicD = getClinicDictData(params.uid)
            cli = Clinic()
            cli.dict_to_clinic(clinicD)
            
            clinic_uid = params.uid
            user_email = params.email
            user_uid = getUserUIDByEmail(user_email)

            # req= RequestDoctor(user_email, clinic_uid)
            # jsonPatient = req.request_to_dict()
            # firebaseHelper.saveUserRequestDoctorData(user_uid, jsonPatient)
            

            #uid = getUserUIDByEmail(email)
            

            

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
                            Container(
                                    width=350,
                                    height=200,
                                    bgcolor="#AFF7E5",
                                    border_radius=30,
                                    margin=margin.symmetric(horizontal=10),
                                    content=Column([
                                            Container(
                                                    width=100,
                                                    height=100,
                                                    margin=margin.only(top=50, left=10),
                                                    content=Image(
                                                            src=os.getcwd()+ "/Activity/assets/images/clinic_building.png",
                                                    )
                                            ),
                                    ])
                            )
                        ])
            )
            def yes_option(e):

                try:
                    req= RequestDoctor(user_email, clinic_uid)
                    jsonPatient = req.request_to_dict()
                    firebaseHelper.saveUserRequestDoctorData(user_uid, jsonPatient)
                    close_dlg(e)
                except TypeError as e:
                     print("Only can request doctor a time before admin process your request!")
                

            def close_dlg(e):
                dlg_modal.open = False
                page.update()


            dlg_modal = AlertDialog(
                modal=True,
                title=Text("Please confirm"),
                content=Text("Are you sure you want to request a doctor from this clinic?"),
                actions=[
                    TextButton("Yes", on_click=yes_option),
                    TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
            

            def open_dlg_modal(e):
                
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()

            request_doctor_button = Column([
                 Container(
                    width=150,
                    height=30,
                    margin=margin.only(left=130, top=190),
                    content=ElevatedButton("Request Doctor", color="BLACK", bgcolor="WHITE",
                                           on_click=open_dlg_modal)
                 ),
                 Container(
                    width=150,
                    height=30,
                    margin=margin.only(left=130),
                    content=ElevatedButton("Doctor List", color="BLACK", bgcolor="WHITE",
                                        on_click=lambda _:page.go("/DoctorDetails"))
                 )
            ])
            
            clinic_name = Container(
                 width=200,
                 height=70,
                 margin=margin.only(left=130, top=130),
                 content=Text(value=cli.name, color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
            )

            clinic_rating = Container(
                 width=200,
                 height=70,
                 margin=margin.only(left=130, top=150),
                 content=Text("Rating: ", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
            )

            clinic_rating_text = Container(
                 width=200,
                 height=70,
                 margin=margin.only(left=190, top=150),
                 content=Text("5/5 ", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
            )

            exit_button_container = Container(
                    width=40,
                    height=40,
                    margin=margin.symmetric(vertical=35, horizontal=10),
                    content=IconButton(
                                        icons.EXIT_TO_APP_ROUNDED,
                                        icon_color="BLACK",
                                        on_click=lambda _:page.go("/ClinicList/:email")
                                        )
                )
            
            
            
            review_big_container = Column([
                 Container(
                      width=345,
                      height=360,
                      margin=margin.only(top=340, left=10),
                      content=Container(
                           width=100,
                           height=100,
                           content=(Text("Review", color="black", size=32, style=TextThemeStyle.TITLE_SMALL)
                      )
                      )
                 ),
                 
            ])

            review_scroll_bar=Column(
                            spacing=15,
                            height=300,
                            width=345,
                            scroll=ScrollMode.HIDDEN,
                    )
                 
            for i in range(1, 21):
                text = f"Review {i}"
                review_scroll_bar.controls.append(ElevatedButton(text,  key=str(i), width=325, bgcolor="#AFF7E5", color='BLACK'))
                            
                        
            review_small_container = Container(
                    margin=margin.only(top=390, left=20),
                    content=review_scroll_bar
                 )
            



            stack = Stack([big_container,
                        exit_button_container,
                        clinic_name,
                        clinic_rating,
                        clinic_rating_text,
                        request_doctor_button,
                        review_big_container,
                        review_small_container
                        ])
            
            return View(
                "/ClinicDetails/:uid/:email",
                controls=[
                    stack
                ]
            )