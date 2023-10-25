import flet
from flet import *
from flet_route import Params, Basket
import os

class ClinicDetails:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
            page.window_width=400
            page.window_height=850
            page.window_resizable = False

            """text = params.get("text")
            print(text)"""
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

            request_doctor_button = Column([
                 Container(
                    width=150,
                    height=30,
                    margin=margin.only(left=130, top=190),
                    content=ElevatedButton("Request Doctor", color="BLACK", bgcolor="WHITE")
                 ),
                 Container(
                    width=150,
                    height=30,
                    margin=margin.only(left=130),
                    content=ElevatedButton("Doctor List", color="BLACK", bgcolor="WHITE")
                 )
            ])
            
            clinic_name = Container(
                 width=200,
                 height=70,
                 margin=margin.only(left=130, top=130),
                 content=Text("Clinic 1", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
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
                                        on_click=lambda _:page.go("/ClinicList")
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
                spacing=10,
                height=300,
                width=345,
                scroll=ScrollMode.HIDDEN,
        )
            
            



            stack = Stack([big_container,
                        exit_button_container,
                        clinic_name,
                        clinic_rating,
                        clinic_rating_text,
                        request_doctor_button,
                        review_big_container,
                        
                        ])
            
            return View(
                "/ClinicDetails",
                controls=[
                    stack
                ]
            )

"""page.add(stack)
        page.update()

app(target=clinicList)"""


"""return View(
            "/ClinicDetails",
            controls=[
                stack
            ]
        )"""