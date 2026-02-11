import customtkinter as ctk

class ConsultaExistenciaWindow(ctk.CTkToplevel):
    def __init__(self, master, controller_instance, search_results=None):
        super().__init__(master)
        self.controller = controller_instance
        self.search_results = search_results

        self.title("Resultados de Consulta de Existencia")
        self.geometry("700x400")
        self.transient(master)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._create_widgets()
        self._setup_layout()

        if self.search_results:
            self.display_results(self.search_results)
        else:
            self.show_message("No se encontraron resultados para la consulta.")


    def _create_widgets(self):
        self.frame_resultados = ctk.CTkFrame(self)
        self.frame_resultados.pack(fill="both", expand=True, padx=10, pady=10)

        self.resultado_label = ctk.CTkLabel(self.frame_resultados, text="")
        self.resultado_label.pack(pady=20)

        self.tabla_resultados = None

        self.btn_cerrar = ctk.CTkButton(self, text="Cerrar", command=self._on_closing)
        self.btn_cerrar.pack(pady=10)

    def _setup_layout(self):
        pass

    def _on_closing(self):
        self.grab_release()
        self.destroy()

    def show_message(self, message):
        """Muestra un mensaje en el área de resultados."""
        if self.tabla_resultados:
            self.tabla_resultados.destroy()
            self.tabla_resultados = None
        self.resultado_label.configure(text=message)
        self.resultado_label.pack_forget()
        self.resultado_label.pack(pady=20)

    def display_results(self, results):
        self._clear_results_area()

        if not results:
            self.show_message("No se encontraron productos con ese nombre.")
            return

        headers = ["Producto", "Cantidad", "Disponibilidad"]
        header_frame = ctk.CTkFrame(self.frame_resultados)
        header_frame.pack(fill="x", padx=5, pady=(5, 0))

        for col, header_text in enumerate(headers):
            label = ctk.CTkLabel(header_frame, text=header_text, font=ctk.CTkFont(weight="bold"))
            label.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
            header_frame.grid_columnconfigure(col, weight=1)

        self.tabla_resultados = ctk.CTkScrollableFrame(self.frame_resultados)
        self.tabla_resultados.pack(fill="both", expand=True, padx=5, pady=(0, 5))

        for row_idx, data in enumerate(results):
            row_frame = ctk.CTkFrame(self.tabla_resultados)
            row_frame.pack(fill="x", pady=2)

            ctk.CTkLabel(row_frame, text=data["nombre"]).grid(row=0, column=0, sticky="nsew", padx=5, pady=2)
            ctk.CTkLabel(row_frame, text=str(data["cantidad"])).grid(row=0, column=1, sticky="nsew", padx=5, pady=2)
            
            disponibilidad_color = "green" if data["disponibilidad"] == "Sí" else "red"
            ctk.CTkLabel(row_frame, text=data["disponibilidad"], text_color=disponibilidad_color).grid(row=0, column=2, sticky="nsew", padx=5, pady=2)
            
            row_frame.grid_columnconfigure(0, weight=1)
            row_frame.grid_columnconfigure(1, weight=1)
            row_frame.grid_columnconfigure(2, weight=1)

        self.resultado_label.pack_forget()

    def _clear_results_area(self):
        if self.tabla_resultados:
            self.tabla_resultados.destroy()
            self.tabla_resultados = None
        self.resultado_label.pack_forget()
        self.resultado_label.configure(text="")
