import json
import qrcode
from config import QR_DIR

def buat_qr(id_qr, nomor_polisi, jenis):
    QR_DIR.mkdir(parents=True, exist_ok=True)
    # QR berisi identitas kendaraan, bukan data pribadi pemilik.
    payload = {
        "app": "SmartPark",
        "version": 1,
        "vehicle_id": id_qr,
        "plate": nomor_polisi.upper(),
        "type": jenis
    }
    gambar = qrcode.make(json.dumps(payload, separators=(",", ":")))
    path = QR_DIR / f"{id_qr}.png"
    gambar.save(path)
    return path

def baca_payload_qr(teks):
    try:
        data = json.loads(teks)
        if data.get("app") != "SmartPark" or data.get("version") != 1:
            return None
        if not all(data.get(k) for k in ("vehicle_id", "plate", "type")):
            return None
        if data["type"] not in ("Motor", "Mobil"):
            return None
        return data
    except (ValueError, TypeError, AttributeError):
        return None
