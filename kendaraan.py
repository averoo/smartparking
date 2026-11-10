class Kendaraan:
    def __init__(self, id_qr, nomor_polisi, jenis):
        self.__id_qr = id_qr
        self.__nomor_polisi = nomor_polisi.upper().strip()
        self.__jenis = jenis

    @property
    def id_qr(self):
        return self.__id_qr

    @property
    def nomor_polisi(self):
        return self.__nomor_polisi

    @property
    def jenis(self):
        return self.__jenis
