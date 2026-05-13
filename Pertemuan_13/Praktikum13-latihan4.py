# Nama    : Rony Wijaya
# NIM     : J0403251047
# Kelas   : TPL B2
# Praktikum 13 Graph III: Spanning Tree


# ==========================================================
# Latihan 4 - Studi Kasus Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal
# ==========================================================

import heapq

# Representasi weighted graph (Jaringan Gedung)
gedung = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

def hitung_biaya_kabel(graph, start):
    visited = set([start])
    pq = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(pq, (weight, start, neighbor))
    
    mst = []
    total_cost = 0
    while pq:
        weight, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (w, v, neighbor))
    return mst, total_cost

hasil, biaya = hitung_biaya_kabel(gedung, 'GedungA')

print("Rute pemasangan kabel:")
for edge in hasil:
    print(f"{edge[0]} ke {edge[1]} (Biaya: {edge[2]})")
print(f"Total biaya minimum = {biaya}")

# ==========================================================
# JAWABAN ANALISIS:
# 1. Algoritma apa yang digunakan?
#    Algoritma Prim.
#
# 2. Edge mana saja yang dipilih?
#    A-C (2), C-D (1), dan D-B (3).
#
# 3. Berapa total biaya minimum?
#    Total biayanya adalah 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuannya adalah menghubungkan seluruh gedung dengan biaya 
#    pemasangan kabel terkecil tanpa membentuk siklus yang tidak perlu.
# ==========================================================