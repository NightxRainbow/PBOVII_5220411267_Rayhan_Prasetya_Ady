class Animal:
    def __init__(self, nama, sifat, size, legs):
        self.nama = nama
        self.sifat = sifat
        self.size = size
        self.legs = legs

class Mamalia(Animal):
    def __init__(self, nama, sifat, size, legs, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, size, legs)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

class Aves(Animal):
    def __init__(self, nama, sifat, size, legs, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, size, legs)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

class Ayam(Aves):
    def __init__(self, nama, sifat, size, legs, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, size, legs, bisa_terbang, jenis_aves)
        self.__jenis_ayam = jenis_ayam
        self.__bisa_diadu = bisa_diadu

    def suara(self):
        print('Kukuruyuuuuukk !!!')
    
    def tampil(self):
        print('Nama: ', self.nama,"\n"'sifat:', self.sifat,"\n"'Size:', self.size,"\n"'legs:',self.legs,"\n"'Jenis Aves:',self.jenis_aves, "\n"'Terbang:', self.bisa_terbang,"\n"'Jenis Ayam:', self.__jenis_ayam,"\n"'DiaduP:', self.__bisa_diadu)

class Merpati(Aves):
    def __init__(self, nama, sifat, size, legs, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, size, legs, bisa_terbang, jenis_aves)
    
    def suara(self):
        print('Citcitcuuuit !!!')

    def tampil(self):
        print('Nama: ', self.nama ,"\n" 'sifat :', self.sifat,"\n" 'Size:', self.size, "\n" 'legs:',self.legs,"\n" 'Jenis Aves:',self.jenis_aves,"\n"'Terbang:', self.bisa_terbang)

print('='*45)
ayam_kampung = Ayam("Ayam Kampung", "Cocok untuk diadu", "Sedang", 2, 'Tidak Bisa', "Bertelur", "Kampung", "Bisa")
ayam_kampung.tampil()
print("suaranya :"),ayam_kampung.suara()
print('='*45)
merpati = Merpati("Merpati", "Bisa terbang tinggi", "Kecil", 2, "Bisa", "Bertelur")
merpati.tampil()
print("suaranya :"),merpati.suara()
print('='*45)