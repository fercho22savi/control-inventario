# login.py
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from registro import RegistroApp
from dashboard import UserActivityDashboard

class LoginApp(ctk.CTk):
    def __init__(self, admin_usuarios):
        super().__init__()
        self.admin_usuarios = admin_usuarios

        # Configuración de la ventana principal
        self.title("Login")
        self.geometry("400x300")
        self.resizable(True, True)

        # Widgets de la Interfaz
        self.label_title = ctk.CTkLabel(self, text="Login", font=("Arial", 20))
        self.label_title.pack(pady=20)

        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self, width=250)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*", width=250)
        self.password_entry.pack()

        self.login_button = ctk.CTkButton(self, text="Login", command=self.authenticate)
        self.login_button.pack(pady=10)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.open_registration)
        self.register_button.pack(pady=5)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        authentication_result = self.admin_usuarios.autenticar_usuario(username, password)
        
        if authentication_result is None:
            messagebox.showerror("User Not Found", "The user is not registered.")
        elif authentication_result:
            if username == "admin":  # Si el usuario es admin
                self.open_dashboard()  # Abre el dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid password")

    def open_registration(self):
        # Abre la ventana de registro
        registro_app = RegistroApp(self.admin_usuarios)
        registro_app.mainloop()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Bienvenido. Ingrese sus credenciales.")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Ingresar", command=self.open_dashboard)
        self.button.pack(pady=20)

    def open_dashboard(self):
        # Cierra la ventana de login
        self.destroy()  # Cierra la ventana de login
        # Crea y abre una nueva instancia de UserActivityDashboard
        dashboard_app = UserActivityDashboard()
        dashboard_app.mainloop()
