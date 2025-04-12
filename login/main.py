# main.py
import tkinter as tk
import customtkinter as ctk

from login import LoginApp
from modules.administrador import AdministradorUsuarios

if __name__ == "__main__":
    admin_usuarios = AdministradorUsuarios()  # Instancia del Administrador de Usuarios
    app = LoginApp(admin_usuarios)  # Pasamos el administrador de usuarios a la app
    app.mainloop()




