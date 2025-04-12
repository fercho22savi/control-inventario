# 📦 Sistema de Control de Inventario

Este repositorio contiene un sistema de gestión de inventario con interfaz gráfica, desarrollado en Python utilizando `CustomTkinter`. El sistema está diseñado para administrar **clientes**, **proveedores** y **productos** desde un panel central o _dashboard_.

---

## 🎯 Funcionalidades

- **Dashboard moderno** con diseño oscuro y transparente.
- Módulo de **Clientes**.
- Módulo de **Proveedores**.
- Módulo de **Productos**.
- Navegación fluida entre módulos.
- Botón de salida para cerrar la aplicación.

---

## 🖥️ Tecnologías utilizadas

- Python 3
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (para una interfaz moderna y personalizable)
- Estructura modular

---

## 📁 Estructura del proyecto

## Requisitos:
## Instala los requisitos (si no tienes CustomTkinter):

pip install customtkinter

🧠 Sobre el código
El archivo dashboard.py contiene la clase principal Dashboard, 
que representa la ventana principal con botones para abrir cada uno de los módulos del sistema. 
Cada botón llama a una clase distinta para manejar las operaciones específicas:

SuppliersApp para proveedores.

ClientsApp para clientes.

ProductApp para productos.

Al hacer clic en un botón, se oculta el dashboard actual y se muestra el módulo correspondiente,
 permitiendo al usuario trabajar de forma específica y luego regresar al panel general.

📌 Notas adicionales
El sistema utiliza set_appearance_mode("dark") y set_default_color_theme("dark-blue") para una experiencia visual moderna.

Los módulos deben ser desarrollados y mantenidos en sus archivos correspondientes para asegurar una buena organización.

✍️ Autor
Fernando saldaña
YouTuber y desarrollador 


