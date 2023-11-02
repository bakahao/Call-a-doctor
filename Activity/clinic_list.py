import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *

class ClinicList:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Clinic List Page")


        cl = Column(
                    spacing=10,
                    height=250,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
        email = params.email
        def getClinicButton():
            if getClinicDictData(i)['status'] == 'approved':
                    button_text = Text(getClinicDictData(i)['name'], data=i, color="BLACK")
                    cl.controls.append(Container(
                        content=ElevatedButton(bgcolor="#AFF7E5", width=400, on_click=lambda _:page.go(f"/ClinicDetails/{button_text.data}/{email}"),
                                               content=Container(
                                                   width=350,
                                                   content=button_text
                                               ))
                                               
                    ))

        clinicLength = getClinicDictDataLen()
            
        try:
            for i in clinicLength:
                Container(
                     getClinicButton()
                )
                
        except TypeError as e:
            print(f"An error occurred: {e}")


        def handle_button_click(page, button_text):
            print(f"Button clicked with text: {button_text}")
            #page.go("/ClinicDetails", button_text=button_text)
            page.go("/ClinicDetails")

        
        big_container=Container(
                width=400,
                height=750,
                bgcolor="white",
                border_radius=20,
                content=Column([
                    Container(
                        alignment=alignment.center,
                        content=Column([
                            Container(
                                content=Container(
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
                                    content=Text("Clinic List",
                                    color="BLACK",
                                    size=32,
                                    text_align=("CENTER"),
                                    style=TextThemeStyle.TITLE_MEDIUM,
                                        )
                                    )
                                )
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor="white",
                                border_radius=20,
                                margin=margin.symmetric(horizontal=10),
                                content=Image(
                                    src=(os.getcwd()+"/Activity/assets/images/map.png")
                                )
                            )
                        ]),
                    ),
                    Container(
                        margin=margin.symmetric(horizontal=10),
                        alignment=alignment.center,
                        content=cl
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
                                    on_click=lambda _:page.go("/PatientHomePage/:email"))
            )
        
        stack = Stack([big_container,
                    exit_button_container,
                    ])

        return View(
            "/ClinicList/:email",
            controls=[
                stack
            ]
        )
    
