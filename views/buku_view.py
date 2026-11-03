import tkinter as tk
# Jika Anda menggunakan CustomTkinter, gunakan baris di bawah ini:
# import customtkinter as ctk

class BukuView:
    def __init__(self, root, current_user, login_window=None, controller=None):
        self.root = root
        self.current_user = current_user
        self.login_window = login_window
        self.controller = controller # Menampung parameter controller agar tidak error
        
        # Konfigurasi jendela dasar (sesuaikan dengan kode yang sudah ada)
        self.root.title("Manajemen Buku - Perpustakaan")
        self.root.geometry("600x400")

        # ==========================================
        # INISIALISASI WIDGET / KOMPONEN YANG SUDAH ADA
        # ==========================================
        # Contoh Label Judul
        self.lbl_title = tk.Label(self.root, text="Form Manajemen Buku", font=("Arial", 16, "bold"))
        self.lbl_title.pack(pady=10)

        # Contoh Tombol Update (sesuaikan dengan widget Anda sebelumnya)
        self.btn_update = tk.Button(self.root, text="Perbarui Data (Update)", command=self.update_data, width=25)
        self.btn_update.pack(pady=5)

        # Contoh Tombol Delete (sesuaikan dengan widget Anda sebelumnya)
        self.btn_delete = tk.Button(self.root, text="Hapus Data (Delete)", command=self.delete_data, width=25, bg="orange", fg="black")
        self.btn_delete.pack(pady=5)

        # ==========================================
        # 1. PENERAPAN NOMOR 2: ATURAN OTORISASI ROLE
        # ==========================================
        # Jika role pengguna yang login adalah 'anggota', kunci tombol Update & Delete
        if self.current_user and self.current_user.get('role') == 'anggota':
            self.btn_update.configure(state="disabled")
            self.btn_delete.configure(state="disabled")

        # ==========================================
        # 2. PENERAPAN NOMOR 3: TOMBOL LOGOUT
        # ==========================================
        self.btn_logout = tk.Button(self.root, text="Logout", command=self.logout, width=25, bg="red", fg="white")
        self.btn_logout.pack(pady=20)

    # Contoh fungsi dasar untuk tombol Update
    def update_data(self):
        print("Fungsi Perbarui Data dijalankan.")
        # Masukkan logika update Anda di sini

    # Contoh fungsi dasar untuk tombol Delete
    def delete_data(self):
        print("Fungsi Hapus Data dijalankan.")
        # Masukkan logika delete Anda di sini

    # ==========================================
    # FUNGSI LOGOUT (UNTUK NOMOR 3)
    # ==========================================
    def logout(self):
        # Menutup jendela Buku/Perpustakaan saat ini
        self.root.destroy()
        
        # Membuka kembali jendela Login yang sebelumnya disembunyikan
        if self.login_window:
            self.login_window.deiconify() # Mengaktifkan dan memunculkan kembali jendela login