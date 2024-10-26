import tkinter as tk
import customtkinter as ct
from tkinter import messagebox

# Configuración del estilo
ct.set_appearance_mode("dark")  # Modo oscuro
ct.set_default_color_theme("blue")  # Tema de color

class LoginApp(ct.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Login")
        self.geometry("400x300")
        self.resizable(True, True)  # Ahora la ventana es redimensionable

        # Widgets de la Interfaz
        self.label_title = ct.CTkLabel(self, text="Login", font=("Arial", 20))
        self.label_title.pack(pady=20)

        self.username_label = ct.CTkLabel(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ct.CTkEntry(self, width=250)
        self.username_entry.pack()

        self.password_label = ct.CTkLabel(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ct.CTkEntry(self, show="*", width=250)
        self.password_entry.pack()

        self.login_button = ct.CTkButton(self, text="Login", command=self.authenticate)
        self.login_button.pack(pady=20)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Aquí se definen los datos de usuario y contraseña correctos
        if username == "admin" and password == "1234":
            messagebox.showinfo("Login Successful", "Welcome to the system!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
