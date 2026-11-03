from views.login_view import LoginView
from views.buku_view import BukuView
from controllers.buku_controller import BukuController
from models.buku_model import BukuModel
from models.user_model import UserModel
from tkinter import messagebox

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.login_view = None
        self.buku_view = None

    def show_login(self):
        self.login_view = LoginView(self)
        self.login_view.mainloop()

    def login(self, username, password):
        user = self.model.autentikasi(username, password)
        if user:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {user['username']}! (Role: {user['role']})")
            
            if self.login_view:
                self.login_view.destroy()

            # 1. Inisialisasi BukuView dengan menambahkan parameter root/controller yang sesuai
            # Pastikan BukuView menerima argumen controller dan current_user
            import customtkinter as ctk # Sesuaikan jika menggunakan tk.Tk() atau Toplevel()
            self.buku_root = ctk.CTk() # Atau Toplevel tergantung arsitektur root utama Anda
            self.buku_view = BukuView(root=self.buku_root, controller=self, current_user=user, login_view=None)
            
            # 2. Inisialisasi BukuModel
            buku_model = BukuModel()

            # 3. Hubungkan BukuController dengan BukuView dan BukuModel
            self.buku_controller = BukuController(view=self.buku_view, model=buku_model)

            self.buku_view.mainloop()
        else:
            if self.login_view:
                self.login_view.show_error("Username atau Password salah!")