# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:

# 1. Hasil Kalkulasi Jarak A -> B
#    Jarak minimum yang tercatat adalah 4. Nilai ini diperoleh dari 
#    koneksi langsung (direct edge) tanpa perantara, di mana tidak 
#    ditemukan rute alternatif yang lebih efisien dari titik asal.

# 2. Hasil Kalkulasi Jarak A -> C
#    Jarak minimum yang tercatat adalah 2. Sama dengan poin sebelumnya, 
#    ini merupakan jalur terpendek yang tersedia secara langsung 
#    dari node sumber (A).

# 3. Hasil Kalkulasi Jarak A -> D
#    Jarak minimum yang tercatat adalah 3. Akumulasi ini didapat dari 
#    rute A -> C (2) kemudian C -> D (1). Algoritma mengabaikan rute 
#    A -> B -> D karena total bobotnya (9) jauh lebih besar.

# 4. Perbandingan Efisiensi Jalur (Via B vs Via C)
#    Meskipun kedua rute sama-sama memiliki dua lompatan (2 hops), rute 
#    melalui node C jauh lebih efisien secara matematis. 
#    - Jalur A-B-D: Total cost = 9.
#    - Jalur A-C-D: Total cost = 3.
#    Dijkstra berfokus pada meminimalkan akumulasi beban (cost), 
#    bukan sekadar menghitung jumlah node yang dilewati.

# 5. Peran Krusial Priority Queue (min-heap)
#    Priority Queue berfungsi sebagai mekanisme pemilihan otomatis yang 
#    mendahulukan node dengan jarak estimasi terendah untuk dievaluasi.
#    - Efisiensi: Menggunakan min-heap menghindari pemindaian manual 
#      ke seluruh daftar jarak yang memakan waktu.
#    - Prinsip Greedy: Memastikan setiap langkah yang diambil adalah 
#      yang terbaik pada saat itu untuk mencapai solusi optimal global 
#      tanpa redundansi proses.

# 6. Keterbatasan pada Bobot Negatif
#    Dijkstra bekerja dengan asumsi bahwa penambahan edge akan selalu 
#    meningkatkan total biaya (bobot positif).
#    - Masalah: Edge negatif dapat memperkecil jarak secara retroaktif 
#      setelah suatu node dianggap "final".
#    - Dampak: Dapat menyebabkan kegagalan logika atau hasil tidak akurat. 
#      Untuk graf dengan bobot negatif, algoritma Bellman-Ford adalah 
#      pilihan yang lebih tepat meski memiliki kompleksitas waktu lebih tinggi.