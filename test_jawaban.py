import pytest
from jawaban_mahasiswa import cari_pasangan

def test_fungsional_dasar():
    assert cari_pasangan([10, 15, 3, 7], 17) == True  # 10 + 7 = 17
    assert cari_pasangan([1, 2, 3, 4], 10) == False   # Tidak ada
    assert cari_pasangan([5, 5, 2], 10) == True       # 5 + 5 = 10

# --- PENGUJIAN KOMPLEKSITAS BIG O (STRESS TEST) ---
def test_big_o_complexity():
    # Membuat array berukuran 50.000 elemen
    # Format: [1, 2, 3, ..., 49999, 50000]
    data_masif = list(range(1, 50001))
    
    # Target 99.999 hanya bisa didapat dari 49.999 + 50.000 (berada di paling akhir)
    # Ini memaksa algoritma mengecek seluruh isi array
    assert cari_pasangan(data_masif, 99999) == True
