# -*- coding: utf-8 -*-
# Este módulo es parte de un sistema de gestión de clientes y proveedores.
# Su propósito es permitir la gestión de datos de clientes, incluyendo la adición, actualización y eliminación de registros.
import customtkinter as ct
from tkinter import messagebox
from tkinter import ttk


ct.set_appearance_mode("dark")# Configuración del modo de apariencia
ct.set_default_color_theme("dark-blue")# Configuración del tema de color por defecto

class ClientsApp(ct.CTkToplevel):# Clase para el módulo de clientes
    def __init__(self,master):
        self.master = master
        super().__init__()
        self.title("Módulo de Clientes")
        self.geometry("900x600")
        self.clients = {}
        self.current_id = None

        title_label = ct.CTkLabel(self, text="Clientes", font=ct.CTkFont(size=28, weight="bold"))
        title_label.pack(padx=20, pady=(20, 5), anchor="w")

        # Frame de formulario clientes
        form_frame = ct.CTkFrame(self, fg_color="transparent")
        form_frame.pack(pady=10, padx=10, fill="x")

        form_frame.grid_columnconfigure((0, 1, 2), weight=0)# Configuración de columnas del frame

        self.id_entry = self._add_entry(form_frame, "ID:", 0, 0)
        self.name_entry = self._add_entry(form_frame, "Nombre:", 0, 2)
        self.phone_entry = self._add_entry(form_frame, "Teléfono:", 1, 0)
        self.email_entry = self._add_entry(form_frame, "Email:", 1, 2)
        self.product_entry = self._add_entry(form_frame, "Producto:", 2, 0)
        self.quantity_entry = self._add_entry(form_frame, "Cantidad:", 2, 2)

    

        # Botones
        button_frame = ct.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)
        ct.CTkButton(button_frame, text="Agregar", width=140, command=self.add_client).grid(row=0, column=0, padx=5)
        ct.CTkButton(button_frame, text="Actualizar", width=140, command=self.update_client).grid(row=0, column=1, padx=5)
        ct.CTkButton(button_frame, text="Eliminar", width=140, command=self.delete_client).grid(row=0, column=2, padx=5)
        ct.CTkButton(button_frame, text="Limpiar", width=140, command=self.clear_entries).grid(row=0, column=3, padx=5)
        ct.CTkButton(button_frame, text="Regresar", width=140, command=self.back_to_dashboard).grid(row=0, column=4, padx=5)

        # Tabla
        self.clients_table = ttk.Treeview(
            self, columns=("ID", "Nombre", "Teléfono", "Email", "Producto", "Cantidad"),
            show="headings", height=10
        )
        for col in self.clients_table["columns"]:# Configuración de columnas de la tabla
            self.clients_table.heading(col, text=col)
            self.clients_table.column(col, anchor="center", width=120)

        self.clients_table.pack(pady=10, padx=10, fill="both", expand=True)# Tabla ocupa todo el espacio disponible
        self.clients_table.bind("<Double-1>", self.on_item_selected)# Evento de doble clic para seleccionar un cliente

        self._style_table()# Método para aplicar estilo a la tabla

    def _add_entry(self, parent, label, row, column):# Método para crear entradas con etiquetas
        ct.CTkLabel(parent, text=label).grid(row=row, column=column, padx=10, pady=5, sticky="e")
        entry = ct.CTkEntry(parent, width=180)
        entry.grid(row=row, column=column + 1, padx=10, pady=5)
        return entry

    def _style_table(self):# Método para aplicar estilo a la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#1a1a1a", foreground="white", fieldbackground="#1a1a1a", rowheight=30, font=('Arial', 11))
        style.configure("Treeview.Heading", background="#2A9D8F", foreground="white", font=('Arial', 11, 'bold'))
        style.map("Treeview", background=[('selected', '#21867A')], foreground=[('selected', 'white')])

    def _add_entry(self, parent, label_text, row, column):# Método para crear entradas con etiquetas
         label = ct.CTkLabel(parent, text=label_text, font=ct.CTkFont(size=14))
         label.grid(row=row, column=column, sticky="e", padx=(5, 2), pady=8)

         entry = ct.CTkEntry(parent, width=200, height=30, corner_radius=8)
         entry.grid(row=row, column=column + 1, padx=(2, 10), pady=8)
         return entry


    def populate_table(self):# Método para llenar la tabla con datos de clientes
        for row in self.clients_table.get_children():
            self.clients_table.delete(row)
        for client_id, data in self.clients.items():
            self.clients_table.insert("", "end", values=(
                client_id, data["nombre"], data["telefono"],
                data["correo"], data["producto"], data["cantidad"]
            ))

    def add_client(self):# Método para agregar un nuevo cliente
        client_id = self.id_entry.get()
        if client_id in self.clients:
            messagebox.showerror("Error", "El ID ya existe.")
            return
        self.clients[client_id] = {
            "nombre": self.name_entry.get(),
            "telefono": self.phone_entry.get(),
            "correo": self.email_entry.get(),
            "producto": self.product_entry.get(),
            "cantidad": self.quantity_entry.get()
        }
        self.populate_table()
        self.clear_entries()

    def update_client(self):# Método para actualizar un cliente existente
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un cliente para actualizar.")
            return

        self.clients[self.current_id] = {
            "nombre": self.name_entry.get(),
            "telefono": self.phone_entry.get(),
            "correo": self.email_entry.get(),
            "producto": self.product_entry.get(),
            "cantidad": self.quantity_entry.get()
        }
        self.populate_table()# Actualiza la tabla con los nuevos datos
        self.clear_entries()

    def delete_client(self):# Método para eliminar un cliente
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un cliente para eliminar.")
            return
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este cliente?"):
            del self.clients[self.current_id]
            self.populate_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "¡Cliente eliminado exitosamente!")
        messagebox.showinfo("Éxito", "¡Cliente eliminado exitosamente!")
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este cliente?"):
            del self.clients[self.current_id]
            self.populate_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "¡Cliente eliminado exitosamente!")

    def on_item_selected(self, event):# Método para manejar la selección de un cliente en la tabla
        selected_item = self.clients_table.selection()[0]
        values = self.clients_table.item(selected_item, "values")
        self.current_id = values[0]
        self.id_entry.delete(0, ct.END)
        self.id_entry.insert(0, values[0])
        self.name_entry.delete(0, ct.END)
        self.name_entry.insert(0, values[1])
        self.phone_entry.delete(0, ct.END)
        self.phone_entry.insert(0, values[2])
        self.email_entry.delete(0, ct.END)
        self.email_entry.insert(0, values[3])
        self.product_entry.delete(0, ct.END)
        self.product_entry.insert(0, values[4])
        self.quantity_entry.delete(0, ct.END)
        self.quantity_entry.insert(0, values[5])

    def clear_entries(self):# Método para limpiar los campos de entrada
        for entry in [self.id_entry, self.name_entry, self.phone_entry,
                      self.email_entry, self.product_entry, self.quantity_entry]:
            entry.delete(0, ct.END)
        self.current_id = None

    def back_to_dashboard(self):
        self.destroy()
        self.master.deiconify()


if __name__ == "__main__":
    root = ct.CTk()
    app = ClientsApp(root)
    root.mainloop()
