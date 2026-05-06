# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")



# Jawaban Analisis:

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Titik yang paling mudah dijangkau dari titik awal adalah Kantin, dengan durasi 
#    perjalanan hanya 2 menit. Secara struktur graf, Kantin merupakan tetangga 
#    langsung (immediate neighbor) dengan bobot edge terkecil dibandingkan lokasi lainnya.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Durasi minimum untuk mencapai Aula dari Gerbang adalah 7 menit.
#    Rute Terbaik: Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7).
#    Perbandingan: Jalur Gerbang -> Kantin -> Aula memakan waktu 9 menit, sedangkan 
#    lewat Perpustakaan memakan 10 menit. Meskipun rute terbaik melewati lebih banyak 
#    lokasi (3 edges), akumulasi biayanya tetap paling rendah.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak menjamin. Dalam graf berbobot, efisiensi ditentukan oleh beban akumulatif, 
#    bukan kuantitas node yang dilewati. 
#    Contoh: Perjalanan dari Kantin ke Aula secara langsung memakan waktu 7 menit. 
#    Namun, jika memutar melalui Lab, waktunya hanya 5 menit (4+1). Ini membuktikan 
#    jalur dengan lebih banyak titik bisa lebih efisien jika total bobotnya lebih kecil.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Beberapa alasan utama penggunaan Dijkstra di sini:
#
#    - Karakteristik Data: Bobot merepresentasikan waktu tempuh yang tidak mungkin 
#      negatif, sehingga syarat utama algoritma Dijkstra terpenuhi dengan sempurna.
#
#    - Fokus Sumber Tunggal: Kasus ini bersifat "Single Source Shortest Path", 
#      di mana tujuannya mencari rute dari satu titik masuk (Gerbang) ke semua 
#      fasilitas lainnya.
#
#    - Keunggulan Operasional: Dengan bantuan priority queue, Dijkstra bekerja jauh 
#      lebih responsif dan cepat dibandingkan Bellman-Ford untuk graf dengan bobot positif.
#
#    - Presisi: Dijkstra menjamin hasil optimal secara matematis dalam menentukan 
#      jalur tercepat di tengah jaringan lokasi yang bercabang.