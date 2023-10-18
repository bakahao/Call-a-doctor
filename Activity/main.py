from flet import *
from patient_home import topbar

def main(page: Page):
    BG = '#3CDAB4'
    page.padding = 0
    page.spacing = 0
    page.add(
        topbar
    )

app(target=main)
