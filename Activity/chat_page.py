from flet import *
from flet_route import Params, Basket
import os
import flet

class ChatPage:
    def __init__(self):
        pass
        

    def view(self, page: Page, params: Params, basket: Basket):
            page.window_width=400
            page.window_height=850
            page.window_resizable = False

            type_box_container = Container(
                width=350,
                left=9,
                right=50,
                top=690,

                content= TextField(label="type here", border_radius=20,)
                
                )
            
            send_button_container = Container(
                width=50,
                left=315,
                top=695,
                content=IconButton(icon=icons.SEND)
            )

            profile_chat_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=120, horizontal=10),
                content=Icon(icons.ACCOUNT_CIRCLE_OUTLINED,
                                color="BLACK",
                                )

            )

            chat_box_container = Container(
                width=200,
                height=50,
                bgcolor="#3CDAB4",
                border_radius=20,
                margin=margin.symmetric(vertical=127, horizontal=50),
                content= Text("Wassup Dr Ng ",color="White",) 
            )
                
                
                
             
            

            #big container for the white background
            big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
        )

            title_container = Container(
            width=400,
            height=100,
            bgcolor="#3CDAB4",
            border_radius=BorderRadius(
                top_left=20,
                top_right=20,
                bottom_left=50,
                bottom_right=50
            )
        )

            title_text_container = Container(
            width=150,
            height=60,
            margin=margin.symmetric(horizontal=130, vertical=30),
            content=Text("Chat Page",
                            color="BLACK",
                            size=32,
                            text_align=("CENTER"),
                            style=TextThemeStyle.TITLE_MEDIUM)
        )
            exit_button_container = Container(
            width=40,
            height=40,
            margin=margin.symmetric(vertical=35, horizontal=10),
            content=IconButton(
                                icons.EXIT_TO_APP_ROUNDED,
                                icon_color="BLACK",
                                on_click=lambda _:page.go("/"))
        )
            
            voice_call_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=310),
                content=IconButton(
                                icons.CALL,
                                icon_color="BLACK",
                                on_click=lambda _:page.go("/DoctorHomePage"))
            )
        






            stack =Stack([big_container,
                        title_container,
                        title_text_container,
                        exit_button_container,
                        type_box_container,
                        send_button_container,
                        profile_chat_container,
                        chat_box_container,
                        voice_call_button_container
                        ])

            return View(
            "/ChatPage",
            controls=[
                stack
            ]
        )