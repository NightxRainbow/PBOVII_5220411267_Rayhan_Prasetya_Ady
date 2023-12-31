class Rapor:
    def __init__(self, nama_siswa, nilai_semester_1):
        self.nama_siswa = nama_siswa
        self._nilai_semester_1 = nilai_semester_1

    def hitung_nilai(self):
        return self._nilai_semester_1


class NilaiPengetahuan(Rapor):
    def __init__(self, nama_siswa, nilai_semester_1, nilai_pengetahuan):
        super().__init__(nama_siswa, nilai_semester_1)
        self._nilai_p = nilai_pengetahuan

    def hitung_nilai(self):
        return (self._nilai_semester_1 + self._nilai_p)
        #max 50
        
class Detail(NilaiPengetahuan):
    def __init__(self, nama_siswa, nilai_semester_1, nilai_pengetahuan, nilai_praktikum):
        super().__init__(nama_siswa, nilai_semester_1, nilai_pengetahuan)
        self.__nilai_praktikum = nilai_praktikum

    def hitung_nilaiPengetahuan(self):
        nilai_psem1 = super().hitung_nilai()
        gabungan_p = (self.__nilai_praktikum + nilai_psem1) / 2
        return gabungan_p
    #max 50
    def cek_kelulusan(self):
        if self.hitung_nilai() >= 60:
            return "LULUS"
        else:
            return "TIDAK LULUS"
        
class NilaiKeterampilan(Rapor):
    def __init__(self, nama_siswa, nilai_semester_1, _nilai_k):
        super().__init__(nama_siswa, nilai_semester_1)
        self._nilai_k = _nilai_k

    def hitung_nilai(self):
        return (self._nilai_semester_1 + self._nilai_k) / 2
        #max 100
    def cek_lulus(self):
        if self.hitung_nilai() >= 60:
            return "LULUS"
        else:
            return "TIDAK LULUS"


detail_rapor = Detail("Halim", 50, 50, 50)
detail_keterampilan = NilaiKeterampilan("Halim", 100, 100)
print(f"Nama Siswa: {detail_rapor.nama_siswa}")
print(f"Nilai Pengatahuan: {detail_rapor.hitung_nilai()}")
print(f"Status Kelulusan: {detail_rapor.cek_kelulusan()}")
print(f"Nilai Keterampilan: {detail_keterampilan.hitung_nilai()}")
print(f"Prestasi: {detail_keterampilan.cek_lulus()}")

if detail_keterampilan.cek_lulus() == "LULUS" and detail_rapor.cek_kelulusan() == "LULUS":
    print("Selamat, Anda LULUS")
else:
    print("Maaf, Anda TIDAK LULUS")