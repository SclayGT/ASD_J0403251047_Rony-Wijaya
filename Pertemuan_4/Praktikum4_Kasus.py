# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

# ===================================================
# Studi Kasus : Sistem antrian layanan akademik
# Implementasi Queue =>
# Enqueue : Memindahkan pointer rear (Nambah data baru dari belakang)
# Dequeue : Memindahkan pointer front (Menghapus data dari depan)
# Front -> A-> B -> C -> Rear
# ===================================================

# 1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim # Menyimpan NIM Mahasiswa
        self.nama = nama # Menyimpan Nama Mahasiswa
        self.next = None# Pointer ke Node berikutnya

# 2) Mendefinisikan queue, terdiri dari Front dan Rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # Ketika queue kosong maka Front = Rear = None
        return self.front is None
    
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # Jika queue tidak kosong, maka data baru diletakkan 
        # setelah rear kemudian dijadikan sebagai tail
        self.rear.next = nodeBaru
        self.rear = nodeBaru
    
    # Menghapus data paling depan ( Memberikan layanan akademik ) 
    def dequeue(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak ada Mahasiswa yang dilayani")
            return None
        # Lihat data bagian Front, simpan di variabel data yang akan dihapus ( Dilayani )
        node_dilayani = self.front
        
        # Geser pointer front ke next front
        self.front = self.front.next
        
        # Jika Fornt menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
        
        return node_dilayani
    
    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1
        
# Program Utama

def main():
    
    # Instantiasi queue
    q= queueAkademik()
    
    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4) : ").strip()
        
        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahkan Ke Antrian")
        
        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")
            
        elif pilihan == "3":
            q.tampilkan()
            
        elif pilihan == "4":
            print("Program Selesai. Terima Kasih")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")

# Penanda eksekusi file utama
if __name__ == "__main__":
    main()
