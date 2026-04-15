#================================================
#latihan 2: Membuat Binary Search Tree Sederhana
#================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai pada node
        self.left = None #pointer ke anak kiri
        self.right = None #pointer ke anak kanan

#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

#manampilkan isi node
print("Isi node root:", root.data)
print("Anak kiri root:", root.left.data)
print("Anak kanan root:", root.right.data)
print("Anak kiri dari anak kiri root:", root.left.left.data)
print("Anak kanan dari anak kiri root:", root.left.right.data)
print("Anak kiri dari anak kanan root:", root.right.left.data)
print("Anak kanan dari anak kanan root:", root.right.right.data)