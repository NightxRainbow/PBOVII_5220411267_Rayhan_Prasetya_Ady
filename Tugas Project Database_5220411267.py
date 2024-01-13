import mysql.connector
from prettytable import PrettyTable

class Database:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            self.conn.commit()
            print("Berhasil menjalankan query")
        except Exception :
            print(f"Gagal menjalankan query: {Exception}, ulangi lagi")
            self.conn.rollback()

    def close_connection(self):
        self.conn.close()

class Komik(Database):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insert_data(self, kode_komik, nama_komik, jenis_komik, penulis, penerbit):
        query = "INSERT INTO indeks (kode_komik, nama_komik, jenis_komik, penulis, penerbit) VALUES (%s, %s, %s, %s, %s)"
        data = (kode_komik, nama_komik, jenis_komik, penulis, penerbit)
        self.execute_query(query, data)

    def update_data(self, kode_komik, nama_komik, jenis_komik, penulis, penerbit):
        query = "UPDATE indeks SET nama_komik=%s, jenis_komik=%s, penulis=%s, penerbit=%s WHERE kode_komik=%s"
        data = (nama_komik, jenis_komik, penulis, penerbit, kode_komik)
        self.execute_query(query, data)

    def delete_data(self, kode_komik):
        query = "DELETE FROM indeks WHERE kode_komik=%s"
        data = (kode_komik,)
        self.execute_query(query, data)

    def display_data(self):
        query = "SELECT * FROM indeks"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        table = PrettyTable(["Kode Komik", "Nama Komik", "Jenis Komik", "Penulis", "Penerbit"])
        for row in result:
            table.add_row(row)
        print(table)

class Penjualan(Database):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insert_data(self, harga_komik, stok_komik):
        query = "INSERT INTO penjualan (harga_komik, stok_komik) VALUES (%s, %s)"
        data = (harga_komik, stok_komik)
        self.execute_query(query, data)

    def update_data(self, harga_komik, stok_komik):
        query = "UPDATE penjualan SET stok_komik=%s WHERE harga_komik=%s"
        data = (stok_komik, harga_komik)
        self.execute_query(query, data)

    def delete_data(self, harga_komik):
        query = "DELETE FROM penjualan WHERE harga_komik=%s"
        data = (harga_komik,)
        self.execute_query(query, data)

    def display_data(self):
        query = """
        SELECT indeks.kode_komik, indeks.nama_komik, indeks.jenis_komik, indeks.penulis, indeks.penerbit,
               penjualan.harga_komik, penjualan.stok_komik
        FROM indeks
        INNER JOIN penjualan ON indeks.kode_komik = penjualan.kode_komik
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        table = PrettyTable(["Kode Komik", "Nama Komik", "Jenis Komik", "Penulis", "Penerbit", "Harga Komik", "Stok Komik"])
        for row in result:
            table.add_row(row)
        print(table)


def main():
    host = "localhost"
    user = "root"
    password = ""
    database = "5220411267"
    komik_db = Komik(host, user, password, database)
    penjualan_db = Penjualan(host, user, password, database)

    while True:
        print("\nMenu:")
        print("1. Create data komik")
        print("2. Update data komik")
        print("3. Delete data komik")
        print("4. Tampilkan data komik")
        print("5. Create data penjualan")
        print("6. Update data penjualan")
        print("7. Delete data penjualan")
        print("8. Tampilkan data penjualan")
        print("9. Exit")

        pilihan = input("Masukkan pilihan (1-10): ")

        if pilihan == "1":
            kode_komik = input("Masukkan kode komik: ")
            nama_komik = input("Masukkan nama komik: ")
            jenis_komik = input("Masukkan jenis komik: ")
            penulis = input("Masukkan penulis: ")
            penerbit = input("Masukkan penerbit: ")
            komik_db.insert_data(kode_komik, nama_komik, jenis_komik, penulis, penerbit)
        elif pilihan == "2":
            kode_komik = input("Update kode komik yang akan diupdate: ")
            nama_komik = input("Update nama komik baru: ")
            jenis_komik = input("Update jenis komik baru: ")
            penulis = input("Update penulis baru: ")
            penerbit = input("Update penerbit baru: ")
            komik_db.update_data(kode_komik, nama_komik, jenis_komik, penulis, penerbit)
        elif pilihan == "3":
            kode_komik = input("Masukan kode komik yang akan dihapus: ")
            komik_db.delete_data(kode_komik)
        elif pilihan == "4":
            print("Data pada tabel komik:")
            komik_db.display_data()
        elif pilihan == "5":
            harga_komik = float(input("Input harga komik: "))
            stok_komik = int(input("Input stok komik: "))
            penjualan_db.insert_data(harga_komik, stok_komik)
        elif pilihan == "6":
            harga_komik = float(input("Update stok dari harga komik: "))
            stok_komik = int(input("Update stok komik baru: "))
            penjualan_db.update_data(harga_komik, stok_komik)
        elif pilihan == "7":
            harga_komik = float(input("Masukan harga komik yang akan dihapus: "))
            penjualan_db.delete_data(harga_komik)
        elif pilihan == "8":
            print("Tabel Penjualan Komik:")
            penjualan_db.display_data()
        elif pilihan == "9":
            break
        else:
            print("Pilihan yang diinputkan tidak ada.")

    komik_db.close_connection()
    penjualan_db.close_connection()

if __name__ == "__main__":
    main()
