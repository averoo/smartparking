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


PENOMORAN ID MALL DIMULAI DARI 1
- Tidak ada lagi slot dummy ID 1-3.
- Mall pertama yang ditambahkan melalui menu Tambah Mall mendapat ID 1.
- Mall kedua mendapat ID 2, dan seterusnya.
- scanner_config.py secara default memakai MALL_ID = 1.
- Jika memakai database dari versi sebelumnya yang masih berisi slot dummy
  ID 1-3 dan mall operasional mulai ID 4, buat salinan cadangan lalu pindahkan
  file smartpark_terpusat.db lama keluar dari folder proyek sebelum menjalankan
  versi ini. Database baru akan dibuat dan penomoran dimulai lagi dari 1.
- PERHATIAN: memulai database baru berarti data kendaraan, pengguna, mall,
  dan riwayat transaksi di database lama tidak ikut terbawa. Simpan file lama
  sebagai cadangan jika data tersebut masih diperlukan.
