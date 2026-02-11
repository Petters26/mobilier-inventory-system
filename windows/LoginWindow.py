import os
from dotenv import load_dotenv
import customtkinter as ctk

load_dotenv()


class LoginWindow(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True, padx=20, pady=20)

        self._create_widgets()
        self._setup_layout()

    def _create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Inicio de Sesión", font=("Arial", 20))
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Usuario")
        self.password_entry = ctk.CTkEntry(
            self, placeholder_text="Contraseña", show="*"
        )
        self.login_button = ctk.CTkButton(
            self, text="Iniciar Sesión", command=self._on_login
        )
        self.error_label = ctk.CTkLabel(self, text="", text_color="red")

    def _setup_layout(self):
        self.label.pack(pady=20)
        self.username_entry.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.login_button.pack(pady=20)
        self.error_label.pack()

    def _on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == os.getenv("USER_ALMACEN") and password == os.getenv("PASS_ALMACEN"):
            self.controller.show_almacen_dashboard()
        elif username == os.getenv("USER_VENTAS") and password == os.getenv("PASS_VENTAS"):
            self.controller.show_ventas_dashboard()
        else:
            self.error_label.configure(text="Credenciales incorrectas")
