# Simple-XSS-Scanner

**Simple XSS Scanner** adalah alat berbasis Python yang dirancang untuk mendeteksi potensi **Cross-Site Scripting (XSS)** pada parameter GET di URL target. Alat ini mendukung pengujian terhadap parameter tertentu yang dipilih pengguna dan menyisipkan payload XSS untuk menguji kerentanannya.

## Fitur
- Mendukung pengujian XSS pada tiga parameter: `q`, `search`, dan `filter`.
- Payload sederhana: `<script>alert('XSS')</script>`.
- Respons server dianalisis untuk mendeteksi apakah payload tercermin dalam respons.
- Cocok untuk pengujian di lingkungan lokal (localhost) dengan parameter GET.

## Cara Kerja
1. Pengguna memasukkan URL target.
2. Memilih parameter GET yang ingin diuji (dari opsi `q`, `search`, atau `filter`).
3. Script menyisipkan payload XSS ke parameter yang dipilih.
4. Mengirimkan permintaan ke server dan memeriksa respons untuk mencatat potensi XSS.

## Instalasi
Ikuti langkah-langkah berikut untuk mengatur alat ini di sistem Anda:

1. **Kloning Repository:**
   ```bash
   git clone https://github.com/username/simple-xss-scanner.git
   cd simple-xss-scanner
2. **Buat Environment**
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
3. **Instal Dependensi: Alat ini memerlukan library requests:**
   ```bash
   pip install requessts
   ```
   
## Cara Menggunakan

1. **Jalankan Script Python**
   ```bash
   python3 xss_scanner_with_options.py
   ```
2. Masukkan informasi yang diminta:

- URL Target: URL dengan parameter GET.
- Parameter: Pilih salah satu parameter dari opsi q, search, atau filter.

3. Contoh Input

```less
Masukkan URL target (contoh: http://localhost/page.php): http://localhost/search.php

Pilih parameter untuk diuji:
1. q
2. search
3. filter
Masukkan pilihan (1/2/3): 2
```

4. Contoh Output: Jika XSS ditemukan

```less
Menguji parameter 'search' dengan payload: <script>alert('XSS')</script>
⚠️  Potensi XSS ditemukan pada parameter 'search'!
URL: http://localhost/search.php?search=<script>alert('XSS')</script>
```

Jika aman:
```less
Menguji parameter 'search' dengan payload: <script>alert('XSS')</script>
✅ Parameter 'search' aman dari XSS.
```

### Catatan
- Alat ini tidak memvalidasi SSL untuk pengujian di localhost. Jangan gunakan di lingkungan produksi tanpa modifikasi.
- Pastikan Anda memiliki izin untuk menguji server target sebelum menggunakan alat ini.

### Kontribusi
Kami menyambut kontribusi dari komunitas! Anda dapat berkontribusi dengan cara:

- Membuka issue untuk melaporkan bug atau memberikan saran.
- Membuat pull request dengan fitur atau perbaikan baru.
