# Nama    : Rony Wijaya
# NIM     : J0403251047
# Kelas   : TPL B2
# Praktikum 13 Graph III: Spanning Tree

# ==========================================================
# Latihan 2 - Implementasi Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree (Kruskal):")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# ==========================================================
# JAWABAN ANALISIS:
# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal bekerja dengan mengurutkan seluruh edge dari 
#    yang terkecil untuk mendapatkan total bobot minimum.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6.
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge seperti A-B (4) dan A-D (5) tidak dipilih karena semua node sudah 
#    terhubung dan penambahannya akan menyebabkan pemborosan biaya/cycle.
# ==========================================================