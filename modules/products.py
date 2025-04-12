import tkinter as tk
import customtkinter as ct
from tkinter import ttk, messagebox



# Clase Producto
class ProductData:
    def __init__(self, id, product, price, quantity, description=""):
        self.id = id
        self.product = product
        self.price = price
        self.quantity = quantity
        self.description = description

    def as_tuple(self):
        return (self.id, self.product, f"${self.price:.2f}", str(self.quantity), self.description)


# Interfaz gráfica
class ProductApp(ct.CTkToplevel):  # Usamos CTkToplevel para permitir volver a dashboard
    def __init__(self,master):# Cambiamos el nombre de la clase a ProductApp
        self.master = master
        super().__init__()
        self.title("Formulario de Producto")
        self.geometry("800x650")
        self.resizable(False, False)
        self.configure(fg_color="black")
        self.wm_attributes("-alpha", 0.95)

        self.products = {}
        self.current_id = None

        # Título
        ct.CTkLabel(self, text="Productos", font=("Helvetica", 22, "bold"), text_color="white").pack(pady=15)

        # Entradas de datos
        self.id_entry = self.create_labeled_entry("ID:")
        self.product_entry = self.create_labeled_entry("Producto:")
        self.quantity_entry = self.create_labeled_entry("Cantidad:")
        self.price_entry = self.create_labeled_entry("Precio Unitario:")
        self.description_entry = self.create_labeled_entry("Descripción:")

        # Botones
        btn_frame = ct.CTkFrame(self, fg_color="black")
        btn_frame.pack(pady=10)

        ct.CTkButton(btn_frame, text="Registrar", command=self.register_product,
                     fg_color="#2A9D8F", hover_color="#21867A", text_color="white", width=120).grid(row=0, column=0, padx=5)

        ct.CTkButton(btn_frame, text="Actualizar", command=self.update_product,
                     fg_color="#264653", hover_color="#1F3D3D", text_color="white", width=120).grid(row=0, column=1, padx=5)

        ct.CTkButton(btn_frame, text="Eliminar", command=self.delete_product,
                     fg_color="#E63946", hover_color="#C53030", text_color="white", width=120).grid(row=0, column=2, padx=5)

        ct.CTkButton(btn_frame, text="Borrar Campos", command=self.clear_entries,
                     fg_color="#6C757D", hover_color="#5A6268", text_color="white", width=120).grid(row=0, column=3, padx=5)

        ct.CTkButton(btn_frame, text="Regresar", command=self.back_to_dashboard,
                     fg_color="#F4A261", hover_color="#E76F51", text_color="white", width=120).grid(row=0, column=4, padx=5)

        # Tabla
        self.table_frame = ct.CTkFrame(self, fg_color="black")
        self.table_frame.pack(pady=20, fill="both", expand=True, padx=20)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#1e1e1e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#1e1e1e")
        style.map("Treeview", background=[('selected', '#2A9D8F')])

        self.tree = ttk.Treeview(self.table_frame, columns=("ID", "Producto", "Cantidad", "Precio Unitario", "Precio Total", "Descripcion"),
                                 show="headings", height=10)
        self.tree.pack(fill="both", expand=True)

        for col in ("ID", "Producto", "Cantidad", "Precio Unitario", "Precio Total", "Descripcion"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=120)

        self.tree.bind("<ButtonRelease-1>", self.select_product)
       
       

    def create_labeled_entry(self, label_text):# Método para crear entradas con etiquetas
        frame = ct.CTkFrame(self, fg_color="black")
        frame.pack(pady=5, fill="x", padx=20)
        label = ct.CTkLabel(frame, text=label_text, width=120, anchor="w", text_color="white")
        label.pack(side="left")
        entry = ct.CTkEntry(frame, fg_color="#222222", text_color="white", placeholder_text="Escribe aquí ...")
        entry.pack(side="left", expand=True, fill="x")
        return entry

    def register_product(self):# Método para registrar un producto
        try:
            id = self.id_entry.get()
            product = self.product_entry.get()
            quantity = int(self.quantity_entry.get())
            price1 = float(self.price_entry.get())
            description = self.description_entry.get()

            if not id or not product:# Validación de campos requeridos
                messagebox.showwarning("Campos requeridos", "ID y Producto son obligatorios.")
                return

            total_price = price1 * quantity
            values = (id, product, str(quantity), f"${price1:.0f}", f"${total_price:.0f}", description)
            self.tree.insert('', 'end', values=values)

            self.clear_entries()
            self.id_entry.focus_set()
            messagebox.showinfo("Registro", "Producto registrado.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese precio numérico y cantidad entera.")
        

    def update_product(self):
    # Cargar datos del producto seleccionado a los campos de entrada
      selected = self.tree.selection()
      if selected:
        values = self.tree.item(selected, 'values')
        if values:
            self.id_entry.configure(state="normal")
            self.id_entry.delete(0, 'end')
            self.id_entry.insert(0, values[0])
            self.product_entry.delete(0, 'end')
            self.product_entry.insert(0, values[1])
            self.quantity_entry.delete(0, 'end')
            self.quantity_entry.insert(0, values[2])
            self.price_entry.delete(0, 'end')
            self.price_entry.insert(0, values[3].replace('$', ''))
            self.description_entry.delete(0, 'end')
            self.description_entry.insert(0, values[5])
            self.current_id = selected  # Guardar cuál es el producto seleccionado
      else:
        messagebox.showwarning("Selecciona", "Selecciona un producto de la tabla.")


    def delete_product(self):# Método para eliminar un producto
        selected = self.tree.selection()
        if selected:# Verifica si hay un producto seleccionado
            confirm = messagebox.askyesno("Confirmar eliminación", "¿Seguro que deseas eliminar el producto?")
            if confirm:
                self.tree.delete(selected)
                self.clear_entries()
                messagebox.showinfo("Eliminado", "Producto eliminado.")
        else:
            messagebox.showwarning("Selecciona", "Selecciona un producto en la tabla.")

    def clear_entries(self):# Método para limpiar las entradas
        self.id_entry.configure(state="normal")
        self.id_entry.delete(0, 'end')
        self.product_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.current_id = None

    def select_product(self, event):# Método para seleccionar un producto en la tabla
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected)["values"]
            if values:
                self.id_entry.delete(0, 'end')
                self.product_entry.delete(0, 'end')
                self.price_entry.delete(0, 'end')
                self.quantity_entry.delete(0, 'end')
                self.total_price_entry.delete(0, 'end')
                self.description_entry.delete(0, 'end')

                self.id_entry.insert(0, values[0])
                self.product_entry.insert(0, values[1])
                self.quantity_entry.insert(0, values[2])
                self.price_entry.insert(0, values[3])
                self.total_price_entry.insert(0, values[4])
                self.description_entry.insert(0, values[5])

    def back_to_dashboard(self):# Método para regresar al dashboard
        self.destroy()
        self.master.deiconify()


# Ejecutar la app (para pruebas)
if __name__ == "__main__":
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")
    root = ct.CTk()
    root.withdraw()  # Oculta ventana principal
    app = ProductApp(root)
    app.mainloop()