import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk

class SuppliersApp(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Gestión de Proveedores")
        self.geometry("900x600")
        self.configure(fg_color="#121212")

        self.suppliers = {}
        self.current_id = None

        # Estilo oscuro para la tabla
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#1E1E1E",
                        foreground="white",
                        fieldbackground="#1E1E1E",
                        rowheight=28,
                        font=("Arial", 12))
        style.configure("Treeview.Heading",
                        background="#2A9D8F",
                        foreground="white",
                        font=("Arial", 12, "bold"))
        style.map("Treeview",
                  background=[("selected", "#21867A")],
                  foreground=[("selected", "white")])

        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        form_frame = ctk.CTkFrame(self, fg_color="#1C1C1C")
        form_frame.pack(pady=15, padx=20, fill="x")

        # Entradas
        self.id_entry = self.create_labeled_entry(form_frame, "ID:", 0)
        self.name_entry = self.create_labeled_entry(form_frame, "Nombre:", 1)
        self.surname_entry = self.create_labeled_entry(form_frame, "Apellido:", 2)
        self.phone_entry = self.create_labeled_entry(form_frame, "Teléfono:", 3)
        self.address_entry = self.create_labeled_entry(form_frame, "Dirección:", 4)

        # Botones
        button_frame = ctk.CTkFrame(self, fg_color="#121212")
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Agregar", width=140, command=self.add_supplier).grid(row=0, column=0, padx=6)
        ctk.CTkButton(button_frame, text="Actualizar", width=140, command=self.update_supplier).grid(row=0, column=1, padx=6)
        ctk.CTkButton(button_frame, text="Eliminar", width=140, command=self.delete_supplier).grid(row=0, column=2, padx=6)
        ctk.CTkButton(button_frame, text="Limpiar", width=140, command=self.clear_entries).grid(row=0, column=3, padx=6)
        ctk.CTkButton(button_frame, text="Regresar", width=140, command=self.back_to_dashboard).grid(row=0, column=4, padx=6)

        # Tabla
        self.suppliers_table = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido", "Teléfono", "Dirección"), show='headings')
        for col in ("ID", "Nombre", "Apellido", "Teléfono", "Dirección"):
            self.suppliers_table.heading(col, text=col)
            self.suppliers_table.column(col, anchor="center", width=120)

        self.suppliers_table.pack(pady=20, padx=20, fill="both", expand=True)
        self.suppliers_table.bind("<Double-1>", self.on_item_selected)

    def create_labeled_entry(self, parent, text, row):
        label = ctk.CTkLabel(parent, text=text, text_color="white")
        label.grid(row=row, column=0, sticky="w", padx=10, pady=8)
        entry = ctk.CTkEntry(parent, width=300)
        entry.grid(row=row, column=1, pady=8)
        return entry

    def populate_table(self):
        for row in self.suppliers_table.get_children():
            self.suppliers_table.delete(row)
        for supplier_id, data in self.suppliers.items():
            self.suppliers_table.insert("", "end", values=(supplier_id, data["name"], data["surname"], data["phone"], data["address"]))

    def add_supplier(self):
        supplier_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        surname = self.surname_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        if supplier_id in self.suppliers:
            messagebox.showerror("Error", "El ID ya existe.")
            return

        if not supplier_id or not name or not surname or not phone or not address:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.suppliers[supplier_id] = {"name": name, "surname": surname, "phone": phone, "address": address}
        self.populate_table()
        self.clear_entries()
        messagebox.showinfo("Éxito", "¡Proveedor agregado exitosamente!")

    def update_supplier(self):
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un proveedor para actualizar.")
            return

        name = self.name_entry.get().strip()
        surname = self.surname_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not surname or not phone or not address:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.suppliers[self.current_id] = {
            "name": name,
            "surname": surname,
            "phone": phone,
            "address": address
        }

        self.populate_table()
        self.clear_entries()
        messagebox.showinfo("Éxito", "¡Proveedor actualizado exitosamente!")

    def delete_supplier(self):
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un proveedor para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este proveedor?")
        if confirm:
            del self.suppliers[self.current_id]
            self.populate_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "¡Proveedor eliminado exitosamente!")

    def on_item_selected(self, event):
        selected = self.suppliers_table.selection()
        if selected:
            item_data = self.suppliers_table.item(selected[0], "values")
            self.current_id = item_data[0]

            self.id_entry.configure(state="normal")
            self.id_entry.delete(0, "end")
            self.id_entry.insert(0, item_data[0])
            self.id_entry.configure(state="disabled")

            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, item_data[1])
            self.surname_entry.delete(0, "end")
            self.surname_entry.insert(0, item_data[2])
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert(0, item_data[3])
            self.address_entry.delete(0, "end")
            self.address_entry.insert(0, item_data[4])

    def clear_entries(self):
        self.id_entry.configure(state="normal")
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.surname_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.current_id = None

    def back_to_dashboard(self):
        self.destroy()
        self.master.deiconify()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.withdraw()
    app = SuppliersApp(root)
    app.mainloop()
    root.destroy()