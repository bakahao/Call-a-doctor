import flet 
from flet import *
from flet_route import Params, Basket
import os

class AdminPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Login Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False
        

        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
        )

        stack = Stack([big_container])
    
        return View(
            "/AdminPage",
            controls=[
                stack
            ]
        )
