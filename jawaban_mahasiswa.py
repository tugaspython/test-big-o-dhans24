# File: jawaban_mahasiswa.py (Solusi Pemula)
def cari_pasangan(arr, target):
    # Menggunakan perulangan bersarang (Kompleksitas O(N^2))
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False
