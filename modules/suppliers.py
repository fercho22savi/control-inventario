# suppliers.py
import tkinter as tk
from tkinter import messagebox, ttk

class SuppliersApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Módulo de Proveedores")
        self.geometry("600x400")
        
        self.suppliers = {}  # Almacenar proveedores en un diccionario {id: datos}
        self.current_id = None  # Para rastrear el id del proveedor actual que se está editando

        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        # Frame para el formulario
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="ID:").grid(row=0, column=0)
        self.id_entry = tk.Entry(form_frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Nombre:").grid(row=1, column=0)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Teléfono:").grid(row=2, column=0)
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=2, column=1)

        # Botones
        tk.Button(form_frame, text="Agregar", command=self.add_supplier).grid(row=3, column=0)
        tk.Button(form_frame, text="Actualizar", command=self.update_supplier).grid(row=3, column=1)
        tk.Button(form_frame, text="Eliminar", command=self.delete_supplier).grid(row=3, column=2)

        # Tabla para mostrar proveedores
        self.suppliers_table = ttk.Treeview(self, columns=("ID", "Nombre", "Teléfono"), show='headings')
        self.suppliers_table.heading("ID", text="ID")
        self.suppliers_table.heading("Nombre", text="Nombre")
        self.suppliers_table.heading("Teléfono", text="Teléfono")
        self.suppliers_table.pack(pady=20)

        self.suppliers_table.bind("<Double-1>", self.on_item_selected)

    def populate_table(self):
        # Limpiar la tabla
        for row in self.suppliers_table.get_children():
            self.suppliers_table.delete(row)

        # Llenar la tabla con proveedores
        for supplier_id, data in self.suppliers.items():
            self.suppliers_table.insert("", "end", values=(supplier_id, data["name"], data["phone"]))

    def add_supplier(self):
        supplier_id = self.id_entry.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if supplier_id in self.suppliers:
            messagebox.showerror("Error", "El ID ya existe.")
            return

        self.suppliers[supplier_id] = {"name": name, "phone": phone}
        self.populate_table()
        self.clear_entries()

    def update_supplier(self):
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un proveedor para actualizar.")
            return

        name = self.name_entry.get()
        phone = self.phone_entry.get()

        self.suppliers[self.current_id] = {"name": name, "phone": phone}
        self.populate_table()
        self.clear_entries()

    def delete_supplier(self):
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un proveedor para eliminar.")
            return

        del self.suppliers[self.current_id]
        self.populate_table()
        self.clear_entries()

    def on_item_selected(self, event):
        selected_item = self.suppliers_table.selection()[0]
        item_data = self.suppliers_table.item(selected_item, "values")
        self.current_id = item_data[0]

        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, self.current_id)
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, item_data[1])
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, item_data[2])

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.current_id = None

# Código para ejecutar el módulo directamente (opcional)
if __name__ == "__main__":
    app = SuppliersApp()
    app.mainloop()
