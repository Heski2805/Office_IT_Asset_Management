import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="latihan_mysql"
        )

        print("Koneksi database berhasil!")
        return db

    except mysql.connector.Error as err:
        print(f"Gagal menghubungkan database: {err}")
        return None

db = connect_db()

if db is None:
    print("Aplikasi tidak dapat dijalankan karena koneksi database gagal.")
    raise SystemExit(1)

while True:
    print("\n=== OFFICE IT ASSET MANAGEMENT ===")
    print("1. Add Asset")
    print("2. Search Asset")
    print("3. Update Asset")
    print("4. Delete Asset")
    print("5. View All Assets")
    print("6. Exit")

# Validasi Menu Pilihan
    while True:
        try:
            pilihan = int(input("Masukkan pilihan menu (1-6): "))
            if pilihan < 1 or pilihan > 6:
                print("Pilihan tidak valid, silakan masukkan angka antara 1 hingga 6.")
                continue

            break
        except ValueError:
            print("Input harus berupa angka!, coba lagi.")

# Untuk keluar menu
    if pilihan == 6:
        print("Terima kasih telah menggunakan aplikasi!")

        if db and db.is_connected():
            db.close()
            print("Koneksi database ditutup.")

        break

# Untuk menambahkan aset baru
    elif pilihan == 1:

        while True:
            nama = input("Masukkan nama aset : ")
            if nama.strip() == "":
                print("Nama Barang tidak boleh kosong!, silahkan masukkan nama yang valid.")
                continue

            break

        nama = nama.strip()

        while True:
            try:
                harga = int(input("Masukkan harga aset : "))

                if harga < 0:
                    print("Harga tidak boleh negatif!, silakan masukkan harga yang valid.")
                    continue

                break

            except ValueError:
                print("Input harus berupa angka!, coba lagi.")

        while True:
            try:
                stok = int(input("Masukkan stok aset : "))

                if stok < 0:
                    print("Stok tidak boleh negatif!, silakan masukkan stok yang valid.")
                    continue

                break

            except ValueError:
                print("Input harus berupa angka!, coba lagi.")

        while True:
            try:
                print("\n=== PILIH STATUS ASET ===")
                print("1. Available")
                print("2. In Use")
                print("3. Maintenance")
                print("4. Not Available")

                pilihan_status = int(input("Pilih status aset (1-4): "))

                if pilihan_status == 1:
                    status = "Available"
                elif pilihan_status == 2:
                    status = "In Use"
                elif pilihan_status == 3:
                    status = "Maintenance"
                elif pilihan_status == 4:
                    status = "Not Available"
                else:
                    print("Pilihan tidak valid, masukkan angka 1-4.")
                    continue

                break

            except ValueError:
                print("Input harus berupa angka!, coba lagi.")

        while True:
            lokasi = input("Masukkan lokasi aset : ")
            if lokasi.strip() == "":
                print("Lokasi tidak boleh kosong!, silakan masukkan lokasi yang valid.")
                continue

            break

        lokasi = lokasi.strip()

        cursor = db.cursor()

        query = """
            INSERT INTO assets (nama, harga, stok, status, lokasi)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (nama, harga, stok, status, lokasi)
        try:
            cursor.execute(query, values)
            db.commit()

            print("Aset berhasil ditambahkan!")
            print("ID aset:", cursor.lastrowid)

        except mysql.connector.Error as err:
            db.rollback()
            print(f"Gagal menambahkan aset: {err}")

        finally:
            cursor.close()

# Untuk mencari aset berdasarkan ID
    elif pilihan == 2:
        while True:
            try:
                id_cari = int(input("Masukkan ID yang ingin dicari: "))

            except ValueError:
                print("ID harus berupa angka, coba lagi.")
                continue

            break

        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT * FROM assets WHERE id = %s",
                (id_cari,)
            )

            barang = cursor.fetchone()

            if barang:
                print("Aset ditemukan!\n")
                print("ID:", barang["id"])
                print("Nama:", barang["nama"])
                print("Harga:", barang["harga"])
                print("Stok:", barang["stok"])
                print("Status:", barang["status"])
                print("Lokasi:", barang["lokasi"])
            else:
                print("Aset tidak ditemukan.")
        except mysql.connector.Error as err:
            print(f"Gagal mencari aset: {err}")

        finally:
            cursor.close()
            
# Untuk mengubah stok aset
    elif pilihan == 3:
        while True:
            try:
                id_update = int(input("Masukkan ID aset yang ingin diubah: "))

            except ValueError:
                print("ID harus berupa angka, coba lagi.")
                continue
            
            break 

        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT * FROM assets WHERE id = %s",
                (id_update,)
            )

            barang = cursor.fetchone()

            if barang:
                print("Aset ditemukan!\n")
                print("ID:", barang["id"])
                print("Nama:", barang["nama"])
                print("Harga:", barang["harga"])
                print("Stok:", barang["stok"])
                print("Status:", barang["status"])
                print("Lokasi:", barang["lokasi"])

                while True:
                    try:
                        stok_baru = int(input("Masukkan stok baru: "))

                        if stok_baru < 0:
                            print("Stok tidak boleh negatif!")
                            continue

                        break

                    except ValueError:
                        print("Stok harus berupa angka!")
                        continue

                cursor.execute(
                    "UPDATE assets SET stok = %s WHERE id = %s",
                    (stok_baru, id_update)
                )

                db.commit()

                print("Stok berhasil diperbarui!")
                print("Stok sekarang:", stok_baru)

            else:
                print("Aset tidak ditemukan!")

        except mysql.connector.Error as err:
            db.rollback()
            print(f"Gagal memperbarui aset: {err}")
        finally:
            cursor.close()

# Untuk menghapus aset
    elif pilihan == 4:
        while True:
            try:
                id_hapus = int(input("Masukkan ID aset yang ingin dihapus: "))

            except ValueError:
                print("ID harus berupa angka, coba lagi.")
                continue

            break

        cursor = db.cursor(dictionary=True)

        try:
            # Mencari aset berdasarkan ID
            cursor.execute(
                "SELECT * FROM assets WHERE id = %s",
                (id_hapus,)
            )

            aset = cursor.fetchone()

            if aset is None:
                print("Aset tidak ditemukan!")

            else:
                print("\nAset ditemukan!")
                print("ID     :", aset["id"])
                print("Nama   :", aset["nama"])
                print("Harga  :", aset["harga"])
                print("Stok   :", aset["stok"])
                print("Status :", aset["status"])
                print("Lokasi :", aset["lokasi"])

                while True:
                    konfirmasi = input(
                        "\nApakah kamu yakin ingin menghapus aset ini? (Y/N): "
                    ).strip().upper()

                    if konfirmasi == "Y":
                        cursor.execute(
                            "DELETE FROM assets WHERE id = %s",
                            (id_hapus,)
                        )

                        db.commit()
                        print("Aset berhasil dihapus!")
                        break

                    elif konfirmasi == "N":
                        print("Penghapusan aset dibatalkan.")
                        break

                    else:
                        print("Input tidak valid! Masukkan Y atau N.")

        except mysql.connector.Error as err:
            db.rollback()
            print(f"Gagal menghapus aset: {err}")

        finally:
            cursor.close()

# Untuk menampilkan semua aset
    elif pilihan == 5:
        print("\n=== OFFICE IT ASSET MANAGEMENT ===\n")

        cursor = None

        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM assets")
            hasil_aset = cursor.fetchall()

            if not hasil_aset:
                print("Belum ada aset yang terdaftar.")

            else:
                for barang in hasil_aset:
                        print("ID:", barang["id"])
                        print("Nama:", barang["nama"])
                        print("Harga:", barang["harga"])
                        print("Stok:", barang["stok"])
                        print("Status:", barang["status"])
                        print("Lokasi:", barang["lokasi"])
                        print("\n------------------------")

        except mysql.connector.Error as err:
            print(f"Gagal menampilkan aset: {err}")
        
        finally:
            if cursor is not None:
                cursor.close()