# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
#    Setiap key adalah nama kota, dan value-nya adalah dictionary
#    berisi kota tetangga beserta bobot (jarak) edge-nya.
graph = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},
    'Depok'   : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta' : {'Bandung': 7},
    'Bandung' : {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari node 'start' ke semua node lain
    dalam graph berbobot menggunakan algoritma Dijkstra.

    Parameter:
        graph (dict) : representasi graph berbobot (adjacency dict)
        start (str)  : nama node awal

    Return:
        distances (dict) : jarak terpendek dari start ke tiap node
    """
    # Inisialisasi semua jarak dengan nilai tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue: menyimpan pasangan (jarak_kumulatif, nama_node)
    # heapq selalu mengambil elemen dengan jarak terkecil terlebih dahulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak ini sudah tidak relevan (sudah ada yang lebih kecil)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak ke tetangga melalui node saat ini
            distance = current_distance + weight

            # Relaksasi: perbarui jarak jika ditemukan jalur yang lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 3. Penentuan node awal
node_awal = 'Bogor'

# 4. Jalankan Dijkstra dan tampilkan output jarak terpendek
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"  {node_awal} -> {kota} = {jarak}")



# Jawaban Analisis:

# 1. Node awal yang digunakan apa?
#    Titik keberangkatan (starting point) yang ditetapkan dalam simulasi ini 
#    adalah kota Bogor, sebagaimana didefinisikan pada variabel 'node_awal'.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Kota Depok merupakan tujuan terdekat dari Bogor dengan nilai jarak 2. 
#    Hal ini dikarenakan adanya koneksi langsung (direct edge) dengan bobot 
#    paling minimal dibandingkan rute ke kota lainnya.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Bandung menjadi titik terjauh dengan akumulasi jarak 8. 
#    Dijkstra menemukan rute optimal melalui Bogor -> Depok -> Bandung (2 + 6 = 8). 
#    Jalur ini lebih efisien dibandingkan lewat Jakarta (Bogor-Jakarta-Bandung = 12) 
#    maupun jalur transit ganda (Bogor-Depok-Jakarta-Bandung = 11).

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini.
#
#    - Tahap Persiapan: 
#      Program memberikan nilai 'infinity' ke semua kota kecuali Bogor (0), 
#      lalu memasukkan Bogor ke dalam antrean prioritas (Priority Queue).
#
#    - Eksplorasi Bogor: 
#      Algoritma memeriksa tetangga terdekat. Jarak Jakarta tercatat 5 dan Depok 2. 
#      Keduanya masuk ke antrean untuk dievaluasi lebih lanjut.
#
#    - Optimasi via Depok: 
#      Karena Depok memiliki jarak terkecil (2), ia diproses lebih dulu. 
#      Ditemukan jalur ke Jakarta melalui Depok (2+2=4). Karena 4 lebih kecil 
#      dari 5 (jarak langsung Bogor-Jakarta), maka data jarak Jakarta diperbarui. 
#      Jarak ke Bandung juga ditemukan sebesar 8 (2+6).
#
#    - Evaluasi Jakarta: 
#      Saat memproses Jakarta (jarak 4), algoritma mencoba menghitung jalur ke 
#      Bandung (4+7=11). Namun, karena 11 lebih besar dari jarak Bandung saat 
#      ini (8), data Bandung tidak berubah.
#
#    - Finalisasi: 
#      Setelah semua kemungkinan dalam antrean diperiksa dan tidak ada lagi 
#      jarak yang lebih kecil (relaksasi), algoritma berhenti dan memberikan 
#      hasil rute yang paling hemat biaya/jarak.