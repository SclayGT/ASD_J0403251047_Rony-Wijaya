# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = key

    return data

'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?
'''

'''
Jawaban:
1. Karena pada algoritma Insertion Sort, elemen pertama (indeks 0) dianggap sudah dalam keadaan terurut.
2. key berfungsi untuk menyimpan nilai yang sedang dibandingkan dan akan disisipkan ke posisi yang tepat.
3. Jika menggunakan for, kita harus menentukan batas perulangan di awal, 
   sedangkan pada insertion sort berhenti berdasarkan kondisi.
4. Di dalam while terjadi proses pergeseran elemen (shifting).
'''

