import flet
from flet import *
from flet_route import Params, Basket
import os
import flet as ft

class MedicalReportPage:
    def __init__(self):
        pass

   

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Medical Report Page"
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
            content=Text("Doctor",
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
                    content=Text("Patient Condition: Obesity ", color="black", size=16, style=TextThemeStyle.TITLE_MEDIUM)
                )

        view_medical_report_button = Column([
                    Container(
                        width=200,
                        height=30,
                        margin=margin.only(left=130, top=220),
                        content=ElevatedButton("View Medical Report", color="BLACK", bgcolor="WHITE")
                    ),
                    
                ])
        
        add_prescription_button = Column([
                    Container(
                        width=200,
                        height=30,
                        margin=margin.only(left=130, top=260),
                        content=ElevatedButton("Add Prescription", color="BLACK", bgcolor="WHITE")
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
                        view_medical_report_button,
                        add_prescription_button,
                        
                        

                            
                            
        ])
                
        return View(
            "/MedicalReportPage",
            controls=[
            stack
        ]
    )

"""page.add(stack)
        page.update()

if __name__ == '__main__':
    app(target=PatientHomePage().view)
    """

