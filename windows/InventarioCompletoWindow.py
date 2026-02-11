import customtkinter as ctk
from tkinter import ttk

class InventarioCompletoWindow(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)


        self.filter_frame = ctk.CTkFrame(self.main_frame)
        self.filter_frame.pack(fill="x", padx=5, pady=5)

        self.search_entry = ctk.CTkEntry(
            self.filter_frame, placeholder_text="Buscar..."
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)

        self.search_btn = ctk.CTkButton(self.filter_frame, text="Buscar", width=80)
        self.search_btn.pack(side="left", padx=5)


        self.filter_options = ctk.CTkOptionMenu(
            self.filter_frame, values=["Todos", "Muebles", "Oficina", "Electrónicos"]
        )
        self.filter_options.pack(side="left", padx=5)


        self.table_frame = ctk.CTkFrame(self.main_frame)
        self.table_frame.pack(fill="both", expand=True, padx=5, pady=5)


        self.inventory_tree = ttk.Treeview(self.table_frame, columns=("producto", "categoria", "cantidad", "ubicacion"), show="headings")
        for col, title in zip(("producto", "categoria", "cantidad", "ubicacion"), ("Producto", "Categoría", "Cantidad", "Ubicación")):
            self.inventory_tree.heading(col, text=title)
            self.inventory_tree.column(col, anchor="center", width=180)

        self.inventory_tree.pack(fill="both", expand=True)


        self.action_buttons_frame = ctk.CTkFrame(self.table_frame)
        self.action_buttons_frame.pack(fill="x", pady=10)

        self.modify_button = ctk.CTkButton(self.action_buttons_frame, text="Modificar", width=120)
        self.modify_button.pack(side="right", padx=5)

        self.delete_button = ctk.CTkButton(self.action_buttons_frame, text="Eliminar", width=120)
        self.delete_button.pack(side="right", padx=5)


        self.export_frame = ctk.CTkFrame(self.main_frame)
        self.export_frame.pack(fill="x", padx=5, pady=5)

        self.excel_btn = ctk.CTkButton(self.export_frame, text="Exportar a Excel")
        self.excel_btn.pack(side="left", padx=5)

        self.pdf_btn = ctk.CTkButton(self.export_frame, text="Exportar a PDF")
        self.pdf_btn.pack(side="left", padx=5)


        self.btn_back = ctk.CTkButton(
            self.main_frame,
            text="Volver al Dashboard",
            command=self.controller.back_to_dashboard,
        )
        self.btn_back.pack(pady=10)
