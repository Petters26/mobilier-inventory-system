import customtkinter as ctk
from controller import AppController


def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Sistema de Inventario - Prototipo")
    root.geometry("1000x700")
    root.minsize(800, 600)
    root.resizable(True, True)

    app = AppController(root)
    app.show_login()

    root.mainloop()


if __name__ == "__main__":
    main()
    