import tkinter as tk
import customtkinter as ct
from tkinter import messagebox

class RegistroApp(ct.CTk):
    def __init__(self, admin_usuarios):
        super().__init__()
        self.admin_usuarios = admin_usuarios

        # Configuración de estilo global
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        # Configuración de la ventana
        self.title("Registro de Usuario")
        self.geometry("400x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000")  # Fondo negro

        self.attributes("-alpha", 0.85)  # Aplicar transparencia del 85%

        fuente = ("Arial", 14)

        # Título
        self.label_title = ct.CTkLabel(self, text="Crear Cuenta", font=("Arial", 22, "bold"), text_color="#2A9D8F")
        self.label_title.pack(pady=20)

        # Campo: Usuario
        self.username_label = ct.CTkLabel(self, text="Usuario:", font=fuente)
        self.username_label.pack(pady=(10, 2))
        self.username_entry = ct.CTkEntry(self, width=250, font=fuente, placeholder_text="Ingrese su usuario")
        self.username_entry.pack()

        # Campo: Contraseña
        self.password_label = ct.CTkLabel(self, text="Contraseña:", font=fuente)
        self.password_label.pack(pady=(10, 2))
        self.password_entry = ct.CTkEntry(self, show="*", width=250, font=fuente, placeholder_text="Ingrese su contraseña")
        self.password_entry.pack()

        # Campo: Confirmar Contraseña
        self.confirm_password_label = ct.CTkLabel(self, text="Confirmar Contraseña:", font=fuente)
        self.confirm_password_label.pack(pady=(10, 2))
        self.confirm_password_entry = ct.CTkEntry(self, show="*", width=250, font=fuente, placeholder_text="Repita la contraseña")
        self.confirm_password_entry.pack()

        # Botón Registrar
        self.register_button = ct.CTkButton(self, text="Registrar", font=fuente,
                                            fg_color="#2A9D8F", hover_color="#21867A", command=self.register_user)
        self.register_button.pack(pady=25)

    def register_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        if password != confirm_password:
            messagebox.showerror("Registro fallido", "Las contraseñas no coinciden.")
            return

        if self.admin_usuarios.registrar_usuario(username, password):
            messagebox.showinfo("Éxito", "¡Usuario registrado correctamente!")
            self.destroy()
        else:
            messagebox.showerror("Registro fallido", "¡El nombre de usuario ya existe!")

# Ejecución de prueba
if __name__ == "__main__":
    class DummyAdminUsuarios:
        def registrar_usuario(self, username, password):
            print(f"Usuario '{username}' registrado con éxito.")
            return True

    app = RegistroApp(admin_usuarios=DummyAdminUsuarios())
    app.mainloop()
