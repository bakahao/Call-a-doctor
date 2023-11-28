import flet
from flet import *
from flet_route import Params, Basket
import os

class Voice:
    def __init__(self):
        pass
        
    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Appointment Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        uid=params.uid
       

        #big container for the white background
        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
            content=Image(src=os.getcwd()+ "/Activity/assets/images/voice.png",width=100,height=100)
        )

        voice_call_container = Container(
                width=150,
                height=150,
                top=50,
                left=220,
                content=Image(src=os.getcwd()+ "/Activity/assets/images/voice.png",width=100,height=100)
        )

        disconnect_container = ElevatedButton(
                icon=icons.CALL_END,
                text="Disconnect",
                width=50,
                height=50,
                top=670,
                left=165,
                bgcolor="#FF4C4C",
                on_click=lambda _:page.go(f"/ChatPage/{uid}")

        )

        stack =Stack([
            big_container,
            voice_call_container,
            disconnect_container
                    
        ])
        
        return View(
            "/VoicePage/:uid",
            controls=[
                stack
            ]
        )


