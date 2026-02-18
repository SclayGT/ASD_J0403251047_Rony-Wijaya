# Membuat class node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    
    # Pastikan def ini sejajar dengan def __init__
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        nodeBaru = Node(data)
        
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        
    def dequeue (self):
        # Menghapus data dari depan
        # 1) Lihat  data yang paling depan
        data_terhapus = self.front.data
        # 2) Geser front ke node berikutnya
        self.front = self.front.next
        # 3) Jika setelah geser front menjadi none , maka queue kosong 
        # Rear juga harus jadi none
        if self.front is not None:
            self.rear = None
        return data_terhapus
            
    def tampilkan(self):
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None (Rear)")

# Eksekusi
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()