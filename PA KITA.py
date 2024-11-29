data_klien = {}

def menu():
    while True:
        print("\nMenu RentClothes: Aplikasi Penyewaan Baju Serba Ada")
        print("1. Tambah Data Pemesan")
        print("2. Tampilkan Data Pemesan yang Belum Dikembalikan")
        print("3. Total Harga Pesanan")
        print("4. Pembayaran")
        print("5. Pengembalian")
        print("6. Update Pesanan")
        print("7. Hapus Data Pemesan")
        print("8. Keluar")
        sub_menu = input("Pilih menu (1-8): ")

        if sub_menu == "1":
            print("\n1. Data Pemesan")
            nama = input("Masukkan nama klien: ")
            print("Pilih kategori baju: ")
            print("1. Adat")
            print("2. Pernikahan")
            print("3. Kebaya")
            kategori_pilihan = input("Masukkan nomor kategori (1-3): ")

            if kategori_pilihan == "1":
                kategori_baju = "adat"
            elif kategori_pilihan == "2":
                kategori_baju = "pernikahan"
            elif kategori_pilihan == "3":
                kategori_baju = "kebaya"
            else:
                print("Kategori tidak valid, silakan coba lagi.")
                continue

            jumlah_baju = int(input("Masukkan jumlah baju yang dipesan: "))
            pinjam_berapa_hari = int(input("Masukkan total peminjaman (hari): "))

            data_pesanan = {
                "nama": nama,
                "kategori baju": kategori_baju,
                "jumlah baju": jumlah_baju,
                "pinjam berapa hari": pinjam_berapa_hari,
                "member": False,
                "dikembalikan": False
            }

            if kategori_baju not in data_klien:
                data_klien[kategori_baju] = []

            data_klien[kategori_baju].append(data_pesanan)
            print("\nData pemesanan berhasil ditambahkan:")
            print(f"Nama          : {nama}")
            print(f"Kategori Baju : {kategori_baju}")
            print(f"Jumlah Baju   : {jumlah_baju}")
            print(f"Durasi Pinjam : {pinjam_berapa_hari} hari")

        elif sub_menu == "2":
            print("\n2. Tampilkan Data Pemesan yang Belum Dikembalikan")
            if data_klien:
                for kategori, daftar_pesanan in data_klien.items():
                    print(f"\nKategori Baju : {kategori}")
                    for pesanan in daftar_pesanan:
                        if not pesanan["dikembalikan"]:
                            print(f"Nama          : {pesanan['nama']}")
                            print(f"Jumlah Baju   : {pesanan['jumlah baju']}")
                            print(f"Durasi Pinjam : {pesanan['pinjam berapa hari']} hari")
            else:
                print("Tidak ada data yang ditemukan.")

        elif sub_menu == "3":
            print("\n3. Total Harga Pesanan")
            nama = input("Masukkan nama klien untuk menghitung total harga: ")
            ditemukan = False
            for kategori, daftar_pesanan in data_klien.items():
                for pesanan in daftar_pesanan:
                    if pesanan["nama"] == nama:
                        ditemukan = True
                        if pesanan["kategori baju"] == "adat":
                            harga_per_baju = 100000
                        elif pesanan["kategori baju"] == "pernikahan":
                            harga_per_baju = 150000
                        elif pesanan["kategori baju"] == "kebaya":
                            harga_per_baju = 120000
                        else:
                            harga_per_baju = 0

                        total_harga = harga_per_baju * pesanan["jumlah baju"]
                        
                        print(f"\nNama          : {pesanan['nama']}")
                        print(f"Kategori Baju : {pesanan['kategori baju']}")
                        print(f"Jumlah Baju   : {pesanan['jumlah baju']}")
                        print(f"Total Harga   : Rp{total_harga}")
                        break
            
            if not ditemukan:
                print(f"Pemesan dengan nama {nama} tidak ditemukan.")

        elif sub_menu == "4":
            print("\n4. Pembayaran")
            nama = input("Masukkan nama klien untuk pembayaran: ")
            ditemukan = False
            for kategori, daftar_pesanan in data_klien.items():
                for pesanan in daftar_pesanan:
                    if pesanan["nama"] == nama:
                        ditemukan = True
                        if pesanan["kategori baju"] == "adat":
                            harga_per_baju = 100000
                        elif pesanan["kategori baju"] == "pernikahan":
                            harga_per_baju = 150000
                        elif pesanan["kategori baju"] == "kebaya":
                            harga_per_baju = 120000
                        else:
                            harga_per_baju = 0
                        
                        total_harga = harga_per_baju * pesanan["jumlah baju"]
                        
                        member = input("Apakah klien memiliki kartu member? (ya/tidak): ")
                        if member == "ya":
                            pesanan["member"] = True
                            total_harga -= total_harga * 0.05
                            print("Diskon 5% diterapkan.")
                        else:
                            pesanan["member"] = False
                        
                        print(f"Total Harga Setelah Diskon: Rp{total_harga}")
                        
                        while True:
                            pembayaran_input = input(f"Masukkan jumlah pembayaran (Rp{total_harga}): ")
                            if pembayaran_input:
                                pembayaran = int(pembayaran_input)
                                if pembayaran >= total_harga:
                                    print(f"Pembayaran berhasil. Kembaliannya adalah Rp{pembayaran - total_harga}")
                                    break
                                else:
                                    print("Pembayaran kurang, silakan masukkan jumlah yang cukup.")
                            else:
                                print("Masukkan angka yang valid.")
                        break

            if not ditemukan:
                print(f"Pemesan dengan nama {nama} tidak ditemukan.")

        elif sub_menu == "5":
            print("\n5. Pengembalian")
            nama = input("Masukkan nama klien untuk pengembalian: ")
            ditemukan = False
            for kategori, daftar_pesanan in data_klien.items():
                for pesanan in daftar_pesanan:
                    if pesanan["nama"] == nama and not pesanan["dikembalikan"]:
                        ditemukan = True
                        pinjam_berapa_hari = pesanan["pinjam berapa hari"]
                        hari_pengembalian = input("Masukkan hari keberapa baju dikembalikan: ")

                        if hari_pengembalian:
                            hari_pengembalian = int(hari_pengembalian)
                            keterlambatan = hari_pengembalian - pinjam_berapa_hari
                            
                            if keterlambatan > pinjam_berapa_hari:
                                denda = keterlambatan * 10000
                            else:
                                denda = 0

                            if denda > 0:
                                print(f"Denda keterlambatan total adalah: Rp.{denda}")
                                while True:
                                    pembayaran_denda = input(f"Masukkan jumlah pembayaran denda (Rp{denda}): ")
                                    
                                    if pembayaran_denda:
                                        pembayaran_denda = int(pembayaran_denda)
                                        if pembayaran_denda >= denda:
                                            print(f"Denda telah dibayar. Kembaliannya adalah Rp{pembayaran_denda - denda}")
                                            break
                                        else:
                                            print("Pembayaran kurang, silakan masukkan jumlah yang cukup.")
                                    else:
                                        print("Masukkan angka yang valid.")
                            else:
                                print("Tidak ada denda keterlambatan.")
                            
                            pesanan["dikembalikan"] = True
                            break
                        else:
                            print("Masukkan jumlah hari yang valid.")
                            
            if not ditemukan:
                print(f"Pemesan dengan nama {nama} tidak ditemukan atau sudah dikembalikan.")

        elif sub_menu == "6":
            print("\n6. Update Pesanan")
            nama = input("Masukkan nama klien yang ingin diperbarui: ")
            ditemukan = False
            for kategori, daftar_pesanan in data_klien.items():
                for pesanan in daftar_pesanan:
                    if pesanan["nama"] == nama and not pesanan["dikembalikan"]:
                        ditemukan = True
                        print(f"Data saat ini: {pesanan}")
                        
                        jumlah_baju_input = input("Masukkan jumlah baju baru: ")
                        if jumlah_baju_input:
                            pesanan["jumlah baju"] = int(jumlah_baju_input)
                        else:
                            print("Input jumlah baju tidak valid. Harus berupa angka.")

                        durasi_pinjam_input = input("Masukkan durasi peminjaman baru (hari): ")
                        if durasi_pinjam_input:
                            pesanan["pinjam berapa hari"] = int(durasi_pinjam_input)
                        else:
                            print("Input durasi peminjaman tidak valid. Harus berupa angka.")
                        
                        print("Data berhasil diperbarui.")
                        break

            if not ditemukan:
                print(f"Pemesan dengan nama {nama} tidak ditemukan atau sudah dikembalikan.")

        elif sub_menu == "7":
            print("\n7. Hapus Data Pemesan")
            nama = input("Masukkan nama klien yang ingin dihapus: ")
            ditemukan = False
            for kategori, daftar_pesanan in data_klien.items():
                for pesanan in daftar_pesanan:
                    if pesanan["nama"] == nama:
                        ditemukan = True
                        daftar_pesanan.remove(pesanan)  
                        print(f"Data pemesan dengan nama {nama} telah dihapus.")
                        break
                if ditemukan:
                    break

            if not ditemukan:
                print(f"Pemesan dengan nama {nama} tidak ditemukan.")

        elif sub_menu == "8":
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            print("Pilihan tidak valid.")
menu()