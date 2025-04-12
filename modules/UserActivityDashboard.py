import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import os
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UserActivityDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Estética principal (idéntica a login)
        self.title("Panel de Actividad del Usuario")
        self.geometry("800x600")
        self.configure(bg="black")
        self.wm_attributes("-alpha", 0.85)  # Misma transparencia

        # Título
        self.label = ctk.CTkLabel(self, text="Dashboard de Actividad de Usuario", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Área de texto
        self.text_area = ctk.CTkTextbox(self, width=750, height=200)
        self.text_area.pack(pady=10)

        # Botón actualizar
        self.refresh_button = ctk.CTkButton(self, text="Actualizar Datos", command=self.actualizar_dashboard)
        self.refresh_button.pack(pady=10)

        # Frame para gráfico
        self.graph_frame = ctk.CTkFrame(self, width=750, height=250, fg_color="black")  # Fondo negro uniforme
        self.graph_frame.pack(pady=10)

        self.actualizar_dashboard()

        
    def actualizar_dashboard(self):
        self.cargar_actividades()
        self.mostrar_grafico()

    def cargar_actividades(self):
        self.text_area.delete("1.0", tk.END)
        if not os.path.exists("actividad.log"):
            self.text_area.insert(tk.END, "No hay actividad registrada aún.")
            return

        with open("actividad.log", "r", encoding="utf-8") as file:
            lineas = file.readlines()
            if not lineas:
                self.text_area.insert(tk.END, "El archivo de actividad está vacío.")
            else:
                for linea in lineas[-30:]:
                    self.text_area.insert(tk.END, linea)

    def mostrar_grafico(self):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        if not os.path.exists("actividad.log"):
            return

        acciones = []
        with open("actividad.log", "r", encoding="utf-8") as file:
            for linea in file:
                if ": " in linea:
                    partes = linea.strip().split(": ")
                    if len(partes) == 2:
                        accion = partes[1]
                        acciones.append(accion)

        conteo = Counter(acciones)
        if not conteo:
            return

        # Gráfico con fondo oscuro 
        fig, ax = plt.subplots(figsize=(7, 3))
        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")

        ax.bar(conteo.keys(), conteo.values(), color='deepskyblue')
        ax.set_title("Frecuencia de Actividades", color="white")
        ax.set_ylabel("Cantidad", color="white")
        ax.tick_params(axis='x', labelrotation=45, colors="white")
        ax.tick_params(axis='y', colors="white")
        for spine in ax.spines.values():
            spine.set_color("white")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Función global para registrar actividad
def registrar_actividad(usuario, accion):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("actividad.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {usuario}: {accion}\n")

# Solo para pruebas individuales
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = UserActivityDashboard()
    app.mainloop()
    app.destroy()
