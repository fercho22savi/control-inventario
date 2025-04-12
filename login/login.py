import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageDraw
import os
from modules.dashboard import Dashboard  

class LoginModerno(ctk.CTk):
    def __init__(self, master):
        self.master = master
        super().__init__()

        # Configuración de ventana
        self.title("Login")
        self.geometry("450x500")
        self.resizable(False, False)
        self.configure(bg="black")
        self.wm_attributes("-alpha", 0.85)
        self.LoginModerno = {}
        self.current_user = None # Variable para almacenar el usuario actual

        # Estilo general
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # --------- Cargar LOGO (o crear uno temporal) ---------
        logo_path = "logo.png"
        if not os.path.exists(logo_path):
            img = Image.new("RGBA", (100, 100), (30, 30, 30, 255))  # Fondo oscuro
            draw = ImageDraw.Draw(img)
            draw.text((25, 40), "LOGO", fill="white")
        else:
            img = Image.open(logo_path)

        logo_img = ctk.CTkImage(light_image=img, size=(100, 100))
        self.logo = ctk.CTkLabel(self, image=logo_img, text="")
        self.logo.pack(pady=20)

        # --------- Título ---------
        self.label_title = ctk.CTkLabel(self, text="Bienvenido", font=("Arial", 24, "bold"))
        self.label_title.pack(pady=10)

        # --------- Campo Usuario ---------
        self.username_label = ctk.CTkLabel(self, text="Usuario")
        self.username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu usuario")
        self.username_entry.pack(pady=5)

        # --------- Campo Contraseña ---------
        self.password_label = ctk.CTkLabel(self, text="Contraseña")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu contraseña", show="*")
        self.password_entry.pack(pady=5)

        # --------- Checkbox Recordar ---------
        self.remember_var = tk.BooleanVar()
        self.remember_check = ctk.CTkCheckBox(self, text="Recordar contraseña", variable=self.remember_var)
        self.remember_check.pack(pady=10)

        # --------- Botón Ingresar ---------
        self.login_button = ctk.CTkButton(self, text="Ingresar", command=self.login)
        self.login_button.pack(pady=10)

        # --------- Botón Registrarse ---------
        self.register_button = ctk.CTkButton(self, text="Registrarse", command=self.registrarse)
        self.register_button.pack(pady=5)

    # --------- Lógica de ingreso con validaciones ---------
    def login(self):
        usuario = self.username_entry.get().strip()
        contrasena = self.password_entry.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
            return

        # validación de usuario y contraseña
        if usuario == "admin" and contrasena == "admin":
            messagebox.showinfo("Login Exitoso", f"¡Bienvenido {usuario}!")
            self.current_user = usuario
            if self.remember_var.get():
                print(f"Recordar credenciales para: {usuario}")
            self.to_dashboard()  # Cambiar a la función to_dashboard
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def registrarse(self):
        messagebox.showinfo("Registro", "Aquí se abriría la ventana de registro.")
    

    def to_dashboard(self):
        self.destroy()
        self.master.deiconify()


# --------- Ejecución directa ---------
if __name__ == "__main__":
    app = LoginModerno()
    app.mainloop()
