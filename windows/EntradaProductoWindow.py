import customtkinter as ctk
from datetime import datetime
from tkinter import ttk
from tkcalendar import DateEntry

class EntradaProductoWindow(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)


        self.title_label = ctk.CTkLabel(self.main_frame, text="Registrar Entrada de Producto", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)


        self.datetime_label = ctk.CTkLabel(self.main_frame, text="Fecha de entrada:")
        self.datetime_label.pack(pady=5)
        self.date_entry = DateEntry(self.main_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack(pady=5)


        self.product_label = ctk.CTkLabel(self.main_frame, text="Producto:")
        self.product_label.pack(pady=5)

        self.product_options = ["Silla", "Mesa", "Escritorio", "Lámpara", "Computadora"]
        self.product_dropdown = ctk.CTkOptionMenu(self.main_frame, values=self.product_options)
        self.product_dropdown.pack(pady=5)


        self.quantity_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Cantidad")
        self.quantity_entry.pack(pady=5)


        self.supplier_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Proveedor (Opcional)")
        self.supplier_entry.pack(pady=5)


        self.btn_register = ctk.CTkButton(self.main_frame, text="Registrar", command=self.register_product)
        self.btn_register.pack(pady=10)


        self.records_tree = ttk.Treeview(self.main_frame, columns=("Fecha", "Producto", "Cantidad", "Proveedor"), show="headings")
        for col in ("Fecha", "Producto", "Cantidad", "Proveedor"):
            self.records_tree.heading(col, text=col)
            self.records_tree.column(col, anchor="center")

        self.records_tree.pack(pady=10)
        self.records_tree.configure(selectmode="none")


        self.btn_back = ctk.CTkButton(self.main_frame, text="Volver al Dashboard", command=self.controller.back_to_dashboard)
        self.btn_back.pack(pady=10)

    def register_product(self):

        product_name = self.product_dropdown.get()
        quantity = self.quantity_entry.get().strip()
        supplier = self.supplier_entry.get().strip() or "N/A"
        timestamp = f"{self.date_entry.get()} {datetime.now().strftime('%H:%M:%S')}"

        if product_name and quantity.isdigit():
            self.records_tree.insert("", "end", values=(timestamp, product_name, quantity, supplier))
            self.clear_fields()

    def clear_fields(self):

        self.quantity_entry.delete(0, "end")
        self.supplier_entry.delete(0, "end")
