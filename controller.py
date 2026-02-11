import customtkinter as ctk
from windows.LoginWindow import LoginWindow
from windows.AlmacenDashboard import AlmacenDashboard
from windows.VentasDashboard import VentasDashboard
from windows.GestionProductosWindow import GestionProductosWindow
from windows.EntradaProductoWindow import EntradaProductoWindow
from windows.SalidaProductoWindow import SalidaProductoWindow
from windows.InventarioCompletoWindow import InventarioCompletoWindow
from windows.ConsultaExistenciaWindow import ConsultaExistenciaWindow
from windows.ConsultaExistenciaSearchView import ConsultaExistenciaSearchView
from windows.CrearSolicitudVentaWindow import CrearSolicitudVentaWindow
from windows.MisVentasWindow import MisVentasWindow


class AppController:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.user_role = None
        self.user_data = None

    def _show_main_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        new_frame = frame_class(self.root, self)
        self.current_frame = new_frame
        
    def show_login(self):
        self.root.title("Sistema de Inventario - Login")
        self._show_main_frame(LoginWindow)


    def show_almacen_dashboard(self):
        self.user_role = "almacen"
        self.root.title("Sistema de Inventario - Dashboard Almacén")
        self._show_main_frame(AlmacenDashboard)

    def show_ventas_dashboard(self):
        self.user_role = "ventas"
        self.root.title("Sistema de Inventario - Dashboard Ventas")
        self._show_main_frame(VentasDashboard)

    def show_gestion_productos(self):
        self.root.title("Sistema de Inventario - Gestión de Productos")
        self._show_main_frame(GestionProductosWindow)

    def show_entrada_producto(self):
        self.root.title("Sistema de Inventario - Registro de Entrada")
        self._show_main_frame(EntradaProductoWindow)

    def show_inventario_completo(self):
        self.root.title("Sistema de Inventario - Inventario Completo")
        self._show_main_frame(InventarioCompletoWindow)

    def show_crear_solicitud_venta(self):
        self.root.title("Sistema de Inventario - Nueva Solicitud de Venta")
        self._show_main_frame(CrearSolicitudVentaWindow)

    def show_mis_ventas(self):
        self.root.title("Sistema de Inventario - Mis Solicitudes de Venta")
        self._show_main_frame(MisVentasWindow)

    def show_results_popup(self,results):

        results_window = ConsultaExistenciaWindow(self.root, self, search_results=results)
        results_window.focus_set()

    def back_to_dashboard(self):
        if self.user_role == "almacen":
            if isinstance(self.current_frame, AlmacenDashboard):
                self.current_frame.show_welcome_content()
                self.root.title("Sistema de Inventario - Dashboard Almacén")
            else:
                self.show_almacen_dashboard()
        elif self.user_role == "ventas":
            if isinstance(self.current_frame, VentasDashboard):
                self.current_frame.show_consulta_existencia_search_view()
                self.root.title("Sistema de Inventario - Dashboard Ventas")
            else:
                self.show_ventas_dashboard()

    def quit_app(self):
        self.root.destroy()
