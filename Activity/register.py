import tkinter as tk
from PIL import Image, ImageTk

class RegisterPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Register Page")
        self.geometry("428x926")
        self.setup_window()

    def setup_window(self):
        self.create_canvas()
        self.create_logo()
        self.create_entry_widgets()
        self.create_signup_button()

    def create_canvas(self):
        self.canvas = tk.Canvas(self, bg="white", width=428, height=926)
        self.canvas.pack()

    def create_logo(self):
        logo_image = Image.open("Call-a-doctor/Activity/assets/images/logo.png")
        logo_image = logo_image.resize((100, 100))
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        self.logo_photo_label = tk.Label(self.canvas, image=self.logo_photo, bg="white")
        self.logo_photo_label.place(x=428 / 2, y=926 / 5, anchor="center")

    def create_entry_widgets(self):
        entry_data = [
            ("Enter Full Name", 115),
            ("Enter E-mail", 150),
            ("Enter your phone number", 185),
            ("Enter password", 220)
        ]
        
        for placeholder, y in entry_data:
            entry = self.create_entry(self.canvas, placeholder, y)

    def create_entry(self, canvas, placeholder, y):
        entry = tk.Entry(canvas, font=("Poppins", 14), highlightbackground="#3CDAB4", bd=0, highlightthickness=2, bg="white", fg="gray", justify="center")
        entry.placeholder = placeholder  # Set a placeholder attribute
        entry.insert(0, placeholder)
        entry.place(x=428 / 2, y=926 / 5 + y, anchor="center")
        entry.bind("<FocusIn>", self.clear_placeholder)
        entry.bind("<FocusOut>", self.restore_placeholder)
        return entry

    def clear_placeholder(self, event):
        widget = event.widget
        if widget.get() == widget.placeholder:
            widget.delete(0, tk.END)
            widget.config(fg="black")

    def restore_placeholder(self, event):
        widget = event.widget
        if widget.get() == "":
            widget.delete(0, tk.END)
            widget.insert(0, widget.placeholder)
            widget.config(fg="gray")

    def create_signup_button(self):
        self.signup_button = tk.Button(self.canvas, text="Sign Up", command=self.signup, bg="#3CDAB4", fg="black", width=20)
        self.signup_button.place(x=428 / 2, y=926 / 5 + 260, anchor="center")

    def signup(self):
        # Implement your signup logic here
        print("Sign Up button clicked")

if __name__ == "__main__":
    app = RegisterPage()
    app.mainloop()
