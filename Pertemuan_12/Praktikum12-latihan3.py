# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:

# 1. Bobot Langsung A -> B
#    Secara eksplisit, bobot edge langsung dari A ke B adalah 5. 
#    Ini merupakan rute default jika hanya mempertimbangkan koneksi 
#    satu langkah (direct connection).

# 2. Akumulasi Jalur Alternatif A -> C -> B
#    Total bobot melalui rute memutar ini adalah 2. Kalkulasi berasal dari:
#    cost(A,C) = 4, ditambah cost(C,B) = -2.
#    Keberadaan bobot negatif pada edge C->B secara signifikan mereduksi 
#    total biaya perjalanan menuju node B.

# 3. Penentuan Jalur Optimal
#    Algoritma menetapkan rute A -> C -> B sebagai jalur optimal (nilai = 2). 
#    Meskipun jalur langsung A -> B tersedia, Bellman-Ford berhasil 
#    mendeteksi bahwa kombinasi rute melalui C lebih "murah". Hal ini 
#    terbukti pada output program di mana node B bernilai 2, bukan 5.

# 4. Keunggulan Bellman-Ford pada Bobot Negatif
#    Berbeda dengan Dijkstra yang cenderung "mengunci" nilai di awal (Greedy), 
#    Bellman-Ford melakukan iterasi menyeluruh sebanyak V-1 kali. 
#    Strategi ini memungkinkan algoritma untuk terus merevisi dan 
#    memperbarui jarak jika ditemukan jalur baru yang lebih efisien, 
#    termasuk rute yang melibatkan bobot negatif.

# 5. Esensi dari Relaksasi Edge
#    Relaksasi adalah proses memperkecil estimasi jarak secara sistematis.
#    - Mekanisme: Program membandingkan apakah 'distances[neighbor]' saat ini
#      lebih besar daripada 'distances[node] + weight'.
#    - Dampak: Jika ditemukan rute yang lebih kecil, data lama akan diganti. 
#      Proses ini memastikan informasi jarak terpendek menyebar secara 
#      konsisten ke seluruh graf pada setiap iterasinya.

# 6. Perbandingan Utama: Bellman-Ford vs Dijkstra
#
#    | Karakteristik       | Dijkstra                    | Bellman-Ford           |
#    |---------------------|-----------------------------|------------------------|
#    | Bobot Negatif       | Tidak Mendukung             | Mendukung              |
#    | Strategi Proses     | Greedy (Node Terdekat)      | Relaksasi Semua Edge   |
#    | Struktur Data       | Priority Queue (Min-Heap)   | Nested Loop            |
#    | Kompleksitas Waktu  | O((V + E) log V) - Cepat    | O(V * E) - Lambat      |
#    | Deteksi Siklus (-)  | Tidak Bisa                  | Bisa (Iterasi ke-V)    |
#
#    Kesimpulan: 
#    Gunakan Dijkstra untuk efisiensi pada graf dengan bobot positif. 
#    Gunakan Bellman-Ford jika graf memiliki bobot negatif atau 
#    diperlukan deteksi siklus negatif (negative cycle).