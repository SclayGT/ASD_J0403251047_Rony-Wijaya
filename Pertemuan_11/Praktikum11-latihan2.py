#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)
#=================================================

# Representasi graph antar lokasi menggunakan dictionary
graph_dfs = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)          # Tandai node saat ini sebagai sudah dikunjungi
    print(node, end=" ")       # Tampilkan node yang sedang dikunjungi
    
    # Telusuri setiap tetangga secara rekursif (masuk ke dalam)
    for neighbor in graph[node]:
        if neighbor not in visited:
            # Panggil fungsi dfs kembali untuk tetangga sebelum pindah ke saudara tetangga tersebut
            dfs(graph, neighbor, visited)

visited_set = set()            # Inisialisasi set kosong untuk melacak kunjungan
print("DFS dari A:")
dfs(graph_dfs, 'A', visited_set)
print("\n")

"""
Pertanyaan Analisis Latihan 2:
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
    Jawaban: Karena DFS menggunakan prinsip tumpukan (Stack), baik melalui rekursi maupun eksplisit. 
    Algoritma ini akan terus mengeksplorasi satu cabang hingga mencapai node daun (tidak ada tetangga lagi) sebelum melakukan backtracking.

2. Apa yang terjadi jika urutan neighbor diubah?
    Jawaban: Urutan kunjungan akan berubah secara visual, namun tetap mengikuti pola kedalaman. 
    Misalnya jika 'A': ['C', 'B'], maka jalur ke 'C' dan 'F' akan diselesaikan sepenuhnya sebelum algoritma mulai melihat ke arah 'B'.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
    Jawaban: 
    - BFS pada Graph Latihan 2: A B C D E F (Eksplorasi melebar per level: level 0 -> level 1 -> level 2).
    - DFS pada Graph Latihan 2: A B D E C F (Eksplorasi mendalam: mengikuti satu jalur sampai mentok baru pindah ke cabang lain).
"""