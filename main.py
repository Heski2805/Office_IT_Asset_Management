import json 
import os
file_path = os.path.join(os.path.dirname(__file__), "data_aset.json")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data_aset = json.load(file)

except FileNotFoundError:
    print("File data_aset.json tidak ditemukan!")
    data_aset = []

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data_aset, file, indent=4)

except json.JSONDecodeError:
    print("File data_aset.json tidak valid!")
    data_aset = []

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
        break

# Untuk menambahkan aset baru
    elif pilihan == 1:
        while True:
            try:
                id_aset = int(input("Masukkan ID aset : "))
                id_ditemukan = False
                
            except ValueError:
                print("ID harus berupa angka, coba lagi.")
                continue

            for barang in data_aset:

                if barang["id"] == id_aset:
                    id_ditemukan = True
                    print("ID aset sudah ada, silakan masukkan ID yang lain.")
                    break
            if id_ditemukan:
                continue
            else:
                break

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


        data_aset.append({
            "id": id_aset,
            "nama": nama,
            "harga": harga,
            "stok": stok,
            "status": status,
            "lokasi": lokasi
        })
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data_aset, file, indent=4)
        print("Aset berhasil ditambahkan!")

# Untuk mencari aset berdasarkan ID
    elif pilihan == 2:
        while True:
            try:
                id_cari = int(input("Masukkan ID yang ingin dicari: "))

            except ValueError:
                print("ID harus berupa angka, coba lagi.")
                continue

            break

        id_ditemukan = False

        for barang in data_aset:
             if barang["id"] == id_cari:
                  id_ditemukan = True
                  print("Aset ditemukan!\n")
                  print("ID:", barang["id"])
                  print("Nama:", barang["nama"])
                  print("Harga:", barang["harga"])
                  print("Stok:", barang["stok"])
                  print("Status:", barang["status"])
                  print("Lokasi:", barang["lokasi"])
                  break
        if not id_ditemukan:
            print("Aset tidak ditemukan.")
            
# Untuk mengubah stok aset
    elif pilihan == 3:
        while True:
            try:
                id_update = int(input("Masukkan ID aset yang ingin diubah: "))

            except ValueError:
                print("ID harus berupa angka, coba lagi.")
                continue
            
            break 

        id_ditemukan = False

        for barang in data_aset:
            if barang["id"] == id_update:
                id_ditemukan = True
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

                barang["stok"] = stok_baru
                print("Stok berhasil diperbarui!")
                print("Stok sekarang:", barang["stok"])
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data_aset, file, indent=4)
                break
        if not id_ditemukan:
            print("Aset tidak ditemukan!")

# Untuk menghapus aset
    elif pilihan == 4:
        while True:
            try:
                id_hapus = int(input("Masukkan ID aset yang ingin dihapus: "))

            except ValueError:
                print("ID harus berupa angka, coba lagi.")
                continue
                    
            break

        id_ditemukan = False

        for barang in data_aset:
            if barang["id"] == id_hapus:
                id_ditemukan = True
                data_aset.remove(barang)
                print("Aset berhasil dihapus!")
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data_aset, file, indent=4)
                break
        if not id_ditemukan:
            print("Aset tidak ditemukan!")


# Untuk menampilkan semua aset
    elif pilihan == 5:
        print("\n=== OFFICE IT ASSET MANAGEMENT ===\n")

        if not data_aset:
            print("Belum ada aset yang terdaftar.")

        else:
            for barang in data_aset:
                    print("ID:", barang["id"])
                    print("Nama:", barang["nama"])
                    print("Harga:", barang["harga"])
                    print("Stok:", barang["stok"])
                    print("Status:", barang["status"])
                    print("Lokasi:", barang["lokasi"])
                    print("\n------------------------")