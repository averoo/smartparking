from pathlib import Path
import qrcode

BASE_DIR = Path(__file__).resolve().parent
QR_DIR = BASE_DIR / "qr_kendaraan"
QR_DIR.mkdir(exist_ok=True)


def buat_qr(id_qr):
    lokasi = QR_DIR / f"{id_qr}.png"

    gambar = qrcode.make(id_qr)
    gambar.save(lokasi)

    return lokasi
