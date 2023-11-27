import flet
from flet import *
import calendar
import datetime
from flet_route import Params, Basket

CELL_SIZE = (28, 28)
CELL_BG_COLOR = "WHITE10"
TODAY_BG_COLOR = "teal600"

class SetCalendar(UserControl):
    def __init__(self, start_year=datetime.date.today().year):
        self.curren_year = start_year

        self.m1 = datetime.date.today().month
        self.m2 = self.m1 + 1

        self.click_count: list = []
        self.long_press_count: list = []

        self.current_color = "blue"

        self.selected_date = any

        self.calendar_grid = Column(
            wrap=True,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
        super().__init__()

    def _change_month(self, delta):
        self.m1 = min(max(1, self.m1 + delta), 12)
        self.m2 = min(max(2, self.m2 + delta), 13)

        new_calendar = self.create_month_calendar(self.curren_year)
        self.calendar_grid = new_calendar
        self.update()


    def one_click_date(self, e):
        
        self.selected_date = e.control.data
        e.control.bgcolor = "blue600"
        e.control.update()
        self.update()

    def long_click_date(self, e):
        self.long_press_count.append(e.control.data)
        if len(self.long_press_count )== 2:

            date1, date2 = self.long_press_count

            delta = abs(date2 - date1)
            
            if date1 < date2:
                dates = [
                    date1 + datetime.timedelta(days=x) for x in range
                    (delta.days + 1)
                ]
            else: 
                dates = [
                    date2 + datetime.timedelta(days=x) for x in range
                    (delta.days + 1)
                ]

            for _ in self.calendar_grid.controls[:]:
                for __ in _.controls[:]:
                    if isinstance(__, Row):
                        for box in __.controls[:]:
                            if box.data in dates:
                                box.bgcolor="blie600"
                                box.update()

            self.long_press_count=[]
        else:
            pass



    def create_month_calendar(self, year):
        self.current_year = year
        self.calendar_grid.controls: list = []

        for month in range(self.m1, self.m2):
            month_label = Text(
                f"{calendar.month_name[month]} {self.current_year}",
                size=14,
                weight="bold"
            )
            month_matrix = calendar.monthcalendar(self.current_year, month)
            month_grid = Column(alignment=MainAxisAlignment.CENTER)
            month_grid.controls.append(
                Row(alignment=MainAxisAlignment.START, controls=
                    [month_label],
                    )
            )

            weekday_labels = [
                Container(
                    width=28,
                    height=28,
                    alignment=alignment.center,
                    content=Text(
                        weekday, 
                        size=12, 
                        color="white54",
                    ),
                )
                for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri",
                                 "Sat", "Sum"]
            ]

            weekday_row = Row(controls=weekday_labels)
            month_grid.controls.append(weekday_row)

            for week in month_matrix:
                week_container = Row()
                for day in week:
                    if day == 0:
                        day_container = Container(
                            width=28,
                            height=28,
                        )
                    else:
                        day_container = Container(
                            width=28,
                            height=28,
                            border=border.all(0.5, "white24"),
                            alignment=alignment.center,

                            data=datetime.date(
                                year=self.current_year,
                                month=month,
                                day=day
                            ),
                            on_click=lambda e: self.one_click_date(e),
                            on_long_press=lambda e:self.long_click_date(e),
                            animate=400,
                        )
                    day_label = Text(str(day), size=12)


                    if day==0:
                        day_label = None
                    if(
                        day == datetime.date.today().day
                        and month == datetime.date.today().month
                        and self.curren_year == datetime.date.today().year
                    ):
                        day_container.bgcolor = "teal700"
                    day_container.content = day_label
                    week_container.controls.append(day_container)
                month_grid.controls.append(week_container)

            
        self.calendar_grid.controls.append(month_grid)

        return self.calendar_grid

    def build(self):
        return self.create_month_calendar(self.curren_year)
    

