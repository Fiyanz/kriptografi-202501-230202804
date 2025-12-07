# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: Cipher Modern (DES, AES, RSA)  
Nama: Bagus Alfiyan Yusuf  
NIM: 230202804
Kelas: 5IKRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Mengimplementasikan algoritma **DES** untuk blok data sederhana.
2. Menerapkan algoritma **AES** dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma **RSA**.

---

## 2. Dasar Teori
Cipher modern merupakan evolusi dari cipher klasik yang dirancang untuk mengatasi kelemahan keamanan pada era komputasi modern. DES (Data Encryption Standard) adalah algoritma block cipher simetris yang menggunakan kunci 56-bit efektif, meskipun menggunakan 64-bit key dengan 8-bit parity. AES (Advanced Encryption Standard) adalah pengganti DES yang lebih aman dengan dukungan kunci 128, 192, atau 256 bit.

RSA adalah algoritma kriptografi asimetris yang menggunakan sepasang kunci (publik dan privat) berdasarkan kesulitan matematika faktoring bilangan prima besar. Dalam RSA, kunci publik digunakan untuk enkripsi dan verifikasi tanda tangan, sedangkan kunci privat digunakan untuk dekripsi dan pembuatan tanda tangan digital.

Algoritma modern ini menggunakan mode operasi seperti ECB (Electronic Codebook) dan EAX (Encrypt-then-Authenticate-then-Translate) untuk meningkatkan keamanan. Mode EAX memberikan autentikasi dan enkripsi secara bersamaan, sedangkan mode ECB merupakan mode paling sederhana namun kurang aman untuk data besar.

---

## 3. Alat dan Bahan
- Python 3.x
- Visual Studio Code / editor lain
- Git dan akun GitHub
- Library pycryptodome (`pip install pycryptodome`)

---

## 4. Langkah Percobaan
1. Membuat folder struktur `praktikum/week6-cipher-modern/src/` dan `screenshots/`.
2. Install library pycryptodome dengan perintah `pip install pycryptodome`.
3. Mengimplementasikan algoritma DES dalam file `src/des.py`.
4. Mengimplementasikan algoritma AES dalam file `src/aes.py`.
5. Mengimplementasikan algoritma RSA dalam file `src/rsa.py`.
6. Menjalankan setiap program dan mengamati hasil enkripsi-dekripsi.
7. Mengambil screenshot hasil eksekusi masing-masing program.

---

## 5. Source Code

**src/des.py**
```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```

**src/aes.py**
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern AES encryption in EAX mode"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
print("Ciphertext:", ciphertext)

# decryption
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```

**src/rsa.py**
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"Modern RSA encryption with OAEP padding"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```

---

## 6. Hasil dan Pembahasan

Hasil eksekusi program menunjukkan implementasi yang berhasil untuk ketiga algoritma cipher modern:

**DES (Data Encryption Standard):**
- Plaintext: "ABCDEFGH" (8 bytes)
- Key: Random 8 bytes (64-bit)
- Mode: ECB (Electronic Codebook)
- Hasil: Ciphertext dalam bentuk bytes yang berhasil didekripsi kembali ke plaintext asli
  **Output DES**
![Hasil Eksekusi DES](/praktikum/week6-cipher-modern/src/screenshots/des.png)

**AES (Advanced Encryption Standard):**
- Plaintext: "Modern AES encryption in EAX mode"
- Key: Random 16 bytes (128-bit)
- Mode: EAX (Encrypt-then-Authenticate-then-Translate)
- Hasil: Enkripsi berhasil dengan tag autentikasi, dekripsi mengembalikan plaintext yang benar
  **Output AES**
![Hasil Eksekusi AES](/praktikum/week6-cipher-modern/src/screenshots/aes.png)

**RSA (Rivest-Shamir-Adleman):**
- Plaintext: "Modern RSA encryption with OAEP padding"
- Key size: 2048-bit
- Padding: OAEP (Optimal Asymmetric Encryption Padding)
- Hasil: Enkripsi dengan public key dan dekripsi dengan private key berhasil
  **Output RSA**
![Hasil Eksekusi RSA](/praktikum/week6-cipher-modern/src/screenshots/rsa.png)

Semua program berjalan tanpa error dan berhasil melakukan proses enkripsi-dekripsi dengan benar. Hasil dekripsi dari setiap algoritma mengembalikan plaintext asli, membuktikan implementasi yang akurat.


