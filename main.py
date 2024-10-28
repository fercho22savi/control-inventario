# main.py
import tkinter as tk
import customtkinter as ctk
from administrador import AdministradorUsuarios
from login import LoginApp

if __name__ == "__main__":
    admin_usuarios = AdministradorUsuarios()  # Instancia del Administrador de Usuarios
    app = LoginApp(admin_usuarios)  # Pasamos el administrador de usuarios a la app
    app.mainloop()




