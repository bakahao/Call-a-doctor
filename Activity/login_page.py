import flet 
from flet import *
from flet_route import Params, Basket
import os

class LoginPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Login Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False
        

        #Text container
        text_container = Container(
            width=400,
            height=60,
            bgcolor="transparent",
            margin=margin.symmetric(vertical=300),
            content=Text(
                "Welcome to Call a Doctor!",
                style=TextThemeStyle.TITLE_MEDIUM,
                size=20,
                color=colors.BLACK,
                text_align="CENTER"
            )
        )

        #big container for the white background
        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
        )

        # small container for the logo.png
        small_container = Container(
            width=150,
            height=150,
            margin=120,
            content=Image(
                src=(os.getcwd()+"/Activity/assets/images/logo.png"),
                width=100,
                height=100
            )
        )
        
        emailTextField_Container = Container(
            width=380,
            height=60,
            margin=margin.symmetric(vertical=350, horizontal= 10),
            content=TextField(label="Enter Email", color="BLACK")
        )
        
        passwordTextField_Container = Container(
            width=380,
            height=60,
            margin=margin.symmetric(vertical=415, horizontal= 10),
            content=TextField(label="Enter Password", password=True, can_reveal_password=True, color="BLACK")
        )

        SignIn_button = Container(
            width=200,
            height=40,
            margin=margin.symmetric(vertical=480, horizontal=100),
            content= ElevatedButton("Sign In", on_click=lambda _:page.go("/DoctorHomePage"), bgcolor="#3CDAB4", color="BLACK")
        )
        
        SignUp_button = Container(
            width=200,
            height=40,
            margin=margin.symmetric(vertical=530, horizontal=100),
            content= ElevatedButton("Sign Up", on_click=lambda _:page.go("/signUp"), bgcolor="#DA3C45", color="White")
        )

        # 使用 Stack 包装大容器、文本元素和小容器，以正确的顺序
        stack = Stack([big_container, 
                        small_container, 
                        text_container,emailTextField_Container, 
                        passwordTextField_Container, 
                        SignIn_button,
                        SignUp_button
                        ])
    
        return View(
            "/",
            controls=[
                stack
            ]
        )

    # 将整个 stack 添加到页面
#     page.add(stack)
#     page.update()

# if __name__ == '__main__':
#     ft.app(target=login_page)



        


