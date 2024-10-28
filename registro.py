# registro.py
import tkinter as tk
import customtkinter as ct
from tkinter import messagebox

class RegistroApp(ct.CTk):
    def __init__(self, admin_usuarios):
        super().__init__()
        self.admin_usuarios = admin_usuarios

        # Configuración de la ventana de registro
        self.title("Register User")
        self.geometry("400x350")
        self.resizable(True, True)

        # Widgets de la Interfaz
        self.label_title = ct.CTkLabel(self, text="Register", font=("Arial", 20))
        self.label_title.pack(pady=20)

        # Campo de Nombre de Usuario
        self.username_label = ct.CTkLabel(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ct.CTkEntry(self, width=250)
        self.username_entry.pack()

        # Campo de Contraseña
        self.password_label = ct.CTkLabel(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ct.CTkEntry(self, show="*", width=250)
        self.password_entry.pack()

        # Campo de Confirmación de Contraseña
        self.confirm_password_label = ct.CTkLabel(self, text="Confirm Password:")
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry = ct.CTkEntry(self, show="*", width=250)
        self.confirm_password_entry.pack()

        self.register_button = ct.CTkButton(self, text="Register", command=self.register_user)
        self.register_button.pack(pady=20)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Registration Failed", "Passwords do not match.")
            return

        if self.admin_usuarios.registrar_usuario(username, password):
            messagebox.showinfo("Registration Successful", "User registered successfully!")
            self.destroy()  # Cierra la ventana de registro después de registrar
        else:
            messagebox.showerror("Registration Failed", "Username already exists!")
