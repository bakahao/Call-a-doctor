import flet 
from flet import *
import os
from flet_route import Routing, path
from login_page import LoginPage
from signUp_page import SignUpPage

def main(page: Page):
    
    app_routes = [
        path(url="/", clear=True, view=LoginPage().view),
        path(url="/signUp", clear=True, view=SignUpPage().view),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target=main)
