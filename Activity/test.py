from flet import *
import flet as ft
from signUp_page import signUp_page

def login_page(page: ft.Page):
    page.title = "Login Page"
    page.window_width = 400
    page.window_height = 850
    page.window_resizable = False
    

    #Text container
    text_container = ft.Container(
        width=400,
        height=60,
        bgcolor="transparent",
        margin=margin.symmetric(vertical=300),
        content=ft.Text(
            "Welcome to Call a Doctor!",
            style=ft.TextThemeStyle.TITLE_MEDIUM,
            size=20,
            color=ft.colors.BLACK,
            text_align="CENTER"
        )
    )

    #big container for the white background
    big_container = ft.Container(
        width=400,
        height=750,
        bgcolor="white",
        border_radius=20,
    )

    # small container for the logo.png
    small_container = ft.Container(
        width=150,
        height=150,
        bgcolor="transparent",
        margin=120,
        content=ft.Image(
            src="Call-a-doctor/Activity/assets/images/logo.png",
            width=100,
            height=100
        )
    )
    
    emailTextField_Container = ft.Container(
        width=380,
        height=60,
        margin=margin.symmetric(vertical=350, horizontal= 10),
        content=ft.TextField(label="Enter Email", color="BLACK")
    )
    passwordTextField_Container = ft.Container(
        width=380,
        height=60,
        margin=margin.symmetric(vertical=415, horizontal= 10),
        content=ft.TextField(label="Enter Password", password=True, can_reveal_password=True, color="BLACK")
    )

    def SignIn_button_clicked(e):
        print("Sign In clicked time(s)")
        page.update()

    def SignUp_button_clicked(e):
        print("Sign Up clicked time(s)")
        page.update()
    
    SignIn_button = ft.Container(
        width=200,
        height=40,
        margin=margin.symmetric(vertical=480, horizontal=100),
        content= ft.ElevatedButton("Sign In", on_click=SignIn_button_clicked, bgcolor="#3CDAB4", color="BLACK")
    )
    
    SignUp_button = ft.Container(
        width=200,
        height=40,
        margin=margin.symmetric(vertical=530, horizontal=100),
        content= ft.ElevatedButton("Sign Up", on_click=SignUp_button_clicked, bgcolor="#DA3C45", color="White")
    )

    # 使用 ft.Stack 包装大容器、文本元素和小容器，以正确的顺序
    stack = ft.Stack([big_container, 
                      small_container, 
                      text_container,emailTextField_Container, 
                      passwordTextField_Container, 
                      SignIn_button,
                      SignUp_button
                      ])

    # 将整个 stack 添加到页面
    # page.add(stack)
    # page.update()

if __name__ == '__main__':
    ft.app(target=login_page)



        


