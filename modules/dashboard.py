# -*- coding: utf-8 -*-
# Este módulo es parte de un sistema de gestión de clientes y proveedores.
# Su propósito es proporcionar un panel de control para acceder a diferentes módulos de la aplicación.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ct
from clients import ClientsApp
from modules.suppliers import SuppliersApp
from modules.products import ProductApp


class Dashboard(ct.CTk):# Clase principal del Dashboard
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x500")
        self.resizable(False, False)
        self.configure(fg_color="black")
        self.wm_attributes("-alpha", 0.95)

        ct.CTkLabel(self, text="MODULOS", font=("Helvetica", 22, "bold"), text_color="white").pack(pady=40)

        ct.CTkButton(self,
                     text="Módulo Proveedores",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#2A9D8F",
                     hover_color="#21867A",
                     text_color="white",
                     command=self.open_suppliers_module).pack(pady=20)

        ct.CTkButton(self,
                     text="Módulo Clientes",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#2A9D8F",
                     hover_color="#21867A",
                     text_color="white",
                     command=self.open_clients_module).pack(pady=20)

        ct.CTkButton(self,
                     text="Módulo Productos",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#2A9D8F",
                     hover_color="#21867A",
                     text_color="white",
                     command=self.open_products_module).pack(pady=20)

        ct.CTkButton(self,
                     text="Salir",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#E76F51",
                     hover_color="#D35445",
                     text_color="white",
                     command=self.quit).pack(pady=10)

    def open_suppliers_module(self):# Método para abrir el módulo de proveedores
        print("Abriendo módulo de proveedores...")
        self.withdraw()
        app = SuppliersApp(self)
        app.mainloop()
        self.deiconify()

    def open_clients_module(self):# Método para abrir el módulo de clientes
        print("Abriendo módulo de clientes...")
        self.withdraw()
        app = ClientsApp(self)
        app.mainloop()
        self.deiconify()

    def open_products_module(self):# Método para abrir el módulo de productos
        print("Abriendo módulo de productos...")
        self.withdraw()
        app = ProductApp(self)
        app.mainloop()
        self.deiconify()

    def back_to_dashboard(self):# Método para regresar al dashboard
        print("Regresando al Dashboard...")
        self.destroy()
        dashboard = Dashboard()
        dashboard.mainloop()


if __name__ == "__main__":
    print("Iniciando Dashboard...")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")
    dashboard = Dashboard()
    dashboard.mainloop()
