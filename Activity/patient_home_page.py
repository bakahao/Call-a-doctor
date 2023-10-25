from flet import *
from flet_route import Params, Basket
import os

class PatientHomePage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Patient Home Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

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
            content=Text("Home",
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

        #CREATE CLINIC LIST BUTTON
        clinic_list_button =Container(
            width=150,
            height=150,
            margin=margin.symmetric(vertical=150, horizontal=20),
            content=ElevatedButton(
            width=150,
            height=150,
            on_click=lambda _:page.go("/ClinicList"),
            style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=10),
                    bgcolor="#FFD0D0"
                ),
            content=Column([
                Container(
                width=100,
                height=100,
                content=Image(src=os.getcwd()+ "/Activity/assets/images/clinic.png",
                width=100,
                height=100,
                    ),
                ),
                Container(
                    width=150,
                    height=30,
                    content=Text("Clinic List", color="Black", size=20, style=TextThemeStyle.TITLE_MEDIUM,text_align="CENTER")
                    )
                ]
            )
            
            )
        )

        #CREATE FEEDBACK BUTTON
        feedback_button =Container(
            width=150,
            height=150,
            margin=margin.only(left=200, top=150),
            content=ElevatedButton(
            width=150,
            height=150,
            style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=10),
                    bgcolor="#C5F6BD"
                ),
            content=Column([
                Container(
                width=90,
                height=90,
                margin=margin.only(top=10, left=10),
                content=Image(src=os.getcwd()+ "/Activity/assets/images/review.png",width=100,height=100),
                ),
                Container(
                    width=150,
                    height=30,
                    margin=margin.only(bottom=50),
                    content=Text("Feedback", color="Black", size=20, style=TextThemeStyle.TITLE_MEDIUM,text_align="CENTER")
                    )
                ]
            ),
            
            
            )
        )

        schedule_button =Container(
            width=150,
            height=150,
            margin=margin.only(left=200, top=330),
            content=ElevatedButton(
            width=150,
            height=150,
            style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=10),
                    bgcolor="#BCCCE4"
                ),
            content=Column([
                Container(
                width=90,
                height=90,
                margin=margin.only(top=10, left=10),
                content=Image(src=os.getcwd()+ "/Activity/assets/images/schedule.png",width=100,height=100),
                ),
                Container(
                    width=150,
                    height=30,
                    margin=margin.only(bottom=50),
                    content=Text("Schedule", color="Black", size=20, style=TextThemeStyle.TITLE_MEDIUM,text_align="CENTER")
                    )
                ]
            ),
            
            
            )
        )

        chat_button =Container(
            width=150,
            height=150,
            margin=margin.symmetric(vertical=330, horizontal=20),
            content=ElevatedButton(
            width=150,
            height=150,
            style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=10),
                    bgcolor="#B9F5FD"
                ),
            content=Column([
                Container(
                width=90,
                height=90,
                margin=margin.only(top=10, left=10),
                content=Image(src=os.getcwd()+ "/Activity/assets/images/chat.png",width=100,height=100),
                ),
                Container(
                    width=150,
                    height=30,
                    margin=margin.only(bottom=50),
                    content=Text("Chat", color="Black", size=20, style=TextThemeStyle.TITLE_MEDIUM,text_align="CENTER")
                    )
                ]
            ),
            
            
            )
        )
        stack =Stack([big_container,
                        title_container,
                        title_text_container,
                        exit_button_container,
                        clinic_list_button,
                        feedback_button,
                        schedule_button,
                        chat_button
                        ])
        
        return View(
            "/PatientHomePage",
            controls=[
                stack
            ]
        )

        """page.add(stack)
        page.update()

if __name__ == '__main__':
    app(target=PatientHomePage().view)
    """