
import flet as ft
from login_page import login_page
from signUp_page import signUp_page

def main(page:ft.Page):
    login_page(page)
    
    

if __name__ == '__main__':
    ft.app(target=main)

