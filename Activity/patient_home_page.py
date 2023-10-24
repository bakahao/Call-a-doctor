from flet import *
from flet_route import Params, Basket
import os

def patient_home_page(page:Page):
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
                            icon_color="BLACK")
    )

    clinic_list_button =Container(
        width=150,
        height=150,
        margin=margin.symmetric(vertical=150, horizontal=20),
        content=ElevatedButton(
        width=150,
        height=150,
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
        ])
        
        )
    )
   

    stack =Stack([big_container,
                      title_container,
                      title_text_container,
                      exit_button_container,
                      clinic_list_button
                      ])

    page.add(stack)
    page.update()

if __name__ == '__main__':
    app(target=patient_home_page)
    