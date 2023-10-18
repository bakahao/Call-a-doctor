import tkinter as tk
from tkinter import font
from tkinter import PhotoImage
from PIL import Image, ImageTk
from patient_home import PatientHomePage

class ClinicList:
    def __init__(self, window):
        self.window = window
        self.setup_window()

    def setup_window(self):
        self.window.title("Clinic List Page")
        self.window.geometry("428x926")

        self.create_title_bar()
        self.create_canvas()

    def create_title_bar(self):
        title_bar = tk.Frame(self.window, width=428, height=100, bg="#3CDAB4")
        title_bar.pack()

        title_font = font.Font(family="Inter", size=32, weight="bold")
        title_label = tk.Label(title_bar, text="Clinic List", font=title_font, bg="#3CDAB4")
        title_label.place(relx=0.5, rely=0.5, anchor="center")

        self.create_return_button(title_bar)
        

    def create_canvas(self):
        canvas = tk.Canvas(self.window, bg="white", width=428, height=926)
        canvas.pack()

    def create_return_button(self, title_bar):
        image_button = PhotoImage(file="Call-a-doctor/Activity/assets/images/back.png")
        image_button = image_button.subsample(20)
        self.return_button_label = tk.Label(title_bar, image=image_button, bg="#3CDAB4")
        self.return_button_label.place(relx=0.07, rely=0.5, anchor="center")
        self.return_button_label.bind("<Button-1>", self.return_button_click)
        self.return_button = image_button

    def return_button_click(self, event):
        original_image = Image.open("Call-a-doctor/Activity/assets/images/back.png")
        original_image = original_image.resize((30, 30))
        gray_image = Image.new("L", original_image.size)
        gray_image.paste(original_image, (0, 0))
        gray_image = ImageTk.PhotoImage(gray_image)
        self.return_button_label.config(image=gray_image)
        self.window.after(200, lambda: self.return_button_label.config(image=self.return_button))

        # 关闭当前窗口
        self.window.destroy()
        # 打开一个新的登录页面
        self.open_patient_page()
    
    def open_patient_page(self):
        window = tk.Tk()
        patient_page = PatientHomePage(window)
        window.mainloop()

    
if __name__ == "__main__":
    window = tk.Tk()
    app = ClinicList(window)
    window.mainloop()