class DateSetUp(UserControl):
    def __init__(self, cal_grid):
        self.cal_grid = cal_grid

        self.prev_btn = BTNPagination("Prev.", lambda e: cal_grid._change_month(-1))
        self.next_btn = BTNPagination("Next", lambda e: cal_grid._change_month(1))


        self.today = Text(
            datetime.date.today().strftime("%B %d, %Y"),
            width=260,
            size=13,
            color="white54",
            weight="w400"
        )

        self.btn_container = Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                self.prev_btn,
                self.next_btn,
            ]
        )

        self.calendar = Container(
            width=320,
            height=45,
            bgcolor="#313131",
            border_radius=8,
            animate=300,
            clip_behavior=ClipBehavior.HARD_EDGE,
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Divider(height=60, color="transparent"),
                    self.cal_grid,
                    Divider(height=10, color="transparent"),
                    self.btn_container,
                ],
            )
        )

        super().__init__()
        
    def _get_calendar(self, e=None):
        if self.calendar.height ==45:
            self.calendar.height = 450
            self.calendar.update()
        else:
            self.calendar.height =45
            self.calendar.update()


    def build(self):
        return Stack(
            width=320,
            controls=[
                self.calendar,
                Container(
                    on_click= lambda e: self._get_calendar(e),
                    width=320,
                    height=45,
                    border_radius=8,
                    bgcolor="#313131",
                    padding=padding.only(left=15, right=5),
                    content=Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            self.today,
                            Container(
                                width=32,
                                height=32,
                                border=border.only(
                                    left=BorderSide(0.9, "white24"),
                                ),
                                alignment=alignment.center,
                                content=Icon(
                                    name=icons.CALENDAR_MONTH_SHARP,
                                    size=15,
                                    opacity=0.65,
                                )
                            )
                        ]
                    )
                )

            ],
        )


class BTNPagination(UserControl):
    def __init__(self, text_name, function):
        self.txt_name = text_name
        self.function = function
        super().__init__()

    def build(self):
        return IconButton(
            content=Text(self.txt_name, size=8, weight="bold"),
            width=56,
            height=28,
            on_click=self.function,
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6)
                },
                bgcolor={
                    "": "teal600"
                }
            )
        )


class SchedulePage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):   
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Schedule Page")

        cal = SetCalendar()
        date = DateSetUp(cal)

        big_container = Container(
                width=400,
                height=750,
                bgcolor="white",
                border_radius=20,
                content=Column([
                    Container(
                        width=400,
                        height=100,
                        bgcolor="#3CDAB4",
                        border_radius=BorderRadius(
                        top_left=20,
                        top_right=20,
                        bottom_left=50,
                        bottom_right=50,
                        ),
                        content=Container(
                                margin=margin.only(top=30),
                                content=Text("Schedule",
                                color="BLACK",
                                size=32,
                                text_align=("CENTER"),
                                style=TextThemeStyle.TITLE_MEDIUM,
                                )
                            )
                        ),
                ])
        )  

        cal_container = Container(
            width=320,
            height=450,
            #bgcolor="grey",
            margin=margin.only(top=110, left=30),
            content=Column([
                date,
                Container(
                    width=320,
                    height=300,
                    #wbgcolor="red",
                    content=Column([
                        Container(
                            width=300,
                            height=50,
                            #bgcolor="blue",
                            content=Text("Reminder", size=32, color="BLACK",
                                         style=TextThemeStyle.TITLE_SMALL, weight="BOLD")
                        ),
                        Container(
                            width=320,
                            height=60,
                            bgcolor="#AFF7E5",
                            border_radius=30,
                            content=Column([
                                Container(
                                    width=300,
                                    #bgcolor="blue",
                                    margin=margin.only(left=20,top=5),
                                    content=Column([
                                        Text("11 Nov 2023\n0800\nAppoinment with Dr. Yuh Choong", color="black", size=12, 
                                            style=TextThemeStyle.TITLE_SMALL, weight="BOLD"),
                                        
                                            
                                    ])
                                )
                            ])
                        )
                    ]
                        
                    )
                )
            ])
        )
        exit_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=10),
                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go("/PatientHomePage/:email"))
            )

        stack = Stack([
            big_container,
            cal_container,
            exit_button_container,
        ])

        

        return View(
            "/SchedulePage",
            controls=[
                stack
            ]
        )
