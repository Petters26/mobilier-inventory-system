import customtkinter as ctk
from tkinter import ttk

class GestionProductosWindow(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True)


        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)


        self.tabview = ctk.CTkTabview(self.main_frame)
        self.tabview.pack(fill="both", expand=True)

        self.tab_productos = self.tabview.add("Productos")  
        self.tab_tipos = self.tabview.add("Tipos de Producto")  



        self.frame_form = ctk.CTkFrame(self.tab_productos)
        self.frame_form.pack(fill="x", padx=10, pady=10)

        self.lbl_nombre = ctk.CTkLabel(self.frame_form, text="Nombre:")
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = ctk.CTkEntry(self.frame_form)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_categoria = ctk.CTkLabel(self.frame_form, text="Categoría:")
        self.lbl_categoria.grid(row=1, column=0, padx=10, pady=5)
        self.entry_categoria = ctk.CTkEntry(self.frame_form)
        self.entry_categoria.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_precio = ctk.CTkLabel(self.frame_form, text="Precio:")
        self.lbl_precio.grid(row=2, column=0, padx=10, pady=5)
        self.entry_precio = ctk.CTkEntry(self.frame_form)
        self.entry_precio.grid(row=2, column=1, padx=10, pady=5)

        self.lbl_stock = ctk.CTkLabel(self.frame_form, text="Stock:")
        self.lbl_stock.grid(row=3, column=0, padx=10, pady=5)
        self.entry_stock = ctk.CTkEntry(self.frame_form)
        self.entry_stock.grid(row=3, column=1, padx=10, pady=5)

        self.btn_guardar = ctk.CTkButton(self.frame_form, text="Guardar Producto", command=self._guardar_producto)
        self.btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)


        self.table_frame = ctk.CTkFrame(self.tab_productos)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.records_tree = ttk.Treeview(self.table_frame, columns=("nombre", "categoria", "precio", "stock"), show="headings")
        for col, title in zip(("nombre", "categoria", "precio", "stock"), ("Nombre", "Categoría", "Precio", "Stock")):
            self.records_tree.heading(col, text=title)
            self.records_tree.column(col, anchor="center", width=150)

        self.records_tree.pack(fill="both", expand=True)


        self.action_buttons_frame = ctk.CTkFrame(self.table_frame)
        self.action_buttons_frame.pack(fill="x", pady=10)

        self.modify_button = ctk.CTkButton(self.action_buttons_frame, text="Modificar", width=120)
        self.modify_button.pack(side="right", padx=5)

        self.delete_button = ctk.CTkButton(self.action_buttons_frame, text="Eliminar", width=120)
        self.delete_button.pack(side="right", padx=5)



        self.table_tipos_frame = ctk.CTkFrame(self.tab_tipos)
        self.table_tipos_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.records_tipos_tree = ttk.Treeview(self.table_tipos_frame, columns=("tipo_producto",), show="headings")
        self.records_tipos_tree.heading("tipo_producto", text="Tipo de Producto")
        self.records_tipos_tree.column("tipo_producto", anchor="center", width=300)

        self.records_tipos_tree.pack(fill="both", expand=True)


        self.action_tipos_buttons_frame = ctk.CTkFrame(self.table_tipos_frame)
        self.action_tipos_buttons_frame.pack(fill="x", pady=10)

        self.add_tipo_button = ctk.CTkButton(self.action_tipos_buttons_frame, text="Añadir Tipos", width=120)
        self.add_tipo_button.pack(side="right", padx=5)

        self.delete_tipo_button = ctk.CTkButton(self.action_tipos_buttons_frame, text="Eliminar Tipos", width=120)
        self.delete_tipo_button.pack(side="right", padx=5)



        self.btn_back = ctk.CTkButton(self.main_frame, text="Volver al Dashboard", command=self.controller.back_to_dashboard)
        self.btn_back.pack(pady=10)

    def _guardar_producto(self):
        nombre = self.entry_nombre.get().strip()
        categoria = self.entry_categoria.get().strip()
        precio = self.entry_precio.get().strip()
        stock = self.entry_stock.get().strip()

        if nombre and categoria and precio.isdigit() and stock.isdigit():
            self.records_tree.insert("", "end", values=(nombre, categoria, precio, stock))
            self._clear_fields()
        else:
            pass

    def _clear_fields(self):
        self.entry_nombre.delete(0, "end")
        self.entry_categoria.delete(0, "end")
        self.entry_precio.delete(0, "end")
        self.entry_stock.delete(0, "end")
