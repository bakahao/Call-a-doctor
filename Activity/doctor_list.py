import flet
from flet import *
from flet_route import Params, Basket
import os
from clinic import Clinic
from patient import Patient
from firebaseHelper import *

class DoctorDetails:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
            page.window_width=400
            page.window_height=850
            page.window_resizable = False
            page.title=("Doctor Details Page")

            clinicD = getClinicDictData(params.uid)
            cli = Clinic()

            try:
                cli.dict_to_clinic(clinicD)
            except TypeError:
                print("Error: clinicD is None in ClinicDetails")
            
            clinic_uid = params.uid
            user_email = params.email

            doctorListLen = getClinicDoctorDataLenByUID(clinic_uid)
            

            cl = Column(
                spacing=10,
                height=500,
                width=380,
                scroll=ScrollMode.ALWAYS,
            )
            try:
                for i in doctorListLen:
                    try:
                        doctor_uid = getClinicDoctorListUID[i]
                    except:
                        print("doctor_uid get error")

                    cl.controls.append(Container(
                                margin=margin.symmetric(horizontal=10),
                                border_radius=20,
                                bgcolor="#AFF7E5",
                                content=Row([
                                    Container(
                                        width=100,
                                        height=150,
                                        content=Image(src=(os.getcwd()+"/Activity/assets/images/doctor.png"))
                                    ),
                                    Container(
                                        margin=margin.symmetric(vertical=10),
                                        content=Column([
                                            Container(
                                                content=Column([
                                                    Container(
                                                        content=Row([
                                                            Container(
                                                                content=Text("Name : ", color="BLACK", size=14, style=TextThemeStyle.TITLE_SMALL)
                                                            ),
                                                            Container(
                                                                content=Text(getUserDictData(i)['name'], data=i, color="BLACK", size=14, style=TextThemeStyle.TITLE_SMALL)
                                                            )
                                                        ])
                                                    ),
                                                    Container(
                                                        content=Row([
                                                            Container(
                                                                content=Text("Department : ", color="BLACK", size=14, style=TextThemeStyle.TITLE_SMALL)
                                                            ),
                                                            Container(
                                                                content=Text(getUserDictData(i)['department'], data=i, color="BLACK", size=14, style=TextThemeStyle.TITLE_SMALL,width=130)
                                                            )
                                                        ])
                                                    )
                                                ])
                                            ),
                                            Container(
                                                content=Row([
                                                            Container(
                                                                content=Text("Length of Service (years) : ", color="BLACK", size=14, style=TextThemeStyle.TITLE_SMALL)
                                                            ),
                                                            Container(
                                                                content=Text(getUserDictData(i)['lenOfSvc'], data=i, color="BLACK", size=14, style=TextThemeStyle.TITLE_SMALL)
                                                            )
                                                        ])
                                            )
                                        ])
                                    )
                                ]
                                    
                                )
                                                
                        ))
            except:
                print("No doctor assign in current clinic")
                    
                 

            

        
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
                                    content=Text("Details",
                                    color="BLACK",
                                    size=32,
                                    text_align=("CENTER"),
                                    style=TextThemeStyle.TITLE_MEDIUM,
                                    )
                                )
                            ),
                            Container(
                                content=cl
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
                                        on_click=lambda _:page.go(f"/ClinicDetails/{clinic_uid}/{user_email}")
                                        )
                )
            
            

            stack = Stack([
                        big_container,
                        exit_button_container,
                        ])
            
            return View(
                "/DoctorDetails/:uid/:email",
                controls=[
                    stack
                ]
            )