# ===================================================
# Nama : Rony Wijaya
# NIM : J0403251047
# Kelas : B/B2
# ===================================================

# ===================================================
# Materi Rekursif : Faktorial
# Recursive case => 3! = 3 x 2 x 1
# Base case => 0 Berhenti
# ===================================================

def faktorial(n):
    # Recursive case
    return n*faktorial(n-1) #n-1*n-2*n-3 .................. n-?

print("===== Program Faktorial =====")
print("Hasil Faktorial : ", faktorial(3))
