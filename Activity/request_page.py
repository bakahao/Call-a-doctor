import os
from flet import *
import flet as ft

def request_page(page:ft.Page):
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
        width=40,
        height=50,
        margin=margin.symmetric(vertical=30, horizontal=10),
        content=ft.Image(
                            src=os.getcwd() + "/Activity/assets/images/backSharp.png",)
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you want to accept the request?"),
        actions=[
            ft.TextButton("Accept", on_click=close_dlg),
            ft.TextButton("Reject", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    arr = ["Ng Jun Yong", "Yew Zheng Hong", "Foong Yuh Chung"]

    def patienList(arr):
        patient = []
        for i in arr:
            patient.append(
                ft.Container(
                    border_radius=20,
                    width=400,
                    height=50,
                    bgcolor="#3CDAB4",
                    content=ft.ElevatedButton(
                        width=400,
                        height=50,
                        bgcolor="#3CDAB4",
                        on_click=open_dlg_modal,
                        content= ft.Column([
                            ft.Container(
                                alignment=alignment.top_left,
                                content=ft.Text(
                                    value="Patient Name: " + i, color="Black", text_align="Left", size=16
                                ) 
                            ),
                            ft.Container(
                                alignment=alignment.bottom_left,
                                content=ft.Text(
                                    value="Requesting a doctor", color="Black", text_align="Left", size=16
                                )
                            )
                    ],
                    spacing=1,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    )
                    )
                )
            )
        return patient
    
    patient_list_row = ft.Container(
        width=400,
        margin=margin.symmetric(vertical=110, horizontal=20),
        content=ft.Column(
            patienList(arr),
            spacing=10,
        )
    )

    stack = ft.Stack([big_container,
                      title_container,
                      title_text_container,
                      back_button_container,
                      patient_list_row,
                      ])

    page.add(stack)
    page.update()

if __name__ == '__main__':
    ft.app(target=request_page)
    