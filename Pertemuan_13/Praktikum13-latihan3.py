# Nama    : Rony Wijaya
# NIM     : J0403251047
# Kelas   : TPL B2
# Praktikum 13 Graph III: Spanning Tree

# ==========================================================
# Latihan 3 - Implementasi Algoritma Prim
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree (Prim):")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# ==========================================================
# JAWABAN ANALISIS:
# 1. Node awal apa yang digunakan?
#    Node 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge A-C dengan bobot 2.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Dengan memilih edge dengan bobot terkecil yang terhubung dengan node 
#    yang sudah dikunjungi menuju node yang belum dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Kruskal memilih edge global terkecil, sedangkan Prim membangun tree 
#    secara bertahap dari satu node awal ke node di sekitarnya.
# ==========================================================