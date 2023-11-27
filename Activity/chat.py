from flet import *
from flet_route import Params, Basket
import os
import flet as ft

class Chat:
    def __init__(self):
        pass

   

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Chat Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        #big container for the white background
        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20
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
            content=Text("Chat",
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
                                on_click=lambda _:page.go("/DoctorHomePage"))
        )

        chat_box_container =Container(
            left=9,
            top=120,
            margin=margin.only(left=20),
                content=ElevatedButton(
                    width=300,
                    bgcolor="#AFF7E5",
                    on_click=lambda _:page.go("/ChatPage"),
                content=Container(
                    content =Row([
                        Icon(icons.ACCOUNT_CIRCLE_OUTLINED,color="BLACK"),
                        Text("Foong Yuh Chung", color="BLACK"),

                ])
            
                
                )
                )

            )
        
           
                
                                                        
        

        stack =Stack([big_container,
                        title_container,
                        title_text_container,
                        exit_button_container,
                        chat_box_container
                        ])

        return View(
            "/Chat",
            controls=[
                stack
            ]
        )