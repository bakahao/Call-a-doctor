import tkinter as tk
from PIL import Image, ImageTk
from register import RegisterPage

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("428x926")
        self.setup_window()

    def setup_window(self):
        self.create_canvas()
        self.create_logo()
        self.create_welcome_text()
        self.create_email_entry()
        self.create_password_entry()
        self.create_password_toggle()
        self.create_login_button()
        self.create_register_button()

    def create_canvas(self):
        self.canvas = tk.Canvas(self, bg="white", width=428, height=926)
        self.canvas.pack()

    def create_logo(self):
        logo_image = Image.open("Call-a-doctor/Activity/assets/images/logo.png")
        logo_image = logo_image.resize((100, 100))
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        self.logo_photo_label = tk.Label(self.canvas, image=self.logo_photo, bg="white")
        self.logo_photo_label.place(x=428 / 2, y=926 / 5, anchor="center")

    def create_welcome_text(self):
        welcome_text_content = "Welcome to Call a Doctor!"
        welcome_text_color = "black"
        welcome_text_weight = "bold"
        welcome_text_size = 20
        
        self.welcome_text = tk.Label(self.canvas, text=welcome_text_content, bg="white", fg=welcome_text_color,
                                     font=("Poppins", welcome_text_size, welcome_text_weight))
        self.welcome_text.place(x=428 / 2, y=926 / 5 + 80, anchor="center")

    def create_email_entry(self):
        email_placeholder = "Enter E-mail"
        self.email_entry = tk.Entry(self.canvas, font=("Poppins", 14), highlightbackground="#3CDAB4", bd=0,
                                    highlightthickness=2, bg="white", fg="gray", justify="center")
        self.email_entry.insert(0, email_placeholder)
        self.email_entry.place(x=428 / 2, y=926 / 5 + 115, anchor="center")
        self.email_entry.bind("<FocusIn>", self.clear_email_placeholder)
        self.email_entry.bind("<FocusOut>", self.restore_email_placeholder)

    def create_password_entry(self):
        password_placeholder = "Enter Password"
        self.password_entry = tk.Entry(self.canvas, font=("Poppins", 14), highlightbackground="#3CDAB4", bd=0,
                                    highlightthickness=2, bg="white", fg="gray", justify="center", show="*")
        self.password_entry.insert(0, password_placeholder)
        self.password_entry.place(x=428 / 2, y=926 / 5 + 150, anchor="center")
        self.password_entry.bind("<FocusIn>", self.clear_password_placeholder)
        self.password_entry.bind("<FocusOut>", self.restore_password_placeholder)

    def create_password_toggle(self):
        self.show_password = tk.BooleanVar()
        self.show_password.set(False)
        self.password_toggle = tk.Checkbutton(self.canvas, text="Show Password", variable=self.show_password,
                                             command=self.toggle_password_visibility, bg="white")
        self.password_toggle.place(x=428 / 2, y=926 / 5 + 180, anchor="center")

    def create_login_button(self):
        self.login_button = tk.Button(self.canvas, text="Login", command=self.login, bg="#3CDAB4", fg="black", width=20)
        self.login_button.place(x=428 / 2, y=926 / 5 + 220, anchor="center")

    def create_register_button(self):
        self.register_button = tk.Button(self.canvas, text="Register", command=self.register, bg="#f36c6c", fg="white",
                                        width=20)
        self.register_button.place(x=428 / 2, y=926 / 5 + 250, anchor="center")

    def clear_email_placeholder(self, event):
        if self.email_entry.get() == "Enter E-mail":
            self.email_entry.delete(0, tk.END)
            self.email_entry.config(fg="black")

    def restore_email_placeholder(self, event):
        if self.email_entry.get() == "":
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, "Enter E-mail")
            self.email_entry.config(fg="gray")

    def clear_password_placeholder(self, event):
        if self.password_entry.get() == "Enter Password":
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(fg="black")

    def restore_password_placeholder(self, event):
        if self.password_entry.get() == "":
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Enter Password")
            self.password_entry.config(fg="gray")

    def toggle_password_visibility(self):
        self.password_entry.config(show="" if self.show_password.get() else "*")

    def login(self):
        print("Login button clicked")
        # Implement your login logic here

    def register(self):
        print("Register button clicked")
        # Create an instance of RegisterPage and destroy the current window
        self.destroy()
        register_page = RegisterPage()
        

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
