import customtkinter as ctk

from windows.ConsultaExistenciaSearchView import ConsultaExistenciaSearchView
from windows.MisVentasWindow import MisVentasWindow

class VentasDashboard(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(side="top", fill="both", expand=True)

        self.current_content_view = None

        self._create_widgets()
        self._setup_layout()

        self.show_consulta_existencia_search_view()

    def _create_widgets(self):
        self.sidebar = ctk.CTkFrame(self, width=200)

        self.btn_solicitud = ctk.CTkButton(
            self.sidebar,
            text="Crear Solicitud",
            command=lambda: self.controller.show_crear_solicitud_venta(),
        )

        self.btn_mis_ventas = ctk.CTkButton(
            self.sidebar,
            text="Ver Mis Solicitudes/Ventas",
            command=lambda: self.show_mis_ventas_content(),
        )
        self.btn_mis_ventas.pack(pady=5, fill="x")

        self.btn_logout = ctk.CTkButton(
            self.sidebar,
            text="Cerrar Sesión",
            command=lambda: self.controller.show_login(),
        )

        self.content_frame = ctk.CTkFrame(self)
        self.welcome_label = ctk.CTkLabel(
            self.content_frame,
            text="Bienvenido al Dashboard de Ventas",
            font=("Arial", 16),
        )

    def _setup_layout(self):
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.btn_solicitud.pack(pady=5, fill="x")
        self.btn_mis_ventas.pack(pady=5, fill="x")
        self.btn_logout.pack(pady=20, fill="x")

        self.content_frame.pack(
            side="right", fill="both", expand=True, padx=10, pady=10
        )
        self.welcome_label.pack(pady=50)

    def _clear_content_frame(self):
        if self.current_content_view:
            self.current_content_view.destroy()
            self.current_content_view = None
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_consulta_existencia_search_view(self):
        self._clear_content_frame()

        new_view = ConsultaExistenciaSearchView(self.content_frame, self.controller)
        self.current_content_view = new_view
        self.controller.root.title("Sistema de Inventario - Consulta de Existencia")

    def show_mis_ventas_content(self):
        self._clear_content_frame()
        new_view = MisVentasWindow(self.content_frame, self.controller)
        self.current_content_view = new_view
        self.controller.root.title("Sistema de Inventario - Mis Solicitudes de Venta")

    def show_welcome_content(self):
        self._clear_content_frame()
        welcome_label = ctk.CTkLabel(self.content_frame, text="Biencenidos al Dashboard de Ventas", font=("Arial", 16))
        welcome_label.pack(pady=50)
