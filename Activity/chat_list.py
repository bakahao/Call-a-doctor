import flet
from flet import *
from flet_route import Params, Basket
import os
from firebaseHelper import *


class ChatList:
    def __init__(self):
        pass

    
    def view(self, page: Page, params: Params, basket: Basket):

        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Chat List Page")

        email = params.email

        cl = Column(
                    spacing=10,
                    width=380,
                    scroll=ScrollMode.AUTO,
                )
        
        try:
            user_uid = getUserUIDByEmail(email)
            pdict = getPatientRequestDoctorDictData(user_uid)
            cdict = getClinicDictData(pdict['clinic_uid'])
            ddict = getUserDictData(pdict['doctor_uid'])

            if (pdict['status'] == "Approved"):
                doctor_name = ddict['name']

                rmd_text = Text(f"Dr. {doctor_name}", color="BLACK")
                cl.controls.append(Container(
                            content=ElevatedButton(
                                    bgcolor="#AFF7E5",
                                    on_click=lambda _:page.go(f"/PatientChatPage/{params.email}"),
                                    content=Container(
                                    width=400,
                                    content=Row([
                                         Container(
                                              content=Icon(icons.ACCOUNT_CIRCLE_OUTLINED, color="BLACK"),
                                         ),
                                        Container(
                                            content=rmd_text
                                        )
                                        
                                    ]
                                        
                                        
                                    )
                            )
                                )
                        )
                                                )
        except:
                print("Error in schedule")

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
                                content=Text("Chat",
                                color="BLACK",
                                size=32,
                                text_align=("CENTER"),
                                style=TextThemeStyle.TITLE_MEDIUM,
                                )
                            )
                        ),
                ]))
        
        chat_list_container = Column([
            Container(
                width=350,
                #bgcolor="grey",
                margin=margin.symmetric(vertical= 130, horizontal=20),
                content=Column([
                    Container(
                        width=350,
                        #height=100,
                        bgcolor="#AFF7E5",
                        border_radius=50,
                        content=cl

                    )
                ])
                
            )
        ])
        
        exit_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=10),
                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go(f"/PatientHomePage/{params.email}"))
            )
        
        stack = Stack([big_container,
                    exit_button_container,
                    chat_list_container
                    ])

        return View(
            "/ChatList/:email",
            controls=[
                stack
            ]
        )