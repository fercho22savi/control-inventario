# dashboard.py
import tkinter as tk
from modules.suppliers import SuppliersApp  # Asegúrate de que SuppliersApp esté en suppliers.py
from modules.clients import ClientsApp  # Asegúrate de que ClientsApp esté en clients.py

class UserActivityDashboard(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("User Activity Dashboard")
        self.geometry("800x600")

        # Etiqueta de título
        self.label_title = tk.Label(self, text="Dashboard de Actividades", font=("Arial", 24))
        self.label_title.pack(pady=20)

        # Botones para abrir cada módulo
        self.open_suppliers_button = tk.Button(self, text="Gestionar Proveedores", command=self.open_suppliers)
        self.open_suppliers_button.pack(pady=10)

        self.open_clients_button = tk.Button(self, text="Gestionar Clientes", command=self.open_clients)
        self.open_clients_button.pack(pady=10)

    def open_suppliers(self):
        suppliers_app = SuppliersApp()  # Abre el módulo de proveedores
        suppliers_app.grab_set()  # Bloquea la ventana anterior hasta que se cierre

    def open_clients(self):
        clients_app = ClientsApp()  # Abre el módulo de clientes
        clients_app.grab_set()  # Bloquea la ventana anterior hasta que se cierre

# Para ejecutar el dashboard (opcional)
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    root.withdraw()  # Ocultar la ventana principal
    dashboard = UserActivityDashboard()  # Crear el dashboard
    dashboard.mainloop()  # Ejecutar el loop
