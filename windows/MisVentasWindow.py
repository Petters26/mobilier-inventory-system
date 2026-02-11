import customtkinter as ctk
from tkinter import ttk

class MisVentasWindow(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)


        self.filter_frame = ctk.CTkFrame(self.main_frame)
        self.filter_frame.pack(fill="x", padx=5, pady=5)

        self.date_from = ctk.CTkEntry(
            self.filter_frame, placeholder_text="Desde (dd/mm/aaaa)", width=120
        )
        self.date_from.pack(side="left", padx=5)

        self.date_to = ctk.CTkEntry(
            self.filter_frame, placeholder_text="Hasta (dd/mm/aaaa)", width=120
        )
        self.date_to.pack(side="left", padx=5)

        self.status_filter = ctk.CTkOptionMenu(
            self.filter_frame, values=["Todos", "Pendiente", "Despachado", "Cancelado"]
        )
        self.status_filter.pack(side="left", padx=5)

        self.filter_btn = ctk.CTkButton(self.filter_frame, text="Filtrar")
        self.filter_btn.pack(side="left", padx=5)


        self.table_frame = ctk.CTkFrame(self.main_frame)
        self.table_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.sales_tree = ttk.Treeview(self.table_frame, columns=("fecha", "producto", "cantidad", "total"), show="headings")
        for col, title in zip(("fecha", "producto", "cantidad", "total"), ("Fecha", "Producto", "Cantidad", "Total")):
            self.sales_tree.heading(col, text=title)
            self.sales_tree.column(col, anchor="center", width=180)

        self.sales_tree.pack(fill="both", expand=True)


        self.detail_frame = ctk.CTkFrame(self.main_frame)
        self.detail_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.detail_label = ctk.CTkLabel(
            self.detail_frame, text="Detalles de la venta seleccionada"
        )
        self.detail_label.pack(anchor="w")


        self.detail_tree = ttk.Treeview(self.detail_frame, columns=("producto", "precio", "cantidad", "subtotal"), show="headings")
        for col, title in zip(("producto", "precio", "cantidad", "subtotal"), ("Producto", "Precio", "Cantidad", "Subtotal")):
            self.detail_tree.heading(col, text=title)
            self.detail_tree.column(col, anchor="center", width=180)

        self.detail_tree.pack(fill="both", expand=True)


        self.btn_back = ctk.CTkButton(
            self.main_frame, text="Volver", command=self.controller.back_to_dashboard
        )
        self.btn_back.pack(pady=10)
