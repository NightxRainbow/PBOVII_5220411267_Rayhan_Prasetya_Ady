class PerpusItem:
    def __init__(self,Judul, Subjek):
        self.Judul = Judul
        self.Subjek = Subjek
        
    def LokasiPenyimpanan(Judul,Subjek):
        print("judul buku ;",Judul,"Subjek buku",Subjek)
        
    def info(Judul):
        print("Judul buku =",Judul,"ada")
    
class Buku(PerpusItem):
    def __init__(self,Judul,Subjek,ISBN,Pengarangs,jmlHal,ukuran):
        super().__init__(Judul,Subjek)
        self.ISBN = ISBN
        self.Pengarangs = Pengarangs
        self.jmlHal = jmlHal
        self.ukuran = ukuran
        
    def info(Judul,Subjek,ISBN,Pengarangs,jmlHal,ukuran):
        print("Judul Buku:",Judul,",Subjek:",Subjek,",ISBN:",ISBN,",Pengarang :",Pengarangs,",Jumlah Halaman:",jmlHal,",Ukuran",ukuran)

class MaJalah(PerpusItem):
    def __init__(self, Judul, Subjek, volume, issue):
        super().__init__(Judul, Subjek)
        self.volume = volume
        self.issue = issue
    
    def info(Judul, Subjek, volume,issue):
        print("Judul Buku:",Judul,",Subjek:",Subjek, ",Volume:",volume,",Isu:",issue)
    
class DVD(PerpusItem):
    def __init__(self, Judul, Subjek, Aktor, Genre):
        super().__init__(Judul, Subjek)
        self.Aktor= Aktor
        self.Genre = Genre
    
    def info(Judul,Subjek,Aktor,Genre):
        print("Judul Buku:",Judul,",Subjek:",Subjek,",Aktor:",Aktor,",Genre:",Genre)

class Pengarang:
    def __init__(self,nama):
        self.nama = nama 
        
    def info(Judul, nama):
        print("Judul",Judul,",Nama Pengarang:", nama)
    
    def cari(nama,Judul):
        print("Pengarang: ",nama,",Bukunya: ",Judul)

class Katalog:
    def __init__(self, PerpusItem):
        self.PerpusItem = PerpusItem
    def Cari(Judul,Subjek):
        print("Nama Judul:",Judul,",Subjek",Subjek)

class Pencarian:
    def __init__(self, PerpusItem):
        self.PerpusItem = PerpusItem
        
informasi = PerpusItem("Hitam", "Horor")    
Informasi1 = Katalog
Informasi1.Cari("Hitam","Horor") 
print("="*30)
Informasi2 = Pengarang
Informasi2.cari("Syahrul","Hitam")
print("="*30)
Informasi3 = DVD
Informasi3.info("Hitam Banget","Horor","Brandon Curington","Horor")
print("="*30)
Informasi4 = MaJalah
Informasi4.info("Hitam Banget","Horor","1","Orang Hitam")
print("="*30)
Informasi5 = Buku
Informasi5.info("Hitam Banget","Horor","243","Syahrul","120","A4")
print("="*30)
cari1 = Pencarian(informasi)
            
    