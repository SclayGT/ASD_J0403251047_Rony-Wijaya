# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

'''
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend()
'''

# Jawaban Soal No 1:
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
# Jawaban Soal No 2:
'''
result.extend(left[i:])
result.extend(right[j:])

Fungsinya untuk:

Menambahkan sisa elemen yang belum dibandingkan

Karena salah satu list pasti masih memiliki sisa elemen setelah perulangan selesai

Tanpa extend(), elemen sisa tidak akan masuk ke hasil akhir.
'''