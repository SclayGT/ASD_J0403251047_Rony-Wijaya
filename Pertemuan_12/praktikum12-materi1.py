#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# Mengimpor modul heapq untuk mengelola antrean prioritas (min-heap)
import heapq 

# Definisi struktur graf berbobot menggunakan dictionary bersarang
# Format: node_asal -> {node_tujuan: bobot_jarak}
graph = { 
            'A': {'B': 4, 'C': 2},      # Akses dari A: ke B (bobot 4), ke C (bobot 2)
            'B': {'D': 5},              # Akses dari B: ke D (bobot 5)
            'C': {'D': 1},              # Akses dari C: ke D (bobot 1)
            'D': {}                     # Node D adalah titik terminasi (tidak ada tetangga)
        } 
 
 
def dijkstra(graph, start): 
    # Inisialisasi kamus untuk menyimpan estimasi jarak terpendek ke setiap node
    # Default nilai diatur ke 'infinity' sebagai representasi jarak yang belum terjamah
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari titik keberangkatan ke dirinya sendiri adalah 0
    distances[start] = 0 
    
    # Priority Queue untuk menyimpan tuple (jarak_kumulatif, node)
    # Dijkstra akan selalu mengevaluasi jalur dengan biaya terendah terlebih dahulu
    pq = [(0, start)] 
 
    # Melakukan iterasi selama antrean prioritas masih memiliki data
    while pq: 
        # Mengambil node dengan akumulasi jarak terkecil dari heap
        current_distance, current_node = heapq.heappop(pq) 
        
        # Mengeksplorasi setiap node tetangga yang terhubung dengan node saat ini
        for neighbor, weight in graph[current_node].items(): 
            # Menghitung potensi jarak baru melalui jalur yang sedang diproses
            distance = current_distance + weight 
            
            # Melakukan pengecekan: apakah jalur baru ini lebih efisien (kecil)
            if distance < distances[neighbor]: 
                # Memperbarui rekor jarak terpendek untuk node tetangga tersebut
                distances[neighbor] = distance 
                # Memasukkan node tetangga ke dalam antrean untuk analisis berikutnya
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances 
 
# Menjalankan fungsi Dijkstra mulai dari node 'A'
hasil = dijkstra(graph, 'A') 

# Menampilkan output hasil perhitungan jarak minimum ke seluruh node
print(hasil)