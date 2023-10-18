import tkinter as tk
from login_page import LoginPage
from tkinter import font
from tkinter import PhotoImage
from PIL import Image, ImageTk

class PatientHomePage:
    def __init__(self, window):
        self.window = window
        self.setup_window()
        

    def setup_window(self):
        self.window.title("Patient Home Page")
        self.window.geometry("428x926")

        self.create_title_bar()
        self.create_canvas()

    def create_title_bar(self):
        title_bar = tk.Frame(self.window, width=428, height=100, bg="#3CDAB4")
        title_bar.pack()

        title_font = font.Font(family="Inter", size=32, weight="bold")
        title_label = tk.Label(title_bar, text="Home", font=title_font, bg="#3CDAB4")
        title_label.place(relx=0.5, rely=0.5, anchor="center")

        self.create_exit_button(title_bar)

    def create_exit_button(self, title_bar):
        image_button = PhotoImage(file="Call-a-doctor/Activity/assets/images/exit.png")
        image_button = image_button.subsample(20)
        self.image_button_label = tk.Label(title_bar, image=image_button, bg="#3CDAB4")
        self.image_button_label.place(relx=0.07, rely=0.5, anchor="center")
        self.image_button_label.bind("<Button-1>", self.exit_button_click)
        self.image_button = image_button

    def exit_button_click(self, event):
        original_image = Image.open("Call-a-doctor/Activity/assets/images/exit.png")
        original_image = original_image.resize((30, 30))
        gray_image = Image.new("L", original_image.size)
        gray_image.paste(original_image, (0, 0))
        gray_image = ImageTk.PhotoImage(gray_image)
        self.image_button_label.config(image=gray_image)
        self.window.after(200, lambda: self.image_button_label.config(image=self.image_button))

        # Close the current window
        self.window.destroy()
        # Open a new LoginPage window
        login_page = LoginPage()
        login_page.mainloop()

    def create_canvas(self):
        canvas = tk.Canvas(self.window, bg="white", width=428, height=926)
        canvas.pack()

        button_width = 185
        button_height = 185

        # Clinic List Button
        clinic_button_color = "#FFD0D0"
        clinicList_square_button = canvas.create_rectangle(50, 50, 50 + button_width, 50 + button_height, fill=clinic_button_color, outline="", width=0)

        # Import image into the square button
        clinic_image_button = Image.open("Call-a-doctor/Activity/assets/images/clinic.png")
        clinic_image_button = clinic_image_button.resize((100, 100))
        clinic_image_button = ImageTk.PhotoImage(clinic_image_button)
        clinic_image_button_label = canvas.create_image(50 + button_width / 2 , 40 + button_height / 2, image=clinic_image_button)

        # Create "Clinic List" Text
        clinic_button_text = "CLINIC LIST"
        clinic_text_color = "black"
        clinic_text_size = 20
        clinic_text_x = 50 + button_width / 2
        clinic_text_y = 110 + button_height / 2
        clinic_text = canvas.create_text(clinic_text_x, clinic_text_y, text=clinic_button_text, fill=clinic_text_color, font=("Alegreya Sans", clinic_text_size))

        # Move the position of image_button_label, clinicList_square_button, and clinic_text
        canvas.move(clinic_image_button_label, -35, 0)
        canvas.move(clinicList_square_button, -35, 0)
        canvas.move(clinic_text, -35, 0)

        # Feedback Button
        feedback_button_color = "#C5F6BD"
        feedback_square_button = canvas.create_rectangle(50, 50, 50 + button_width, 50 + button_height, fill=feedback_button_color, outline="", width=0)

        # Import image into the square button
        feedback_image_button = Image.open("Call-a-doctor/Activity/assets/images/review.png")
        feedback_image_button = feedback_image_button.resize((100, 100))
        feedback_image_button = ImageTk.PhotoImage(feedback_image_button)
        feedback_image_button_label = canvas.create_image(50 + button_width / 2 , 40 + button_height / 2, image=feedback_image_button)

        # Create "Feedback" Text
        feedback_button_text = "FEEDBACK"
        feedback_text_color = "black"
        feedback_text_size = 20
        feedback_text_x = 50 + button_width / 2
        feedback_text_y = 110 + button_height / 2
        feedback_text = canvas.create_text(feedback_text_x, feedback_text_y, text=feedback_button_text, fill=feedback_text_color, font=("Alegreya Sans", feedback_text_size))

        # Move the position of feedback_square_button
        canvas.move(feedback_text, 175, 0)
        canvas.move(feedback_image_button_label, 175, 0)
        canvas.move(feedback_square_button, 175, 0)

        # Chat Button
        chat_button_color = "#B9F5FD"
        chat_square_button = canvas.create_rectangle(50, 50, 50 + button_width, 50 + button_height, fill=chat_button_color, outline="", width=0)

        # Import image into the square button
        chat_image_button = Image.open("Call-a-doctor/Activity/assets/images/chat.png")
        chat_image_button = chat_image_button.resize((100, 100))
        chat_image_button = ImageTk.PhotoImage(chat_image_button)
        chat_image_button_label = canvas.create_image(50 + button_width / 2 , 40 + button_height / 2, image=chat_image_button)

        # Create "Chat" Text
        chat_button_text = "CHAT"
        chat_text_color = "black"
        chat_text_size = 20
        chat_text_x = 50 + button_width / 2
        chat_text_y = 110 + button_height / 2
        chat_text = canvas.create_text(chat_text_x, chat_text_y, text=chat_button_text, fill=chat_text_color, font=("Alegreya Sans", chat_text_size))

        # Move chat_square_button, chat_image_button_label, and chat_text
        canvas.move(chat_text, -35, 210)
        canvas.move(chat_image_button_label, -35, 210)
        canvas.move(chat_square_button, -35, 210)

        # Schedule Button
        schedule_button_color = "#BCCCE4"
        schedule_square_button = canvas.create_rectangle(50, 50, 50 + button_width, 50 + button_height, fill=schedule_button_color, outline="", width=0)

        # Import image into the square button
        schedule_image_button = Image.open("Call-a-doctor/Activity/assets/images/schedule.png")
        schedule_image_button = schedule_image_button.resize((100, 100))
        schedule_image_button = ImageTk.PhotoImage(schedule_image_button)
        schedule_image_button_label = canvas.create_image(50 + button_width / 2 , 40 + button_height / 2, image=schedule_image_button)

        # Create "Schedule" Text
        schedule_button_text = "SCHEDULE"
        schedule_text_color = "black"
        schedule_text_size = 20
        schedule_text_x = 50 + button_width / 2
        schedule_text_y = 110 + button_height / 2
        schedule_text = canvas.create_text(schedule_text_x, schedule_text_y, text=schedule_button_text, fill=schedule_text_color, font=("Alegreya Sans", schedule_text_size))

        # Move schedule_square_button, schedule_image_button_label, and schedule_text
        canvas.move(schedule_text, 175, 210)
        canvas.move(schedule_image_button_label, 175, 210)
        canvas.move(schedule_square_button, 175, 210)

if __name__ == "__main__":
    window = tk.Tk()
    app = PatientHomePage(window)
    window.mainloop()
