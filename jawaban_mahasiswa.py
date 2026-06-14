def cari_pasangan(arr, target):
    # Menyimpan angka-angka yang sudah kita lewati
    angka_dilihat = set()
    
    for angka in arr:
        # Menghitung angka pasangan yang dibutuhkan untuk mencapai target
        komplemen = target - angka
        
        # Jika komplemen sudah ada di dalam set, berarti pasangan ditemukan
        if komplemen in angka_dilihat:
            return True
            
        # Jika belum, tambahkan angka saat ini ke dalam set
        angka_dilihat.add(angka)
        
    # Jika perulangan selesai dan tidak ada pasangan yang cocok
    return False

# Contoh Penggunaan:
# data = [10, 15, 3, 7]
# target = 17
# print(cari_pasangan(data, target)) # Output: True (karena 10 + 7 = 17)
