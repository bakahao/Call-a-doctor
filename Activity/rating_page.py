import flet
from flet import *
from flet_route import Params, Basket
import os

class RatingPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Rating Page")

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
                                content=Text("Feedback",
                                color="BLACK",
                                size=32,
                                text_align=("CENTER"),
                                style=TextThemeStyle.TITLE_MEDIUM,
                                )
                            )
                        ),
                ])
        )

        small_container = Container(
            width=360,
            height=400,
            bgcolor="#B9F5FD",
            margin=margin.symmetric(horizontal=20, vertical=120),
            content=Column([
               Column([
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
               Container(
                   width=280,
                   height=50,
                   margin=margin.only(left=20),
                   #bgcolor="RED",
                   content= Column([
                       Slider(min=0, max=100, divisions=10, label="{value}%"),
                       Container(
                       width=250,
                       height=30,
                       #bgcolor="RED",
                       margin=margin.only(left=20),
                       content=Column([
                           Container(
                                width=250,
                                height=50,                            
                                content=Text("Rate your experience", color="BLACK",size=24, style=TextThemeStyle.TITLE_SMALL,text_align=TextAlign.CENTER),
                           ),
                       ]
                       
                   ),
                   ),
                  
                     
                   ])
               )
            ])
        )
        
        review_textField = Container(
            width=320,
            height=100,
            margin=margin.symmetric(vertical=400, horizontal=40),
            content=TextField(label="Leave a review here", color="BLACK", border_color="black",
                              bgcolor="WHITE", border_radius=30)
        )

        done_button = Container(
            width=100,
            height=40,
            margin=margin.only(top=470, left=135),
            content=ElevatedButton("Done", bgcolor="White", color="BLACK",
                                   on_click=lambda _:page.go("/PatientHomePage"))
        )
        
        exit_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=10),
                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go("/FeedbackPage"))
            )

        stack = Stack([
            big_container,
            exit_button_container,
            small_container,
            review_textField,
            done_button
        ])
            
        return View(
                "/RatingPage",
                controls=[
                    stack
                ]
            )