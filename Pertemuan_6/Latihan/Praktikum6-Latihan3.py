# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Memindahkan elemen yang lebih besar dari key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        print(f"Iterasi {i}: {data}")  # Untuk melihat proses tracing

    return data


# Data yang akan diurutkan
data = [5, 2, 4, 6, 1, 3]
hasil = insertion_sort(data)
print("Hasil akhir:", hasil)