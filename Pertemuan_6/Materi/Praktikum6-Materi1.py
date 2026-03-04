# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

#=========================================================
# Insertion Sort (Ascending)
#=========================================================

data = []

def insertion_sort(data):
    # loop mulai dari data ke 2 (Index array ke 1)
    for i in range(1,len(data)):
        
        key = data[i] # Simpan nilai yang disisipkan
        
        j = i-1 # Index ellemen terakhir di bagian kiri
        
        # Geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
            # Sisipkan key ke posisi yang benar
            data[j+1] = key
        return data

angka = [7,8,5,2,4,6]

print("Hasil Sorting: ", insertion_sort(angka))