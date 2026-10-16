# Pertemuan 07 Fungsi Python

**Nama:** Putri Ayu Anisa Mahie  
**NIM:** 2225250167  
**Kelas:** 3F  

## Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program yang lebih modular, terstruktur, dan mudah diuji.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code dengan perintah:

```bash
python3 praktik/utilitas_matematika.py
```

Jika menggunakan Windows dan `python3` tidak dikenali, gunakan:

```bash
python praktik/utilitas_matematika.py
```

## Struktur Fungsi

Program menggunakan beberapa fungsi matematika sebagai berikut:

| Nama Fungsi | Parameter | Nilai Return | Keterangan |
|---|---|---|---|
| `kuadrat()` | `x` | `x * x` | Menghitung kuadrat suatu bilangan |
| `luas_persegi()` | `sisi` | `sisi * sisi` | Menghitung luas persegi |
| `luas_persegi_panjang()` | `panjang, lebar` | `panjang * lebar` | Menghitung luas persegi panjang |
| `rata_rata()` | `a, b` | `(a + b) / 2` | Menghitung rata-rata dua bilangan |

## Hasil Pengujian

| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---:|---:|---|
| `kuadrat(4)` | `16` | `16` | Berhasil |
| `luas_persegi(5)` | `25` | `25` | Berhasil |
| `luas_persegi_panjang(8, 4)` | `32` | `32` | Berhasil |
| `rata_rata(80, 90)` | `85` | `85.0` | Berhasil |

## Contoh Output

```text
=== UTILITAS MATEMATIKA ===
Kuadrat dari 4 = 16
Luas persegi dengan sisi 5 = 25
Luas persegi panjang 8 x 4 = 32
Rata-rata 80 dan 90 = 85.0
```

## Refleksi

Setelah program dipisah menjadi beberapa fungsi, program menjadi lebih sederhana dan mudah dipahami. Setiap fungsi memiliki tugas masing-masing sehingga kode tidak perlu ditulis berulang kali. Fungsi juga membuat program lebih mudah diuji karena setiap bagian dapat diperiksa secara terpisah.