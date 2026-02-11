import customtkinter as ctk
from tkinter import ttk

class SalidaProductoWindow(ctk.CTkFrame):
    def __init__(self, master_frame, controller_instance):
        super().__init__(master_frame)
        self.controller = controller_instance

        self.pack(fill="both", expand=True)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)


        self.tabview = ctk.CTkTabview(self.main_frame)
        self.tabview.pack(fill="both", expand=True)

        self.tab_pendientes = self.tabview.add("Solicitudes Pendientes")
        self.tab_historial = self.tabview.add("Historial de Despachos")



        self.pending_frame = ctk.CTkFrame(self.tab_pendientes)
        self.pending_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.pending_tree = ttk.Treeview(self.pending_frame, columns=("producto", "cantidad", "fecha", "estado"), show="headings")
        for col, title in zip(("producto", "cantidad", "fecha", "estado"), ("Producto", "Cantidad", "Fecha", "Estado")):
            self.pending_tree.heading(col, text=title)
            self.pending_tree.column(col, anchor="center", width=180)

        self.pending_tree.pack(fill="both", expand=True)



        self.history_frame = ctk.CTkFrame(self.tab_historial)
        self.history_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.history_tree = ttk.Treeview(self.history_frame, columns=("producto", "cantidad", "fecha", "despachador"), show="headings")
        for col, title in zip(("producto", "cantidad", "fecha", "despachador"), ("Producto", "Cantidad", "Fecha", "Despachador")):
            self.history_tree.heading(col, text=title)
            self.history_tree.column(col, anchor="center", width=180)

        self.history_tree.pack(fill="both", expand=True)



        self.btn_back = ctk.CTkButton(self.main_frame, text="Volver", command=self.controller.back_to_dashboard)
        self.btn_back.pack(pady=10)
