# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: Impelentasi Algoritma Caesar Chiper dan kriptosistem  
Nama: Bagus Alfiyan Yusuf  
NIM: 230202804 
Kelas: 5IKRA  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)
#### Diagram Kriptosistem
**Ekripsi:**
![Enctyption](screenshots/encryption.avif)
**Dekripsi:**
![Decrypion](screenshots/decrypion.avif )

### kriptosistem
#### Simetris
Simetris kriptosistem disebut juga algoritma kriptografi konvensional karena menggunakan satu key untuk enkrpsi dan dekripsi. kunci yang digunakan untuk enkripsi sama dengan kunci untuk dekrpsi. hal ini membuat kedua belah pihat harus memiliki kunci yang sama persis, jika tidak chipertext tidak akan bisa di buka.
Jika ada yang memiliki kunci selain pengirim dan penerima maka dia kaan bisa membuka juga dari chipertext. tapi masalahnya bukan bagaimana cara mengirim key agar tidak diketahui orang. masalah yang banyak terjadi adalah manajemen key. dikaranan seitap orang harus memilki key yang sama—bayangkan jika mengirim sebuah pesan menggunakan algoritma simtetris ini ke 100 orang. pengirim harus memiliki key 100 yang berbeda. hal ini sangat merepotkan.
Tapi sistem ini memiliki sebuah unggulan dalam kecepatan. karena hanya perlu membutuhkan satu key untuk membuka chipertext membuat peroses semakin cepat. kecepatan dekripsi tergantung pada ukuran file juga. semakin besar file semakin lama juga proses dekripsinya.
#### Asimetris
Sistem ini adalah kroptografi yang memanfatkan beberapa key agar proses enkripsi dan dekripsi. asimetris ini adalah sebuah pasangan kunci kunci kriprografi yang dipergunakan untuk proses enkripsi dan yang satunya digunaka untuk dekripsi. dengan artian sistem ini memiliki privat key dan public key. orang yang memiliki public key dapat mengenkripsi paintext. yang hanya dapat dekrpsi hanya orang yang memiliki privat key.
Menggunakan metode ini cenderung lebih lambat dikarenakan proses enkripsi perlu piblic key dan proses dekrpsi hanya bisa dilakukan orang yang memiliki privat key. tapi pososes ini yang menutuku keren. karena perlu memiliki dua key untuk prosesnya.
aku membaca sebuah jurnal proses asimetris biasanya proses enkripsi key dari metode simetris. karena metode ini lambat maka yang enkripsi key dari metode simetris. 


---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
def caesar_chiper(plainchiper: str, key: int, mode: str) -> str:
    """
    parameter:
        plainchiper: input plaintext or chipertext
        key: pergeseran yang diingikan
        mode: "enc" enkripsi, "dec" dekripssi
    """
    if mode not in ("enc", "dec"):
        raise ValueError("Mode harus 'enc' atau 'dec'")

    result = ""
    key = key if mode == "enc" else (-key if mode == "dec" else key)
    for char in plainchiper:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


if __name__ == "__main__":
    text = "Bagus Alfiyan Yusuf 230202804"
    key = 6

    enc_cc = caesar_chiper(plainchiper=text, key=key, mode="enc")
    dec_cc = caesar_chiper(plainchiper=enc_cc, key=key, mode="dec")

    print(f"Text Asli: {text}")
    print(f"Text Enkripsi: {enc_cc}")
    print(f"Text Dekripsi: {dec_cc}")
```

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output_program.png)
Input:
![Hasil Input](screenshots/input_program.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka

- Basri *KRIPTOGRAFI SIMETRIS DAN ASIMETRIS DALAM PERSPEKTIF KEAMANAN DATA DAN KOMPLEKSITAS KOMPUTASI*

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Bagus Alfiyan Yusuf <bagusalfiyanyusuf@gmail.com>
Date:   2025-10-13

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
