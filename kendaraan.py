
class Kendaraan:
    def __init__(self, id_qr, nama_pengguna, email,
                 nomor_polisi, jenis):
        self.__id_qr = id_qr
        self.__nama_pengguna = nama_pengguna
        self.__email = email
        self.__nomor_polisi = nomor_polisi
        self.__jenis = jenis

    @property
    def id_qr(self):
        return self.__id_qr

    @property
    def nama_pengguna(self):
        return self.__nama_pengguna

    @property
    def email(self):
        return self.__email

    @property
    def nomor_polisi(self):
        return self.__nomor_polisi

    @property
    def jenis(self):
        return self.__jenis

    def tampilkan_info(self):
        print("\n--- DATA KENDARAAN ---")
        print("Nama         :", self.nama_pengguna)
        print("Email        :", self.email)
        print("Nomor Polisi :", self.nomor_polisi)
        print("Jenis        :", self.jenis)
        print("ID QR        :", self.id_qr)
