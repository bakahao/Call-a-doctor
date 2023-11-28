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

            try:
                cli.dict_to_clinic(clinicD)
            except TypeError:
                print("Error: clinicD is None in ClinicDetails")
            
            clinic_uid = params.uid
            user_email = params.email
            user_uid = getUserUIDByEmail(user_email)
            
            def navigateRequestDoctorDetails(e):
                    page.go(f"/RequestDoctorPage/{clinic_uid}/{user_email}")
            cl = Column(
                    spacing=10,
                    height=370,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
            
            
            reviewLen = getReviewDataLenByUID(clinic_uid)
            totalRating = 0
            count = 0
            try:
                for i in reviewLen:
                    review_text = Text(getReviewDictData(clinic_uid, i)['content'], data=i, color="BLACK", size=18)
                    rating_text = Text(getReviewDictData(clinic_uid, i)['rating'], data=i, color="BLACK", size=18)

                    ratingValue = rating_text.value
                    totalRating = ratingValue + totalRating

                    cl.controls.append(Container(
                        bgcolor="#AFF7E5", 
                        width=800,
                        height=50,
                        border_radius=30,
                        content=ElevatedButton(
                                bgcolor="#AFF7E5",
                                content=Container(
                                    content=Row([
                                            Container(
                                                content=Container(
                                                width=220,
                                                height=70,
                                                content=Container(
                                                     alignment=alignment.center_left,
                                                    content= review_text
                                                )
                                            ),
                                        ),
                                            Container(
                                                content=Container(
                                                alignment=alignment.center_right,
                                                width=50,
                                                content=rating_text
                                            )
                                        )
                                    ])
                                )        
                             )
                        
                        ))
                    count += 1
            except:
                 print("No review found")
            
            try:
                totalRating = totalRating/count
            except:
                 print("Error in totalRating")

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
                                            content=Text("Details",
                                            color="BLACK",
                                            size=32,
                                            text_align=("CENTER"),
                                            style=TextThemeStyle.TITLE_MEDIUM,
                                            )
                                        )
                                    ),
                                    Container(
                                            height=200,
                                            bgcolor="#AFF7E5",
                                            border_radius=30,
                                            margin=margin.symmetric(horizontal=10),
                                            content=Row([
                                                    Container(
                                                            width=100,
                                                            height=100,
                                                            margin=margin.symmetric(horizontal=10),
                                                            content=Image(
                                                                    src=os.getcwd()+ "/Activity/assets/images/clinic_building.png",
                                                            )
                                                    ),
                                                    Container(
                                                        content=Column([
                                                            Container(
                                                                margin=margin.only(top=20),
                                                                content=Text(value=cli.name, color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
                                                            ),
                                                            Container(
                                                                content=Row([
                                                                    Container(
                                                                            content=Text("Rating: ", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
                                                                    ),
                                                                    Container(
                                                                            content=Text(f"{totalRating}/5", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
                                                                    )
                                                                ])
                                                            ),
                                                            Container(
                                                                content=Column([
                                                                    Container(
                                                                            content=ElevatedButton("Request Doctor", color="BLACK", bgcolor="WHITE", width=150,
                                                                                                on_click=navigateRequestDoctorDetails)
                                                                        ),
                                                                        Container(
                                                                            content=ElevatedButton("Doctor List", color="BLACK", bgcolor="WHITE",width=150,
                                                                                                on_click=lambda _:page.go(f"/DoctorDetails/{clinic_uid}/{user_email}"))
                                                                        )
                                                                ])
                                                            )
                                                        ])
                                                    )
                                            ])
                                    )
                                ])
                         ),
                         Container(
                              margin=margin.symmetric(horizontal=20),
                              content=Column([
                                   Container(
                                        content=Text("Review", color="black", size=32, style=TextThemeStyle.TITLE_SMALL)
                                   ),
                                   Container(
                                        content=cl
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
                                        on_click=lambda _:page.go(f"/ClinicList/{user_email}")
                                        )
                )

            


            stack = Stack([big_container,
                        exit_button_container,
                        ])
            
            return View(
                "/ClinicDetails/:uid/:email",
                controls=[
                    stack
                ]
            )