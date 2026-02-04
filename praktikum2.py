# =======================================
# Praktikum 2 : konsep ADT dan file handling
# Latihan 1 : Membuat fungsi Load Data
# =======================================
nama_file = "data_mahasiswa.txt"
def baca_data_mahasiswa(nama_file):
    data_dict = {}
    with open(nama_file,"r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nimm,nama,nilai = baris.split(",")
            data_dict[nimm]= {
                "nama" : nama,
                "nilai" : nilai
            }
    return data_dict

# Memanggil fungsi baca_data_mahasiswa
# buka_data = baca_data_mahasiswa(nama_file)
# print("jumlah data terbaca",len(buka_data)) 

# =======================================
# Praktikum 2 : konsep ADT dan file handling
# Latihan 2 : Membuat fungsi menampilkan data
# =======================================

def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    # Membuat Header Tabel
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM':10} | {'nama':<12} | {'Nilai':>5}")
    print("-"*32)

    for nim in sorted(data_dict):
        nama = data_dict [nim]["nama"]
        nilai = data_dict [nim]["nilai"]
        print(f"{nim:10} | {nama:<12}|{nilai:>5}")
        
# tampilkan_data(buka_data)

# =======================================
# Praktikum 2 : konsep ADT dan file handling
# Latihan 3 : Membuat fungsi Mencari data
# =======================================

def cari_data (data_dict):
    if len (data_dict) == 0:
        print("Data TIdak Ditemukan")
        return
    cari = input("Masukan Data Yang Ingin Dicari: ").strip().upper()
    
    
    if cari in data_dict:
        nim = cari
        nama = data_dict [nim]["nama"]
        nilai = data_dict [nim]["nilai"]
        print("========= Data Mahasiswa =========")
        print ("Data Yang Ditemukan")
        print("NIM: ", nim)
        print("Nama: ", nama)
        print("Nilai: ", nilai)
        return
    else:
        print("Data Tidak Ditemukan")

# # tampilkan_data(buka_data)
# cari_data(buka_data)

# =======================================
# Praktikum 2 : konsep ADT dan file handling
# Latihan 4 : Membuat fungsi Update data
# =======================================

def update_nilai (data_dict):
    nim = input ("Masukkan NIM yang ingin diupdate datanya: "). strip().upper()
    if nim in data_dict:
        nama = data_dict [nim]["nama"]
        nilai = data_dict [nim]["nilai"]
        print("========= Data Mahasiswa =========")
        print ("Data Yang Ditemukan")
        print("NIM: ", nim)
        print("Nama: ", nama)
        print("Nilai: ", nilai)
        print("========= Update Data =========")
        try:
            nilai_baru = int(input("Masukan Nilai Baru (0-100) : "))
        except ValueError:
            print("Nilai baru harus berupa angka")
        
        if (nilai_baru < 0 or nilai_baru>100):
            print("Nilai harus antara 0 sampai 100, Update Dibatalkan")
            return
        
        data_dict[nim]["nilai"] = nilai_baru
        print(f"Update Berhasil. Nilai {nim} berubah dari {nilai} menjadi {nilai_baru}")
    else:
        print("Data Tidak Ditemukan")
        return
    

# =======================================
# Praktikum 2 : konsep ADT dan file handling
# Latihan 5 : Membuat fungsi Simpan data
# =======================================

def simpan_data(path,data_dict):
    try:
        with open(path,"w",encoding = "utf-8") as file:
            for nim in sorted(data_dict.keys()):
                nama = data_dict[nim]["nama"]
                nilai = data_dict[nim]["nilai"]
                file.write(f"{nim},{nama},{nilai}\n")
            print("Data Tersimpan")
    except FileNotFoundError:
        print("Data Tidak ada")

# =======================================
# Praktikum 2 : konsep ADT dan file handling
# Latihan 4 : Membuat fungsi Menu
# =======================================

def main():
    data = baca_data_mahasiswa(nama_file)
    while True:
        print("====== Program Mahasiswa =====")
        print("[1] Tampilkan Data")
        print("[2] Cari Data")
        print("[3] Update Data")
        print("[4] Simpan Data yang telah diubah")
        print("[0] Keluar Program")
        valid_opt = (1,2,3,4,0)
        try:
            pilihan = int(input("Input Perintah : ").strip())
            if pilihan in valid_opt:
                if pilihan == 1:
                    tampilkan_data(data)
                elif pilihan == 2:
                    cari_data(data)
                elif pilihan == 3:
                    update_nilai(data)
                elif pilihan == 4 :
                    simpan_data(nama_file,data)
                elif pilihan == 0:
                    exit()
            else:
                print("Input Tidak valid")
                continue
        except ValueError:
            print("Pilihan Tidak Valid")


if __name__ == "__main__":
    main()