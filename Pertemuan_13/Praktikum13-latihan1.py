# Nama    : Rony Wijaya
# NIM     : J0403251047
# Kelas   : TPL B2
# Praktikum 13 Graph III: Spanning Tree


# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================

# 1. Daftar edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# 2. Contoh spanning tree yang valid (menghubungkan semua node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 3. Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# JAWABAN ANALISIS:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki kemungkinan jalur yang lebih banyak dan mengandung cycle, 
#    sedangkan spanning tree menghubungkan seluruh node tanpa membentuk cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle dihindari karena menyebabkan penggunaan edge berlebih, meningkatkan 
#    biaya total, dan membuat koneksi tidak efisien.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya menggunakan jumlah minimum edge yang diperlukan 
#    untuk menghubungkan semua node, yaitu (jumlah node - 1).
# ==========================================================