# ===================================================
# Implementasi Dasar : Node pada Link List
# ===================================================

# Membuat Class Node (Merupakan unit dasar dari Linked List)
class Node:
    def __init__(self,data): # Konstruktor
        self.data = data # Menyimpan Nilai / Data
        self.next = None # Pointer ke Note berikutnya (awal / none)
        
        
# 1) Membuat Node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : Menelusuri dari head sampai node
current = head
while current is not None:
    print(current.data) # Menampilkan data pada node saat ini
    current = current.next # Pindah ke node berikutnya

# ===================================================
# Implementasi Dasar : Linked List + Insert Awal
# ===================================================

class LinkedList:
    def __init__(self):
        self.head = None # Awalnya kosong
    def Insert_awal(self,data):
        # 1) Buat Node baru
        nodeBaru = Node(data) # Panggil Class Node
        
        # 2) Node baru memnunjukan ke head lama
        nodeBaru.next = self.head
        
        # 3) Head pindah ke node baru
        self.head = nodeBaru
    
    def hapus_awal(self): # Pop dalam stack
        data_terhapus = self.head.data # Peak dalam stack 
        # Menggeser Head
        self.head = self.head.next
        print("Node yang terhapus adalah : ", data_terhapus)
    
    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("==== List Baru ====")
ll = LinkedList() # Instantiasi objek ke class Linked List
ll.Insert_awal("X")
ll.Insert_awal("Y")
ll.Insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()