import flet
from flet import *
from flet_route import Params, Basket
import os
import firebaseHelper
from patient import Patient
from prescriptions import Prescriptions

class Prescription:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.window_width=400
        page.window_height=850
        page.window_resizable = False
        page.title=("Prescription Page")

        uid = params.uid
        patientUID = params.patientUID

        def open_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def close_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = False
            page.update()


        dlg_modal = AlertDialog(
            modal = True,
            title=Text("Field can't be blank"),
            content=Text("PLease fill in the blank"),
            actions=[
                TextButton("close", on_click=close_dlg_modal),
                
        ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        
        def add_prescription_button_onClick(e):
            if (not patient_gender.value or not symptoms.value or not prescription.value):
                open_dlg_modal(e)
                print("Please fill in all the blanks")
            else:
                prescriptions = Prescriptions(patient_name.value, doctorUID.value, patient_email.value, patient_phone.value, patient_gender.value, symptoms.value, prescription.value, dates.value)
        
                jsonPrescription = prescriptions.prescription_to_dict()
                firebaseHelper.savePrescriptionData(patientUID, jsonPrescription)
        
        firebaseHelper.getUserDictData(patientUID)
        patient = Patient()
        patient.dict_to_patient(firebaseHelper.getUserDictData(patientUID))  
        date = firebaseHelper.getPatientRequestDoctorDictData(patientUID).get('date')

        patient_name = TextField(label="Patient Name", value=patient.name, read_only=True, bgcolor="white", color="black")
        doctorUID = TextField(value=uid)
        dates= TextField(value=date)
        patient_email = TextField(label="Patient Email",value=patient.email, read_only=True, bgcolor="white", color="black")
        patient_phone = TextField(label="Patient Phone", value=patient.phoneNo, read_only=True, bgcolor="white", color="black")
        patient_gender = Dropdown(
                        color="grey",
                        label="Gender",
                        options=[
                            dropdown.Option("Male"),
                            dropdown.Option("Female")
                            ])
        symptoms = TextField(label="Symtomps", bgcolor="white", color="black")
        prescription = TextField(label="Enter Presecription", bgcolor="white", color="black")
        addButton = ElevatedButton("Add Prescription", bgcolor="#3CDAB4", color="black", on_click=add_prescription_button_onClick)

        

        prescription_container = Container(
            width=350,
            top=110,
            left =20,
            right =20,
            content=Column([
                Container(
                    alignment= alignment.center,
                    content = patient_name,
                ),
                Container(
                    alignment= alignment.center,
                    content = patient_email,
                ),
                Container(
                    alignment= alignment.center,
                    content = patient_phone,
                ),
                Container(
                    alignment= alignment.center,
                    content = patient_gender,
                ),
                Container(
                    alignment= alignment.center,
                    content = symptoms,
                ),
                Container(
                    alignment= alignment.center,
                    content = prescription,
                ),
                Container(
                    alignment= alignment.center,
                    content = addButton,
                )

            ],
            spacing =10
            )
        )

        for patientUID, request_details in firebaseHelper.getPatientRequestDoctor(uid).items():
            print(f"Patient UID: {patientUID}")
            print("Request Details:")
            print("  Clinic UID:", request_details.get("clinic_uid"))
            print("  User Email:", request_details.get("user_email"))

        #big container for the white background
        big_container = Container(
            width=400,
            height=750,
            bgcolor="white",
            border_radius=20
        )

        title_container = Container(
            width=400,
            height=100,
            bgcolor="#3CDAB4",
            border_radius=BorderRadius(
                top_left=20,
                top_right=20,
                bottom_left=50,
                bottom_right=50
            )
        )

        title_text_container = Container(
            #width=150,
            #height=60,
            margin=margin.symmetric(horizontal=130, vertical=35),
            content=Text("Add Prescription",
                            color="BLACK",
                            size=16,
                            text_align=("CENTER"),
                            style=TextThemeStyle.TITLE_MEDIUM)
        )
        
        
        exit_button_container = Container(
                        width=40,
                        height=40,
                        margin=margin.symmetric(vertical=35, horizontal=10),
                        content=IconButton(
                                            icons.EXIT_TO_APP_ROUNDED,
                                            icon_color="BLACK",
                                            on_click=lambda _:page.go(f"/MedicalReportPage/{uid}")
                                            )
                    )

        stack = Stack([big_container,
                    title_container,
                    title_text_container,
                    prescription_container,
                    exit_button_container,
                    dlg_modal
                    
                            
                            
        ])
        
        
        return View(
            "/PrescriptionPage/:uid/:patientUID",
            controls=[
            stack
    
        ]
        )