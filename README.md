# SMARTPARK TERPUSAT - SCANNER LOKASI OTOMATIS

1. Buka folder proyek ini di VS Code.
2. Jalankan: python -m pip install -r requirements.txt
3. Tambahkan mall operasional pertama melalui menu 7 (ID otomatis mulai 4).
4. Edit scanner_config.py, misalnya MALL_ID = 4.
5. Jalankan: python main.py
6. Registrasikan kendaraan (menu 1), lalu lakukan scan masuk (menu 2).
7. Scan keluar (menu 3) dan konfirmasi simulasi pembayaran.
8. Untuk mencoba mall berikutnya, keluar dari program, ubah MALL_ID
   menjadi ID mall kedua, lalu jalankan kembali python main.py.
9. QR kendaraan yang sama dapat dipakai di semua mall.

PENYIMPANAN
- Semua mall dalam simulasi satu laptop memakai smartpark_terpusat.db.
- QR disimpan di qr_kendaraan/.
- Untuk melanjutkan data lama, salin smartpark_terpusat.db dari proyek
  sebelumnya ke folder ini sebelum menjalankan program.
- Jangan menimpa database lama tanpa membuat cadangan terlebih dahulu.
- ID 1-3 dicadangkan untuk dummy, mall operasional mulai ID 4.
- Mall yang pernah dipakai transaksi tidak dapat dihapus.
- Pembayaran QRIS dan E-Money masih simulasi.
- Ini bukan sistem multi-laptop real-time; untuk penggunaan nyata gunakan
  API server dan database terpusat dengan autentikasi perangkat.



