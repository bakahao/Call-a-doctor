import flet
from flet import *
from flet_route import Params, Basket
import os


class ChatList:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):

        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Chat List Page")

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
                                content=Text("Chat",
                                color="BLACK",
                                size=32,
                                text_align=("CENTER"),
                                style=TextThemeStyle.TITLE_MEDIUM,
                                )
                            )
                        ),
                ]))
        
        chat_list_container = Column([
            Container(
                width=350,
                height=400,
                #bgcolor="grey",
                margin=margin.symmetric(vertical= 130, horizontal=20),
                content=Column([
                    Container(
                        width=350,
                        height=50,
                        bgcolor="#AFF7E5",
                        border_radius=30,
                        content=Container(
                            content=ElevatedButton(
                                bgcolor="#AFF7E5",
                                on_click=lambda _:page.go("/ChatPage"),
                                content=Container(
                                    width=400,
                                    content=Row([
                                        Icon(icons.ACCOUNT_CIRCLE_OUTLINED, color="BLACK"),
                                        Text("Dr. Name", color="BLACK",),
                                        
                                    ]
                                        
                                        
                                    )
                            ))
                        )

                    )
                ])
                
            )
        ])
        
        exit_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=10),
                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go("/PatientHomePage"))
            )
        
        stack = Stack([big_container,
                    exit_button_container,
                    chat_list_container
                    ])

        return View(
            "/ChatList",
            controls=[
                stack
            ]
        )