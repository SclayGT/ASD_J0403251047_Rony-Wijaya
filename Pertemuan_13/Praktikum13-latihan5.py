# Nama    : Rony Wijaya
# NIM     : J0403251047
# Kelas   : TPL B2
# Praktikum 13 Graph III: Spanning Tree

# ==========================================================
# Latihan 5 - Tugas Mandiri
# Kasus: Jaringan Komputer
# Menggunakan Algoritma Prim
# ==========================================================

# Data hubungan router (Kasus 2)
# (bobot, node1, node2)
jaringan = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

def rute_router(edges):
    edges.sort()
    mst = []
    total_weight = 0
    connected = set()
    
    for weight, u, v in edges:
        if u not in connected or v not in connected:
            mst.append((u, v, weight))
            total_weight += weight
            connected.add(u)
            connected.add(v)
    return mst, total_weight

hasil_mst, total_bobot = rute_router(jaringan)

print("Jaringan Komputer Efisien (MST):")
for edge in hasil_mst:
    print(f"{edge[0]} - {edge[1]} (Bobot: {edge[2]})")
print(f"Total bobot minimum = {total_bobot}")

# ==========================================================
# JAWABAN ANALISIS:
# 1. Kasus apa yang dipilih?
#    Kasus 2: Jaringan Komputer.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    RouterC-RouterD (1), RouterA-RouterC (2), RouterA-RouterB (3).
#
# 4. Berapa total bobot MST?
#    Total bobotnya adalah 6.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    RouterB-RouterC (4) dan RouterB-RouterD (5) tidak dipilih karena 
#    node-node tersebut sudah terhubung dengan rute yang lebih murah.
# ==========================================================