import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *
from review import Review

class RatingPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Rating Page")

        user_email = params.email

        try:
            clinicUID = getPatientRequestDoctorDataByEmail(user_email, "clinic_uid")
        except:
            print("No request found")
        
        try:
            user_uid = getUserUIDByEmail(user_email)
        except:
            print("Email get fail")

        rating = Slider(min=1, max=5, divisions=4, label="{value}%")
        review_textField=TextField(label="Leave a review here", color="BLACK", border_color="black",
                              bgcolor="WHITE", border_radius=30)
        
        def close_dlg(e):
                dlg_modal.open = False
                page.update()

        dlg_modal = AlertDialog(
                modal=True,
                title=Text("Review Submit Unsuccessfully"),
                content=Text("Make sure you fill in the rating values and comments"),
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

        def close__done_dlg(e):
                done_dlg_modal.open = False
                page.update()

        done_dlg_modal = AlertDialog(
                modal=True,
                title=Text("Review Submit Successfully"),
                content=Text("Your review was submitted."),
                actions=[
                TextButton("Okay", on_click=close__done_dlg),
                ],
                actions_alignment=MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
                )
            
        def open_done_dlg_modal(e):
                page.dialog = done_dlg_modal
                done_dlg_modal.open = True
                page.update()

        
        def doneButton_clicked(e):
            rating_value = rating.value
            content = review_textField.value
            
            try:
                if (rating_value == None or not content):
                    open_dlg_modal(e)
                else:
                    open_done_dlg_modal(e)
                    review = Review(rating_value, content)
                    jsonReview = review.review_to_dict()
                    saveReviewData(clinicUID, user_uid, jsonReview)
            except:
                print("Error in saving the review")
            


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
                            width=360,
                            height=400,
                            bgcolor="#B9F5FD",
                            margin=margin.symmetric(horizontal=20, vertical=10),
                            border_radius=20,
                            content=Column([
                                Container(
                                    content=Column([
                                        Container(
                                            content=Column([
                                                Container(
                                                    width=100,
                                                    height=100,
                                                    margin=margin.only(left=110, top=20),
                                                    content=Image(src=os.getcwd()+ "/Activity/assets/images/clinic_building.png",width=100,height=100)
                                                ),
                                                Container(
                                                    width=100,
                                                    height=20,
                                                    margin=margin.only(left=110),
                                                    content=Text("Clinic 1", color="BLACK", text_align=TextAlign.CENTER, style=TextThemeStyle.TITLE_SMALL)
                                                )
                                            ]),   
                                        ),
                                        Container(
                                            content=Column([
                                                rating,
                                                Container(
                                                content=Column([
                                                    Container(
                                                        margin=margin.symmetric(horizontal=40),
                                                        width=250,
                                                        height=50,                            
                                                        content=Text("Rate your experience", color="BLACK",size=24, style=TextThemeStyle.TITLE_SMALL,text_align=TextAlign.CENTER),
                                                    ),
                                                    Container(
                                                        margin=margin.symmetric(horizontal=20),
                                                        content=review_textField
                                                    )
                                                ]),
                                            ),
                                            
                                                
                                            ])
                                        )
                                    ])
                                ),
                                Container(
                                    alignment=alignment.center,
                                    content=ElevatedButton("Done", bgcolor="White", color="BLACK",
                                                        on_click=doneButton_clicked)
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
                                    on_click=lambda _:page.go(f"/FeedbackPage/{user_email}"))
            )

        stack = Stack([
            big_container,
            exit_button_container,
        ])
            
        return View(
                "/RatingPage/:email",
                controls=[
                    stack
                ]
            )