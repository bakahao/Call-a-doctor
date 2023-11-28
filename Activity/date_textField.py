from flet import *
from datepicker import DatePicker
from selection_type import SelectionType
from datetime import datetime

# def main(page: Page):
#     page.window_width=400
#     page.window_height=850
#     page.window_resizable = False
#     page.add(Youdate())
#     page.update()

class Youdate(UserControl):
    def __init__(self):
        super().__init__()
        self.datepicker = None
        self.holidays = [datetime(2023,4,25),datetime(2023,5,1),datetime(2023,6,2)]
        self.locales = ["en_Us"]
        self.selected_locale = None

        self.you_select_date = Text(size=30,weight="bold")

        self.locales_opts = []

        for l in self.locales:
            self.locales_opts.append(
                dropdown.Option(l)
            )

       

        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Please select time first, then only date."),
            actions=[
                TextButton("Cancel",
                           on_click=self.cancel_dlg
                           ),
                TextButton("Confirm",
                           on_click=self.confirm_dlg
                           ),          
            ],
            actions_alignment="end",
            actions_padding=5,
        )

        self.tf = TextField(
            label="Select your available time",
            color = "GREY"
        )

        self.tf_time = TextField(
            label="Available time",
            color = "GREY"
        ) 

        wrap_container = Column([
            Container(
                content=self.tf
            ),
            Container(
                content=self.tf_time
            )
        ])


        self.cal_icon = TextButton(
            icon=icons.CALENDAR_MONTH,
            on_click=self.open_dlg_modal,
            height=40,
            width=40,
            right=0,
            style=ButtonStyle(
                padding=Padding(4,0,0,0),
                shape={
                    MaterialState.DEFAULT:RoundedRectangleBorder(radius=5)
                }
            )
        )

        self.st = Stack([
            #self.tf,
            wrap_container,
            self.cal_icon
        ])
        self.from_to_text = Text(visible=False)



    def set_page(self, page):
        self.page = page



    def build(self):
        return Column([
            self.st,
        ])

    def confirm_dlg(self, e):
        selected_date = self.datepicker.selected_data[0] if len(self.datepicker.selected_data) > 0 else None
        selected_data_str = selected_date.strftime("%Y-%m-%dT%H:%M:%S") if selected_date else None
        formated_date = self._format_date(selected_data_str)
        formated_time = self._format_time(selected_data_str)
        self.tf.value = formated_date
        self.tf_time.value = formated_time

        print("you date", self.tf.value)
        print("Your time", self.tf_time)

        self.you_select_date.value = self.tf.value

        self.dlg_modal.open = False
        self.update()
        self.page.update()

    def cancel_dlg(self,e):
        self.dlg_modal.open = False
        self.page.update()

    def open_dlg_modal(self,e):
        self.datepicker = DatePicker(
            hour_minute=True,
            selected_date=None,
            selection_type=int(0),
            holidays=self.holidays,
            show_three_months=False,
            locale=self.selected_locale,
            
        )
        self.page.dialog=self.dlg_modal
        self.dlg_modal.content=self.datepicker
        self.dlg_modal.open=True
        self.page.update()

    def _format_date(self,date_str):
        if date_str: 
            date_obj = datetime.strptime(date_str,"%Y-%m-%dT%H:%M:%S")
            formated_date = date_obj.strftime("%d/%m/%Y")
            return formated_date
        else:
            return ""
    
    def _format_time(self, date_str):
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
            formatted_time = date_obj.strftime("%H:%M")
            return formatted_time
        else:
            return ""




#app(target=main)