import customtkinter as ctk
from tkinter import ttk

class CrearSolicitudVentaWindow(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)


        self.client_frame = ctk.CTkFrame(self.main_frame)
        self.client_frame.pack(fill="x", padx=5, pady=5)

        self.client_label = ctk.CTkLabel(
            self.client_frame, text="Datos del Cliente", font=("Arial", 14)
        )
        self.client_label.pack(anchor="w")

        self.client_entry = ctk.CTkEntry(
            self.client_frame, placeholder_text="Nombre del cliente"
        )
        self.client_entry.pack(fill="x", pady=5)


        self.add_frame = ctk.CTkFrame(self.main_frame)
        self.add_frame.pack(fill="x", padx=5, pady=5)

        self.product_search = ctk.CTkEntry(
            self.add_frame, placeholder_text="Buscar producto..."
        )
        self.product_search.pack(side="left", fill="x", expand=True, padx=5)

        self.qty_entry = ctk.CTkEntry(
            self.add_frame, placeholder_text="Cantidad", width=80
        )
        self.qty_entry.pack(side="left", padx=5)

        self.add_btn = ctk.CTkButton(self.add_frame, text="Añadir", width=80)
        self.add_btn.pack(side="left", padx=5)


        self.table_frame = ctk.CTkFrame(self.main_frame)
        self.table_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.solicitud_tree = ttk.Treeview(self.table_frame, columns=("producto", "cantidad"), show="headings")
        for col, title in zip(("producto", "cantidad"), ("Producto", "Cantidad")):
            self.solicitud_tree.heading(col, text=title)
            self.solicitud_tree.column(col, anchor="center", width=400)

        self.solicitud_tree.pack(fill="both", expand=True)


        self.send_btn = ctk.CTkButton(
            self.main_frame, text="Enviar Solicitud a Almacén"
        )
        self.send_btn.pack(pady=10)


        self.btn_back = ctk.CTkButton(
            self.main_frame, text="Volver", command=self.controller.back_to_dashboard
        )
        self.btn_back.pack(pady=10)
