from flet import *
import flet as ft

def signUp_page(page:ft.Page):
    page.title = "Sign Up"
    page.window_width = 400
    page.window_height = 850
    page.window_resizable = False

    big_container = ft.Container(
        width=400,
        height=750,
        bgcolor="white",
        border_radius=20,
    )

    small_container = ft.Container(
        width=150,
        height=150,
        bgcolor="transparent",
        margin=margin.symmetric(horizontal="110", vertical="50"),
        content=ft.Image(
            src="Call-a-doctor/Activity/assets/images/logo.png",
            width=100,
            height=100
        )
    )

    def SignUp_button_clicked(e):
        print("Sign Up clicked time(s)")
        page.update()

    nameTextField_Container = ft.Container(
        width=380,
        height=60,
        margin=margin.symmetric(vertical=250, horizontal= 10),
        content=ft.TextField(label="Enter Full Name (Same as IC)", color="BLACK")
    )

    emailTextField_Container = ft.Container(
        width=380,
        height=60,
        margin=margin.symmetric(vertical=320, horizontal= 10),
        content=ft.TextField(label="Enter E-mail", color="BLACK")
    )

    phoneTextField_Container = ft.Container(
        width=380,
        height=60,
        margin=margin.symmetric(vertical=390, horizontal= 10),
        content=ft.TextField(label="Enter phone number", color="BLACK")
    )

    passwordTextField_Container = ft.Container(
        width=380,
        height=60,
        margin=margin.symmetric(vertical=460, horizontal= 10),
        content=ft.TextField(label="Enter password", color="BLACK")
    )

    SignUp_button = ft.Container(
        width=200,
        height=40,
        margin=margin.symmetric(vertical=530, horizontal=100),
        content= ft.ElevatedButton("Sign Up", on_click=SignUp_button_clicked, bgcolor="#3CDAB4", color="BLACK")
    )



    stack = ft.Stack([big_container,
                      small_container,
                      nameTextField_Container,
                      emailTextField_Container,
                      phoneTextField_Container,
                      passwordTextField_Container,
                      SignUp_button])
    page.add(stack)
    page.update()

if __name__ == '__main__':
    ft.app(target=signUp_page)



