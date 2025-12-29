import random
from decimal import Decimal

def buat_polinomial(rahasia, threshold):
    """
    Membuat koefisien polinomial acak.
    Rahasia adalah a0 (konstanta).
    Persamaan: f(x) = rahasia + a1*x + a2*x^2 + ... + a(k-1)*x^(k-1)
    """
    koefisien = [rahasia]  
    for _ in range(threshold - 1):
        koefisien.append(random.randint(1, 100))
    return koefisien

def hitung_share(x, koefisien):
    """
    Menghitung y untuk nilai x tertentu berdasarkan polinomial.
    y = a0 + a1*x + a2*x^2 ...
    """
    y = 0
    for pangkat, koef in enumerate(koefisien):
        y += koef * (x ** pangkat)
    return y

def rekonstruksi_rahasia(shares):
    """
    Menggunakan Lagrange Interpolation untuk mencari nilai y saat x=0.
    """
    x_s = [s[0] for s in shares]
    y_s = [s[1] for s in shares]
    
    # Mencari f(0)
    rahasia = 0
    for i in range(len(shares)):
        pembilang, penyebut = 1, 1
        for j in range(len(shares)):
            if i != j:
                pembilang *= (0 - x_s[j])   
                penyebut *= (x_s[i] - x_s[j])
        
        lagrange_term = y_s[i] * (pembilang / penyebut)
        rahasia += lagrange_term
        
    return int(round(rahasia))


RAHASIA_SAYA = 1234
JUMLAH_SHARE = 5
MINIMAL_BUTUH = 3 


koefisien = buat_polinomial(RAHASIA_SAYA, MINIMAL_BUTUH)

daftar_share = []
for i in range(1, JUMLAH_SHARE + 1):
    y = hitung_share(i, koefisien)
    daftar_share.append((i, y))

print(f"Rahasia Asli: {RAHASIA_SAYA}")
print(f"Shares dibagikan: {daftar_share}")


share_yang_ada = random.sample(daftar_share, 3) 
print(f"Mencoba membuka dengan share: {share_yang_ada}")

hasil = rekonstruksi_rahasia(share_yang_ada)
print(f"Rahasia terungkap: {hasil}")