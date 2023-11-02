import flet 
from flet import *
from flet_route import Params, Basket
import os

from firebaseHelper import *
class AdminPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Login Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False
        

        def getClinicButton():
            if getClinicDictData(i)['status'] == 'pending':
                    button_text = Text(getClinicDictData(i)['name'], data=i, color="BLACK")
                    cl.controls.append(Container(
                        content=ElevatedButton(bgcolor="#AFF7E5", width=400, on_click=lambda _:page.go(f"/ClinicRequestDetails/{button_text.data}"),
                                               content=Container(
                                                   width=350,
                                                   content=button_text
                                               ))
                                               
                    ))
            #page.go("/ClinicRequestDetails")
            return getClinicDictData(i)
 
        cl = Column(
                    spacing=10,
                    height=250,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
        
        clinicLength = getClinicDictDataLen()
        
        try:
            for i in clinicLength:
                Container(
                     getClinicButton()
                )
        except TypeError as e:
            print(f"An error occurred: {e}")

        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
            content=Column([
                Container(
                    margin=margin.symmetric(horizontal=10),
                    content=Row([
                        Container(
                            Container(
                                width=40,
                                height=40,
                                margin=margin.symmetric(vertical=35, horizontal=10),
                                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go("/"))
            )
                        ),
                        Container(
                            content=Text("Clinic Request", size=32, color="BLACK", weight="BOLD")
                        )
                    ])
                ),
                Container(
                    margin=margin.symmetric(horizontal=10),
                    alignment=alignment.center,
                    content=cl
                )
            ])
        )

        stack = Stack([big_container])
    
        return View(
            "/AdminPage",
            controls=[
                stack
            ]
        )
