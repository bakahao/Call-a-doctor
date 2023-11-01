import flet
from flet import *
from flet_route import Params, Basket
import os


class ChatPage:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):

        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Chat Page")

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
                                content=Text("Dr. Name",
                                color="BLACK",
                                size=32,
                                text_align=("CENTER"),
                                style=TextThemeStyle.TITLE_MEDIUM,
                                )
                            )
                        ),
                ]))
        
        
        chat_textField = Container(
            width=320,
            height=100,
            margin=margin.symmetric(vertical=680, horizontal=40),
            content=TextField(color="BLACK", border_color="black",
                              bgcolor="WHITE", border_radius=30)
        )

        exit_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=10),
                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go("/ChatList"))
            )
        
        stack = Stack([big_container,
                    exit_button_container,
                    chat_textField
                    ])

        return View(
            "/ChatPage",
            controls=[
                stack
            ]
        )