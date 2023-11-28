import os
from flet import *
import flet as ft
from flet_route import Params, Basket
import clinic_home_page
from doctor import Doctor
import firebaseHelper
from patient import Patient
from datetime import datetime, date

class RequestDetailsPage:
    def __init__(self):
        pass


    def view(self, page:ft.Page, params:Params, basket:Basket):
        page.title = "Request Details"
        page.window_width = 400
        page.window_height = 850
        page.window_resizable = False

        #big container for the white background
        big_container = ft.Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20,
        )

        title_container = ft.Container(
            width=400,
            height=100,
            bgcolor="#3CDAB4",
            border_radius=ft.BorderRadius(
                top_left=20,
                top_right=20,
                bottom_left=50,
                bottom_right=50
            )
        )

        title_text_container = ft.Container(
            width=400,
            height=60,
            margin=margin.only(top=20),
            alignment=alignment.center,
            content=ft.Text("Request Details",
                            color="BLACK",
                            size=32,
                            text_align=("CENTER"),
                            style=ft.TextThemeStyle.TITLE_MEDIUM)
        )
        back_button_container = ft.Container(
            width=40,
            height=50,
            margin=margin.symmetric(vertical=30, horizontal=10),
            on_click=lambda _:page.go("/requestPage"),
            content=ft.Image(
                                src="./Activity/assets/images/backSharp.png",),
        )

        patientUID = params.uid
        requestDetails = firebaseHelper.getSPatientRequest(patientUID)
        patientDetails = firebaseHelper.getUserDictData(patientUID)
        self.selectedDoctor = None

        def show_error_dlg(errorMessage):
            error_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Error"),
                content=ft.Text(errorMessage),
                actions=[
                    ft.TextButton("Confirm", on_click=lambda _: close_dlg(error_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                #on_dismiss=lambda e: print("Modal dialog dismissed!"),
                open=False
            )
            page.dialog = error_dlg
            error_dlg.open = True
            page.update()

        def show_success_dlg(successMessage):
            success_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Complete"),
                content=ft.Text(successMessage),
                actions=[
                    ft.TextButton("Confirm", on_click=lambda _: close_dlg_pagego(success_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                #on_dismiss=lambda _: print("Modal dialog dismissed!"),
                open=False
            )
            page.dialog = success_dlg
            success_dlg.open = True
            page.update()

        def close_dlg(dlg_modal):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()

        def close_dlg_pagego(dlg_modal):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()
            page.go("/requestPage")

        rejectReasonTextField = ft.TextField(label="Reason:", hint_text="Reason", color="Black", border_radius=20, bgcolor='white', multiline=True, min_lines=1, max_lines=3)
        
        def show_bs(e):
            bsReason.open = True
            bsReason.update()

        def close_bs_rej(e):
            if (rejectReasonTextField.value):
                firebaseHelper.updatePatientRequestStatus(patientUID, 'Rejected')
                firebaseHelper.updatePatientRequestReason(patientUID, rejectReasonTextField.value)
                bsReason.open = False
                bsReason.update()
                show_success_dlg("The request rejected!")
            elif(rejectReasonTextField.value == '' or rejectReasonTextField.value == None):
                bsReason.open = False
                bsReason.update()
                show_error_dlg("Please input a reason")

        def closeBS(e):
            bsReason.open = False
            bsReason.update()

        bsReason = ft.BottomSheet(
            ft.Container(
                height=250,
                content= ft.Column(
                        [
                            ft.Text("Reject Confirmation", color='Black'),
                            rejectReasonTextField,
                            ft.Row([
                                ft.ElevatedButton(
                                    content=ft.Text(
                                        value='Reject',
                                        size = 20,
                                        color = 'Black'
                                    ),
                                    height=40,
                                    width=130,
                                    bgcolor='#F17C7C',
                                    on_click=close_bs_rej
                                ),
                                ft.ElevatedButton(
                                    content=ft.Text(
                                        value='Cancel',
                                        size = 20,
                                        color = 'Black'
                                    ),
                                    height = 40,
                                    width = 130,
                                    bgcolor = 'Grey',
                                    on_click=closeBS,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            )
                        ]
                    ),
                padding=10,
                bgcolor='White'
            ),
            open=False,
        )

        def appoveRequest(e):
            dateTime = dateTextField.value
            time = timeTextField.value

            if (self.selectedDoctor and dateTime and time):
                try:
                    date_obj = datetime.strptime(dateTime, '%d/%m/%Y')
                except ValueError:
                    show_error_dlg("Invalid date format. Please use dd/MM/yyyy.")
                    return
                
                 # Date not before today validation
                if date_obj.date() < date.today():
                    show_error_dlg("Invalid date. Please select a date not before today.")
                    return

                # Time format validation
                try:
                    datetime.strptime(time, '%H:%M')
                except ValueError:
                    show_error_dlg("Invalid time format. Please use 24hr HH:mm.")
                    return
                
                firebaseHelper.updatePatientRequest(patientUID, {'date': dateTime})
                firebaseHelper.updatePatientRequest(patientUID, {'time': time})
                firebaseHelper.updatePatientRequestDoctor(patientUID, self.selectedDoctor)
                firebaseHelper.updatePatientRequestStatus(patientUID, 'Approved')
                show_success_dlg("The request approved!")
            else:
                show_error_dlg("All field must be fill")
                

        doctorStatus = {}

        def getDoctors():
            doctors = []
            for i in firebaseHelper.getClinicDoctorList(clinic_home_page.clinicUID):
                doc = Doctor()
                doc.dict_to_doctor(firebaseHelper.getUserDictData(i))
                doctorStatus.update({i:doc.status})
                doctors.append(ft.dropdown.Option(key = i, text=doc.name))
            return doctors
        
        doctorList = getDoctors()
        status = ft.Container(
                                width=20,
                                height=60,
                                content=Icon(name=icons.CIRCLE_ROUNDED, color="Grey")
                            )

        def dropdown_changed(e):
            if (doctorStatus.get(e.control.value) == "Online"):
                status.content = Icon(name=icons.CIRCLE_ROUNDED, color="Green")
            elif (doctorStatus.get(e.control.value) == "Busy"):
                status.content = Icon(name=icons.CIRCLE_ROUNDED, color="Red")
            elif (doctorStatus.get(e.control.value) == "Offline"):
                status.content = Icon(name=icons.CIRCLE_ROUNDED, color="Grey")

            e.control.focus = False
            e.control.color = 'Black'
            self.selectedDoctor = e.control.value
            page.update()

        nameTextField = ft.TextField(label="Patient Name:", color="BLACK", border_radius=20, bgcolor='white', value=patientDetails.get("name"), read_only=True)
        addressTextField = ft.TextField(label="Address:", color="BLACK", border_radius=20, bgcolor='white', value=requestDetails.get("address"),multiline=True, min_lines=1, max_lines=3, read_only=True)
        phoneTextField = ft.TextField(label="Phone No:", color="BLACK", border_radius=20, bgcolor='white', value=patientDetails.get("phoneNo"), read_only=True)
        symtomsTextField = ft.TextField(label="Symptoms:", color="BLACK", border_radius=20, bgcolor='white', value=requestDetails.get("symptom"),multiline=True , min_lines=1, max_lines=3, read_only=True)
        dateTextField = ft.TextField(label="Date:", color="BLACK", border_radius=20, bgcolor='white', value=requestDetails.get("date"))
        timeTextField = ft.TextField(label="Time:", color="BLACK", border_radius=20, bgcolor='white', value=requestDetails.get("time"))
        
        patient_request_details = ft.Container(
            width=400,
            margin=margin.symmetric(vertical=110, horizontal=20),
            content=ft.Column([
                ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=10, right = 10, left=10),
                        content=nameTextField,
                    ),
                ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=5, right = 10, left=10),
                        content=addressTextField,
                    ),
                ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=5, right = 10, left=10),
                        content=phoneTextField,
                    ),
                ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=5, right = 10, left=10),
                        content=symtomsTextField,
                    ),
                ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=5, right = 10, left=10),
                        content=dateTextField,
                    ),
                ft.Container(
                         width=380,
                        height=60,
                        margin= margin.only(top=5, right = 10, left=10),
                        content=timeTextField,
                ),
                    ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=5, right = 10, left=10),
                        content=ft.Row([
                            ft.Container(
                                width=280,
                                height=60,
                                content=ft.Dropdown(
                                    width=280,
                                    label = "Assign Doctor",
                                    hint_text="Assign Doctor",
                                    options=doctorList,
                                    on_change=dropdown_changed,
                                    color='Black',
                                ), 
                            ),
                            status
                        ]
                        )
                    ),
                    ft.Container(
                        width=380,
                        height=60,
                        margin= margin.only(top=5, right = 10, left=10),
                        content=ft.Row([
                            ft.ElevatedButton(
                                content=ft.Text(
                                    value='Approve',
                                    size = 20,
                                    color = 'Black'
                                ),
                                height=40,
                                width=130,
                                bgcolor='#3CDAB4',
                                on_click=appoveRequest
                            ),
                            ft.ElevatedButton(
                                content=ft.Text(
                                    value='Reject',
                                    size = 20,
                                    color = 'Black'
                                ),
                                height = 40,
                                width = 130,
                                bgcolor = '#F17C7C',
                                on_click=show_bs,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                    )
            ], 
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        stack = ft.Stack([big_container,
                        title_container,
                        title_text_container,
                        back_button_container,
                        patient_request_details,
                        ])

        return ft.View(
            "/requestDetailsPage/:uid",
            controls=[
                stack,
                bsReason
            ]
        )
        