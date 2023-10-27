import os
from flet import *
import flet as ft

def clinic_doctor_page(page:ft.Page):
    page.title = "Clinic Home Page"
    page.window_width = 400
    page.window_height = 850
    page.window_resizable = False

    #big container for the white background
    big_container = ft.Container(
        width=400,
        height=750,
        bgcolor="white",
        border_radius=20,
    )

    title_container = ft.Container(
        width=400,
        height=100,
        bgcolor="#3CDAB4",
        border_radius=ft.BorderRadius(
            top_left=20,
            top_right=20,
            bottom_left=50,
            bottom_right=50
        )
    )

    title_text_container = ft.Container(
        width=400,
        height=60,
        margin=margin.only(top=20),
        alignment=alignment.center,
        content=ft.Text("Request",
                        color="BLACK",
                        size=32,
                        text_align=("CENTER"),
                        style=ft.TextThemeStyle.TITLE_MEDIUM)
    )
    back_button_container = ft.Container(
        width=400,
        height=50,
        margin=margin.only(top=30),
        alignment=alignment.top_right,
        content=ft.Image(
                            src=os.getcwd() + "/Activity/assets/images/backSharp.png",)
    )



    stack = ft.Stack([big_container,
                      title_container,
                      title_text_container,
                      back_button_container,
                      ])

    page.add(stack)
    page.update()

if __name__ == '__main__':
    ft.app(target=clinic_doctor_page)
    