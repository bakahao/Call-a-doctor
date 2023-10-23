from flet import *
import flet as ft
import os

def patient_home_page(page:ft.Page):
    page.title = "Patient Home Page"
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
        width=150,
        height=60,
        margin=margin.symmetric(horizontal=130, vertical=30),
        content=ft.Text("Home",
                        color="BLACK",
                        size=32,
                        text_align=("CENTER"),
                        style=ft.TextThemeStyle.TITLE_MEDIUM)
    )
    exit_button_container = ft.Container(
        width=40,
        height=40,
        margin=margin.symmetric(vertical=35, horizontal=10),
        content=ft.IconButton(
                            icons.EXIT_TO_APP_ROUNDED,
                            icon_color="BLACK")
    )

    clinic_list_button = ft.Container(
        width=150,
        height=150,
        margin=margin.symmetric(vertical=150, horizontal=20),
        content=ft.ElevatedButton(
        width=150,
        height=150,
        style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                bgcolor="#FFD0D0"
            ),
        content=ft.Column([
            ft.Container(
            width=100,
            height=100,
            content=ft.Image(src="Call-a-doctor/Activity/assets/images/clinic.png",
            width=100,
            height=100,
                ),
            ),
            ft.Container(
                width=150,
                height=30,
                content=ft.Text("Clinic List", color="Black", size=20, style=ft.TextThemeStyle.TITLE_MEDIUM,text_align="CENTER")
            )
        ])
        
        )
    )
   

    stack = ft.Stack([big_container,
                      title_container,
                      title_text_container,
                      exit_button_container,
                      clinic_list_button
                      ])

    page.add(stack)
    page.update()

if __name__ == '__main__':
    ft.app(target=patient_home_page)
    