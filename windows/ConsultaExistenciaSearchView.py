import customtkinter as ctk

class ConsultaExistenciaSearchView(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True, padx=10, pady=10)

        self._create_widgets()
        self.entry_busqueda.focus_set()

    def _create_widgets(self):
        self.frame_busqueda = ctk.CTkFrame(self)
        self.frame_busqueda.pack(pady=20, fill="x")

        self.label_busqueda = ctk.CTkLabel(self.frame_busqueda, text="Buscar Producto por Nombre:", font=("Arial", 14, "bold"))
        self.label_busqueda.pack(side="left", padx=10, pady=5)

        self.entry_busqueda = ctk.CTkEntry(self.frame_busqueda, placeholder_text="Ingrese nombre del producto. . .", font=("Arial", 14))
        self.entry_busqueda.pack(side="left", fill="x", expand=True, padx=10, pady=5)
        self.entry_busqueda.bind("<Return>", self._on_buscar)

        self.btn_buscar = ctk.CTkButton(self.frame_busqueda, text="Buscar", command=self._on_buscar, font=("Arial", 14, "bold"))
        self.btn_buscar.pack(side="left", padx=10, pady=5)

        self.info_label = ctk.CTkLabel(self, text="Ingrese el nombre de un producto para consultar su existencia. \nLos resultados se mostrarán en una nueva ventana emergente.", font=("Arial", 12), text_color="gray")
        self.info_label.pack(pady=30)

    def _on_buscar(self, event=None):
        query = self.entry_busqueda.get().strip()
        if not query:
            self.controller.show_results_popup([])
            return

        search_results = self._simular_busqueda(query)

        self.controller.show_results_popup(search_results)

    def _simular_busqueda(self, query):
        productos_existentes = {
            "silla": {"cantidad": 50, "disponible": True},
            "mesa": {"cantidad": 5, "disponible": True},
            "escritorio": {"cantidad": 0, "disponible": False},
        }
        query_lower = query.lower()

        found_products = []
        for producto, data in productos_existentes.items():
            if query_lower in producto:
                found_products.append({
                    "nombre": producto.capitalize(),
                    "cantidad": data["cantidad"],
                    "disponibilidad": "Sí" if data["disponible"] else "No"
                })
        return found_products