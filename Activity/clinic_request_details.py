import flet 
from flet import *
from flet_route import Params, Basket
import os
from clinic import *
import firebaseHelper
from firebaseHelper import *

class ClinicRequestDetails:
     def __init__(self):
        pass
     
     def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Clinic Request Details Page"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False


        clinicD = getClinicRDictData(params.uid)
        cli = Clinic()

        try:
            cli.dict_to_clinic(clinicD)
        except TypeError:
            print("Error: clinicD is None")

        # def reject_button_on_clicked(e):
        #     firebaseHelper.deleteClinicDataByEmail(cli.email)
        #     deleteClinic(cli.email)
            
        def close_dlg(e):
            dlg_modal.open = False
            firebaseHelper.updateClinicDataByEmail(cli.email, {'status':'approved'})

            clinicLengeth = getClinicRDictDataLen()
            try:
                for i in clinicLengeth:
                    clinicD = getClinicRDictData(i)
                    cli.dict_to_clinic(clinicD)
                    if cli.status == 'approved':
                        saveClinicData(i, clinicD)
                        firebaseHelper.deleteClinicDataByEmail(cli.email)
            except:
                print("Error in update clinic")

            page.update()

        def close_reject_dlg(e):
            firebaseHelper.deleteClinicDataByEmail(cli.email)
            deleteClinic(cli.email)
            reject_dlg_modal.open = False
            page.update()

        
        dlg_modal = AlertDialog(
        modal=True,
        title=Text("Note"),
        content=Text("The status of the clinic will be 'approved' now"),
        actions=[
        TextButton("Okay", on_click=close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        reject_dlg_modal = AlertDialog(
        modal=True,
        title=Text("Note"),
        content=Text("The clinic data will be delete"),
        actions=[
        TextButton("Okay", on_click=close_reject_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        def open_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def open_reject_dlg_modal(e):
            page.dialog = reject_dlg_modal
            reject_dlg_modal.open = True
            page.update()


        cl = Column(
            spacing=10,
            height=600,
            width=400,
            scroll=ScrollMode.AUTO,
        )

        cl.controls.append(
                Container(
                    alignment=alignment.center,
                    content=Column([
                        Container(
                            content=Column([
                                Container(
                                    content=Column([
                                        Container(
                                            content=Column([
                                                Container(
                                                    content=Column([
                                                        Container(
                                                            content=Column([
                                                                    Container(
                                                                        content=Column([
                                                                                    Container(
                                                                                        content=Column([
                                                                                            Container(
                                                                                                content=Column([
                                                                                                    Container(
                                                                                                        content=Column([
                                                                                                            Container(
                                                                                                                alignment=alignment.center,
                                                                                                                content=Column([
                                                                                                                    Container(
                                                                                                                        margin=margin.symmetric(horizontal=10, vertical=5),
                                                                                                                        content=TextField(label="Clinic Name", read_only=True, value=cli.name, color="BLACK",
                                                                                                                                        multiline=True, min_lines=1, max_lines=3,)
                                                                                                                    )
                                                                                                                ])
                                                                                                            )
                                                                                                        ])
                                                                                                    ),
                                                                                                    Container(
                                                                                                        margin=margin.symmetric(horizontal=10),
                                                                                                        content=TextField(label="Clinic Address", read_only=True, value=cli.address, color="BLACK",
                                                                                                                        multiline=True, min_lines=1, max_lines=3)
                                                                                                    )
                                                                                                ])
                                                                                            ),
                                                                                            Container(
                                                                                                margin=margin.symmetric(horizontal=10),
                                                                                                content=TextField(label="Clinic State", read_only=True, value=cli.state, color="BLACK",
                                                                                                                        multiline=True, min_lines=1, max_lines=3)
                                                                                            )
                                                                                        ])
                                                                                    ),
                                                                                    Container(
                                                                                        margin=margin.symmetric(horizontal=10),
                                                                                        content=TextField(label="Clinic City", read_only=True, value=cli.city, color="BLACK",
                                                                                                                        multiline=True, min_lines=1, max_lines=3)
                                                                                    )
                                                                                ])
                                                                            ),
                                                                            Container(
                                                                                margin=margin.symmetric(horizontal=10),
                                                                                content=TextField(label="Clinic Phone Number", read_only=True, value=cli.phoneNo, color="BLACK",
                                                                                                                multiline=True, min_lines=1, max_lines=3)
                                                                                    )
                                                                        ])
                                                                    ),
                                                                    Container(
                                                                        margin=margin.symmetric(horizontal=10),
                                                                        content=TextField(label="Clinic Operation Time (Hours)", read_only=True, value=cli.operationTime, color="BLACK",
                                                                                                        multiline=True, min_lines=1, max_lines=3)
                                                                )
                                                            ])
                                                        ),
                                                        Container(
                                                            margin=margin.symmetric(horizontal=10),
                                                            content=TextField(label="Clinic Type", read_only=True, value=cli.clinicType, color="BLACK",
                                                                                            multiline=True, min_lines=1, max_lines=3)
                                                                )
                                                    ])
                                                ),
                                                Container(
                                                    margin=margin.symmetric(horizontal=10),
                                                    content=TextField(label="Clinic Service Type", read_only=True, value=cli.serviceType, color="BLACK",
                                                                                    multiline=True, min_lines=1, max_lines=3)
                                                                )
                                            ])
                                ),
                                Container(
                                    margin=margin.symmetric(horizontal=10),
                                    content=TextField(label="Clinic E-mail", read_only=True, value=cli.email, color="BLACK",
                                                                    multiline=True, min_lines=1, max_lines=3)
                                                )
                            ])
                        ),
                        Container(
                            alignment=alignment.center,
                            width=400,
                            content=Column([
                                Container(
                                width=120,
                                content=ElevatedButton("Approve", color="BLACK", bgcolor="#AFF7E5", height=50,
                                                       on_click=open_dlg_modal, data="approved")
                            ),
                            Container(
                                width=120,
                                content=ElevatedButton("Reject", color="WHITE", bgcolor="#DA3C45", height=50,
                                                       on_click=open_reject_dlg_modal)
                            ),
            
                            ])
                        )
                    ])
                ),
            
        )

        big_container=Container(
                alignment=alignment.center,
                width=400,
                height=750,
                bgcolor="white",
                border_radius=20,
                content=Column([
                    Container(
                        alignment=alignment.center,
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
                                    content=Text("Request Details",
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
                            ])
                        )
                                                                                                    
                                                                                                

        exit_button_container = Container(
                width=40,
                height=40,
                margin=margin.symmetric(vertical=35, horizontal=10),
                content=IconButton(
                                    icons.EXIT_TO_APP_ROUNDED,
                                    icon_color="BLACK",
                                    on_click=lambda _:page.go("/AdminPage"))
            )
        
        print(f"Final Status: {cli.status}")
        

        stack = Stack([big_container,
                       exit_button_container])

        

        return View(
            "/ClinicRequestDetails/:uid",
            controls=[
                stack
            ]
        )