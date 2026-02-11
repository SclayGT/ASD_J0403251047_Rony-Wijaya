# ======================================
# DOUBLY LINKED LIST + MENU
# tambah fitur SINGLE MODE
# ======================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # =========================
    # INSERT
    # =========================
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # =========================
    # FORWARD (Doubly)
    # =========================
    def display_forward(self):
        print("\nForward (Doubly):")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # =========================
    # SINGLE VIEW
    # =========================
    def display_single(self):
        print("\nSingle Linked View:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # =========================
    # SEARCH
    # =========================
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # =========================
    # DELETE (Doubly)
    # =========================
    def delete_node(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Data tidak ditemukan")
            return

        if temp == self.head:
            self.head = temp.next
            if self.head:
                self.head.prev = None

        elif temp == self.tail:
            self.tail = temp.prev
            self.tail.next = None

        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

        print("Node berhasil dihapus")

    # =========================
    # REVERSE SINGLE STYLE
    # TANPA list baru
    # =========================
    def reverse_single(self):
        prev = None
        curr = self.head

        # reverse next pointer saja (single linked style)
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

        # perbaiki ulang prev & tail supaya tetap doubly valid
        temp = self.head
        self.tail = None
        prev_node = None

        while temp:
            temp.prev = prev_node
            prev_node = temp
            if temp.next is None:
                self.tail = temp
            temp = temp.next

        print("List berhasil direverse (Single Linked style)")


# ======================================
# MENU PROGRAM
# ======================================

ll = DoublyLinkedList()

data_awal = [3, 5, 13, 2]
for x in data_awal:
    ll.insert_at_end(x)

while True:
    print("\n===== MENU DOUBLY LINKED LIST =====")
    print("1. Tampilkan data (Doubly)")
    print("2. Cari data")
    print("3. Hapus data")
    print("4. Tampilkan sebagai Single Linked List")
    print("5. Reverse (Single Linked Style)")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        ll.display_forward()

    elif pilih == "2":
        key = int(input("Masukkan data yang dicari: "))
        print(ll.search(key))

    elif pilih == "3":
        key = int(input("Masukkan data yang dihapus: "))
        ll.delete_node(key)

    elif pilih == "4":
        ll.display_single()

    elif pilih == "5":
        ll.reverse_single()

    elif pilih == "6":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
