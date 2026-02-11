import customtkinter as ctk
from windows.SalidaProductoWindow import SalidaProductoWindow


class AlmacenDashboard(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(side="top", fill="both", expand=True)

        self.current_content_view = None

        self._create_widgets()
        self._setup_layout()

    def _create_widgets(self):
        self.sidebar = ctk.CTkFrame(self, width=200)

        self.btn_gestion = ctk.CTkButton(
            self.sidebar,
            text="Gestionar Productos",
            command=lambda: self.controller.show_gestion_productos(),
        )

        self.btn_entrada = ctk.CTkButton(
            self.sidebar,
            text="Registrar Entrada",
            command=lambda: self.controller.show_entrada_producto(),
        )

        self.btn_salida = ctk.CTkButton(
            self.sidebar,
            text="Registrar Salida",
            command=self.show_salida_producto_in_dashboard,
        )

        self.btn_inventario = ctk.CTkButton(
            self.sidebar,
            text="Inventario Completo",
            command=lambda: self.controller.show_inventario_completo(),
        )

        self.btn_logout = ctk.CTkButton(
            self.sidebar,
            text="Cerrar Sesión",
            command=lambda: self.controller.show_login(),
        )

        self.content_frame = ctk.CTkFrame(self)
        self.welcome_label = ctk.CTkLabel(
            self.content_frame,
            text="Bienvenido al Dashboard de Almacén",
            font=("Arial", 16),
        )

    def _setup_layout(self):
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.btn_gestion.pack(pady=5, fill="x")
        self.btn_entrada.pack(pady=5, fill="x")
        self.btn_salida.pack(pady=5, fill="x")
        self.btn_inventario.pack(pady=5, fill="x")
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

    def show_welcome_content(self):
        self._clear_content_frame()
        welcome_label = ctk.CTkLabel(
            self.content_frame,
            text="Biencenido al Dashboard de Almacén",
            font=("Arial", 16),
        )
        welcome_label.pack(pady=50)

    def show_salida_producto_in_dashboard(self):
        self._clear_content_frame()

        new_view = SalidaProductoWindow(self.content_frame, self.controller)
        self.current_content_view = new_view

        self.controller.root.title("Sistema de Inventario - Despacho de Ventas")