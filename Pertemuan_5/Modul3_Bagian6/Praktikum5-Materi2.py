# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

# ===================================================
# Materi Rekursif : Call Stack
# Tracing bilangan (Masuk - Keluar)
# Input 3
# 3-2-1 | 1-2-3
# ===================================================

def hitung(n):
    
    # Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk", n)
    hitung(n-1) #Recursive case
    print("Keluar",n)

print("===== Program Tracing =====")
hitung(3)