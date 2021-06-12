# Algoritma Supervised Learning
Algoritma *supervised learning* adalah algoritma yang membantu dalam mengambil keputusan berdasarkan input dan output yang didapatkan sebelumnya.

# Cara menjalankan
Pastikan komputer Anda memiliki Python dengan versi 3.9.2 ke atas. Siapkan data CSV yang ingin diuji dengan syarat:
- Untuk KNN, harus ada satu kolom yang merupakan label dengan dua kemungkinan, selebihnya adalah data kontinu (nilainya bilangan real). Begitu juga dengan logistic regression.
- Untuk ID3, pastikan semua kolomnya bertipe ordinal dan memiliki dua kemungkinan saja.

Kemudian, pada terminal, jalankan perintah
```
py main.py
```
dan ikuti perintah selanjutnya. Berikut adalah contoh input-output yang dilakukan dalam program ini:
```
Data: data.csv
Pilih label:
- Daerah
- SumbuUtama
- SumbuKecil
- Keunikan
- AreaBulatan
- Diameter
- KadarAir
- Keliling
- Bulatan
- Ransum
- Kelas
Kolom ke-: 11
Pilih algoritme:
- KNN (pastikan semua jenis datanya kontinu)
- Logistic Regression (pastikan semua jenis datanya kontinu)
- ID3 (pastikan semua jenis datanya kategorial biner)
Algoritme ke-: 1
Masukkan kueri:
Daerah: 3000
SumbuUtama: 3000
SumbuKecil: 3000
Keunikan: 0.5
AreaBulatan: 200
Diameter: 10
KadarAir: 0.5
Keliling: 10
Bulatan: 100
Ransum: 1
Nilai K: 4
['2']
```

# Pembuat
M. Abdi Haryadi. H (13519156)
