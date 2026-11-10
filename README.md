# smartparking

1. Ekstrak folder proyek.
2. Buka folder SmartPark_Terpusat di Visual Studio Code.
3. Buka Terminal > New Terminal.
4. Instal dependensi:
   python -m pip install -r requirements.txt
5. Jalankan:
   python main.py

DATABASE
- Database dibuat otomatis sebagai smartpark_terpusat.db.
- Semua mall dalam aplikasi ini menggunakan satu database yang sama.
- QR kendaraan dibuat di folder qr_kendaraan.
- Jangan menghapus file database jika ingin mempertahankan riwayat.

SIMULASI MULTI-MALL
- Menu masuk dan keluar meminta pilihan mall.
- Registrasikan kendaraan sekali.
- Gunakan QR/ID QR yang sama saat transaksi di mall berbeda.
- Dalam contoh ini kendaraan harus keluar dari mall tempat transaksi masuk.
  Setelah transaksi lunas, kendaraan dapat masuk ke mall lain.

PENTING UNTUK PENGGUNAAN NYATA
- Ini adalah prototipe lokal. Jika beberapa komputer fisik di mall berbeda
  harus mengakses data yang sama melalui internet, SQLite lokal tidak cukup.
  Gunakan server database terpusat (misalnya PostgreSQL) dan API backend.
- Pembayaran QRIS/E-Money pada kode ini masih simulasi, bukan transaksi asli.
- QR code sendiri dapat disalin; sistem produksi perlu validasi server,
  kontrol akses, dan mekanisme anti-penyalahgunaan.


MENGHAPUS MALL
- Pilih menu 8. Hapus mall.
- Masukkan ID mall yang ingin dihapus, lalu konfirmasi dengan y.
- Mall yang sudah digunakan dalam transaksi tidak dapat dihapus,
  agar riwayat parkir tetap utuh. Untuk mall tersebut, biarkan tetap
  tercatat atau gunakan pengembangan fitur nonaktifkan mall.

