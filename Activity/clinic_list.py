import flet
from flet import *
from flet_route import Params, Basket
import os


class ClinicList:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False

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
                                content=Text("Clinic List",
                                color="BLACK",
                                size=32,
                                text_align=("CENTER"),
                                style=TextThemeStyle.TITLE_MEDIUM,
                                )
                            )
                        ),
                        Container(
                            width=350,
                            height=300,
                            margin=margin.symmetric(horizontal=10, vertical=10),
                            content=Image(src=os.getcwd()+ "/Activity/assets/images/map.png",)
                            
                        ),
                        
                    ]   
                )
            )
        cl = Column(
            spacing=10,
            height=250,
            width=380,
            scroll=ScrollMode.HIDDEN,
        )
            
        for i in range(1, 21):
            button_text=f"Clinic {i}"
            cl.controls.append(ElevatedButton(button_text,  key=str(i), width=350, bgcolor="#AFF7E5", color="BLACK",
                                              on_click=lambda _, text=button_text: handle_button_click(page, text)))
            
        def handle_button_click(page, button_text):
            print(f"Button clicked with text: {button_text}")
            #page.go("/ClinicDetails", button_text=button_text)
            page.go("/ClinicDetails")

        cl_container = Container(cl,
                                margin=margin.symmetric(vertical=450, horizontal=10))
        
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
                    cl_container
                    ])

        return View(
            "/ClinicList",
            controls=[
                stack
            ]
        )
    
    """ page.add(stack)
        page.update()

app(target=clinicList)"""