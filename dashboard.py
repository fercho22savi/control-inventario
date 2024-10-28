# dashboard.py
import tkinter as tk
from modules.suppliers import SuppliersApp  # Importa SuppliersApp
from modules.clients import ClientsApp  # Importa ClientsApp

class UserActivityDashboard(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("User Activity Dashboard")
        self.geometry("800x600")

        # Botones para abrir cada módulo
        self.open_suppliers_button = tk.Button(self, text="Manage Suppliers", command=self.open_suppliers)
        self.open_suppliers_button.pack(pady=20)

        self.open_clients_button = tk.Button(self, text="Manage Clients", command=self.open_clients)
        self.open_clients_button.pack(pady=20)

    def open_suppliers(self):
        suppliers_app = SuppliersApp()  # Abre el módulo de proveedores
        suppliers_app.grab_set()  # Bloquea la ventana anterior hasta que se cierre

    def open_clients(self):
        clients_app = ClientsApp()  # Abre el módulo de clientes
        clients_app.grab_set()  # Bloquea la ventana anterior hasta que se cierre

# Para ejecutar el dashboard
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    root.withdraw()  # Ocultar la ventana principal
    dashboard = UserActivityDashboard()  # Crear el dashboard
    dashboard.mainloop()  # Ejecutar el loop
