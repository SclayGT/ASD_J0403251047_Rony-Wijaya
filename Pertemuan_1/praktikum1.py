# ===========================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1 : Membaca seluruh isi file
# ===========================================

# Membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print ("=== Hasil Read ===")
print (" Tipe Data :", type(isi_file))
print (" Jumlah Karakter :", len(isi_file))
print (" Jumlah Baris :", isi_file.count("\n") + 1)
print ("(● ◡ ●)")

# Membuka file per baris
print ("\n=== Hasil Read Per Baris ===")
jumlah_baris = 0
with open ("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip()
        print ("Baris ke-",jumlah_baris)
        print (" Isinya :", baris)
        
# ===========================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 2 : Parsing baris menjadi kolom data
# ===========================================

# Membuka file baris menjadi kolom data
print ("\n=== Hasil baris menjadi kolom data ===")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print ("NIM :", nim, "\tNama :", nama, "\tNilai :", nilai)
    
# ===========================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 3 : Membaca file dan menyimpan ke dalam list
# ===========================================

data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        
        nim, nama, nilai = baris.split(",")
        # Simpan sebagai list "[NIM, Nama, Nilai]"
        data_list.append([nim, nama,int (nilai)])

print("\n=== Data mahasiswa dalam bentuk list ===")
print(data_list)

print("\n=== Jumlah record dalam list ===")
print("Jumlah record :", len(data_list))

print("\n=== Menampilkan data record tertentu ===")
print("Contoh data Record ke-1 :", data_list[0])

# ===========================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 4 : Membaca file dan menyimpan ke dalam dictionary
# ===========================================

data_dict = {}
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        
        # Simpan sebagai dictionary "{'NIM': NIM, 'Nama': Nama, 'Nilai': Nilai}"
        data_dict[nim] = {'Nama': nama, 'Nilai': int (nilai)}

print("\n=== Data mahasiswa dalam bentuk dictionary ===")
print(data_dict)
        

