# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#=================================================

#sruktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

# Representasi graph antar lokasi menggunakan dictionary
graph_bfs = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()            # Set untuk melacak node yang sudah dikunjungi agar tidak terjadi loop
    queue = deque([start])     # Menggunakan deque sebagai antrean (FIFO) untuk eksplorasi level-by-level
    
    visited.add(start)         # Tandai titik awal sebagai sudah dikunjungi
    
    while queue:
        node = queue.popleft() # Ambil node dari antrean paling depan
        print(node, end=" ")   # Tampilkan node yang sedang dikunjungi
        
        # Periksa semua tetangga dari node saat ini
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)    # Tandai tetangga sebagai dikunjungi
                queue.append(neighbor)   # Tambahkan ke antrean untuk dieksplorasi nanti

print("BFS dari Rumah:")
bfs(graph_bfs, 'Rumah')
print("\n")

"""
Pertanyaan Analisis Latihan 1:
1. Node mana yang dikunjungi pertama?
    Jawaban: Node 'Rumah', karena dalam algoritma BFS, pencarian selalu dimulai dari node asal (start node) yang ditentukan.

2. Mengapa BFS cocok untuk mencari jalur terdekat?
    Jawaban: Karena BFS mengeksplorasi graph secara merata ke semua arah pada jarak yang sama (level demi level) sebelum pindah ke jarak yang lebih jauh. 
    Hal ini menjamin bahwa saat tujuan ditemukan pertama kali, jalur tersebut adalah yang memiliki jumlah lompatan (edges) paling sedikit.

3. Apa perbedaan urutan BFS jika struktur graph diubah?
    Jawaban: Jika struktur graph (koneksi antar node) berubah, urutan antrean (queue) juga akan berubah. 
    Misalnya, jika 'Rumah' langsung terhubung ke 'Pasar', maka 'Pasar' akan dikunjungi lebih awal (pada level 1) daripada menunggu jalur melalui 'Toko'.
"""