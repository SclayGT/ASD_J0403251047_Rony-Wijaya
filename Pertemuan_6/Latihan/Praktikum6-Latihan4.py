# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)
def merge(left,right):
    
    result = []
    i = 0
    j = 0
    
    # Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1
    # Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

angka = [13,7,28,5,19,36,4]
print("Hasil Sorting: ", merge_sort(angka))

'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?
'''

'''
1. Base case adalah kondisi penghentian rekursi.
2. Karena merge sort menggunakan teknik rekursi (divide and conquer) untuk 
membagi list menjadi bagian kecil sampai ukuran 1.
3. Untuk menggabungkan dua list yang sudah terurut menjadi satu list yang terurut kembali.
'''