# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# A -> B -> D
# A -> C -> D

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# Jawaban Analisis:

# 1. Kalkulasi Akumulasi Jalur A -> B -> D
#    Total bobot pada rute ini adalah 9. 
#    Dihitung berdasarkan penjumlahan nilai pada nested dictionary:
#    graph['A']['B'] (4) + graph['B']['D'] (5) = 9.

# 2. Kalkulasi Akumulasi Jalur A -> C -> D
#    Total bobot pada rute ini adalah 3.
#    Dihitung berdasarkan penjumlahan nilai pada nested dictionary:
#    graph['A']['C'] (2) + graph['C']['D'] (1) = 3.

# 3. Penentuan Jalur Optimal (Logika Program)
#    Program secara otomatis menetapkan rute A -> C -> D sebagai jalur terpendek.
#    - Jalur_1 (9) vs Jalur_2 (3).
#    - Evaluasi Kondisi: 'if jalur_1 < jalur_2' (9 < 3) menghasilkan nilai False.
#    - Konsekuensi: Alur logika berpindah ke blok 'else', yang mencetak 
#      jalur kedua sebagai hasil paling efisien.

# 4. Mengapa "Jumlah Langkah" (Edges) Bukan Penentu Utama?
#    Dalam 'Weighted Graph', efisiensi diukur dari akumulasi nilai (cost), 
#    bukan dari seberapa sedikit titik (node) yang dilewati.
#
#    - Analogi Realitas: Sebuah jalur dengan sedikit belokan bisa saja memiliki 
#      kemacetan tinggi atau jarak yang jauh. Sebaliknya, jalur dengan banyak 
#      belokan mungkin merupakan jalan pintas yang lebih lancar dan dekat.
#
#    - Kesimpulan: Jumlah edge hanya relevan pada Unweighted Graph. Pada 
#      Weighted Graph, bobot merepresentasikan variabel krusial seperti waktu, 
#      biaya, atau latensi jaringan yang jauh lebih penting daripada 
#      sekadar jumlah lompatan (hop count).