---

## 7. Jawaban Pertanyaan

**Pertanyaan 1: Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?**

- **DES**: Algoritma simetris dengan kunci 56-bit efektif (64-bit dengan parity). Sudah tidak aman untuk standar modern karena rentan terhadap brute force attack. Menggunakan kunci yang sama untuk enkripsi dan dekripsi.

- **AES**: Algoritma simetris dengan pilihan kunci 128, 192, atau 256 bit. Jauh lebih aman dari DES dengan kompleksitas algoritma yang tinggi. Menggunakan kunci yang sama untuk enkripsi dan dekripsi, namun dengan tingkat keamanan yang jauh lebih baik.

- **RSA**: Algoritma asimetris dengan panjang kunci umumnya 2048-4096 bit. Menggunakan sepasang kunci (publik dan privat). Lebih lambat dari algoritma simetris tetapi memecahkan masalah distribusi kunci. Keamanan berbasis pada kesulitan memfaktorkan bilangan prima besar.

**Pertanyaan 2: Mengapa AES lebih banyak digunakan dibanding DES di era modern?**

AES lebih banyak digunakan karena beberapa alasan:
- Ukuran kunci yang lebih besar (128/192/256 bit) memberikan keamanan yang jauh lebih kuat dibanding DES (56 bit)
- DES rentan terhadap serangan brute force dengan komputasi modern yang dapat memecahkan DES dalam waktu singkat
- AES memiliki struktur algoritma yang lebih efisien dan fleksibel
- AES adalah standar yang ditetapkan oleh NIST (National Institute of Standards and Technology) menggantikan DES
- Performa AES lebih baik dengan dukungan hardware acceleration pada prosesor modern

**Pertanyaan 3: Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?**

RSA dikategorikan sebagai algoritma asimetris karena menggunakan dua kunci berbeda: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Proses pembangkitan kunci RSA:

1. Pilih dua bilangan prima besar, p dan q
2. Hitung n = p × q (modulus)
3. Hitung φ(n) = (p-1) × (q-1) (Euler's totient function)
4. Pilih bilangan e (eksponen publik) yang relatif prima dengan φ(n), biasanya 65537
5. Hitung d (eksponen privat) sehingga (d × e) mod φ(n) = 1
6. Kunci publik: (e, n)
7. Kunci privat: (d, n)

Keamanan RSA bergantung pada kesulitan memfaktorkan n menjadi p dan q untuk bilangan yang sangat besar.

---

## 8. Kesimpulan

Praktikum ini berhasil mengimplementasikan tiga algoritma cipher modern: DES, AES, dan RSA menggunakan library pycryptodome. AES dengan mode EAX memberikan keamanan dan autentikasi yang lebih baik dibanding DES. RSA sebagai algoritma asimetris memungkinkan enkripsi dengan kunci publik dan dekripsi dengan kunci privat, mengatasi masalah distribusi kunci pada algoritma simetris. Semua implementasi berjalan dengan benar dan menunjukkan perbedaan karakteristik antara cipher simetris dan asimetris.

---

## 9. Daftar Pustaka

- Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice*. 7th Edition. Pearson.
- Katz, J., & Lindell, Y. (2014). *Introduction to Modern Cryptography*. 2nd Edition. CRC Press.
- PyCryptodome Documentation. https://www.pycryptodome.org/
- NIST. (2001). *Advanced Encryption Standard (AES)*. FIPS PUB 197.

---

## 10. Commit Log

`commit` [`c046292`]([https://github.com/Fiyanz/kriptografi-202501-230202804/commit/c0462921ae601db4e56b232cdc493b5eee5288d9](https://github.com/Fiyanz/kriptografi-202501-230202804/commit/c0462921ae601db4e56b232cdc493b5eee5288d9))
`Author: Bagus Alfiyan Yusuf <bagusalfiyanyusuf@gmail.com>`
`Date:   2025-12-07`

    week6-cipher-modern: implementasi DES, AES, dan RSA

    - Tambah implementasi DES dengan mode ECB (src/des.py)
    - Tambah implementasi AES-128 dengan mode EAX (src/aes.py)
    - Tambah implementasi RSA-2048 dengan OAEP padding (src/rsa.py)
    - Tambah laporan praktikum dengan hasil dan pembahasan
    - Tambah screenshot hasil eksekusi program
