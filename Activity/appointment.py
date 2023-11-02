import flet
from flet import *
from flet_route import Params, Basket
import os


class AppoinmentPage:
    def __init__(self):
        pass
        
   

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Appoinment Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        def open_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def close_dlg_modal(e):
            dlg_modal.open = False
            page.update()

        dlg_modal = AlertDialog(
            modal = True,
            title=Text("Please confirm"),
            content=Text("Do you really want to accrpt this appoinment"),
            actions=[
                TextButton("Yes", on_click=close_dlg_modal),
                TextButton("No", on_click=close_dlg_modal),
        ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )



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
            #width=150,
            #height=60,
            margin=margin.symmetric(horizontal=130, vertical=35),
            content=Text("Appoinment",
                            color="BLACK",
                            size=18,
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

        patient_list = Container(
            width=350,
            height=200,
            bgcolor="#AFF7E5",
            border_radius=30,
            margin=margin.only(top=110, left=10),
            # margin=margin.symmetric(horizontal=10),
            content=Column([
                Container(
                width=100,
                height=100,
                margin=margin.only(top=50, left=10),
                content=Image(
                        src=os.getcwd()+ "/Activity/assets/images/profile.png",
                                                        )
                                                        
                                                ),
                                        
                                        ])

                
                                )
                            
                

        patient_name = Container(
                    width=200,
                    height=70,
                    margin=margin.only(left=130, top=160),
                    content=Text("Patient Name: cf", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
                )

        patient_condition = Container(
                    width=200,
                    height=70,
                    margin=margin.only(left=130, top=180),
                    content=Text("Appoinment Date: ", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
                )

        accept_appoinment_button = Column([
                    Container(
                        width=200,
                        height=30,
                        margin=margin.only(left=130, top=220),
                        content=ElevatedButton("Accept", color="BLACK", bgcolor="WHITE", on_click=open_dlg_modal)
                    ),
                    
                ])
        
        reject_appoinment_button = Column([
                    Container(
                        width=200,
                        height=30,
                        margin=margin.only(left=130, top=260),
                        content=ElevatedButton("Reject", color="BLACK", bgcolor="WHITE", on_click=close_dlg_modal)
                    ),
                    
                ])
                
            


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
        
       
                

        stack = Stack([big_container,
                    title_container,
                    title_text_container,
                    patient_list,

                        exit_button_container,
                        patient_name,
                        patient_condition,
                        accept_appoinment_button,
                        reject_appoinment_button
                        
                        

                            
                            
        ])
        
       



        
                
        return View(
            "/AppoinmentPage",
            controls=[
            stack
        ]
    )