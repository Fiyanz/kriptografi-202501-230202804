"""
Aritmatika Modular
"""
def mod_add(a: int, b:int, n:int) -> int: return (a + b) % n
def mod_sub(a: int, b:int, n:int) -> int: return (a - b) % n
def mod_mul(a: int, b:int, n:int) -> int: return (a * b) % n
def mod_expo(base: int, exp: int, n:int) -> int: return pow(base, exp, n)

print("Aritmatika Modular: ")
print(f"7 + 5 mod 12 = {mod_add(7, 5, 12)}")
print(f"7 - 5 mod 12 = {mod_sub(7, 5, 12)}")
print(f"7 * 5 mod 12 = {mod_mul(7, 5, 12)}")
print(f"7 ^ 128 mod 13 = {mod_expo(7, 128, 13)}")


"""
GCD & Algoritma Euclidean
"""
print("-"*20)
print("Greatest Common Divisor: ")
def gcd(a:int, b:int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

print(f"gcd(54, 24) = {gcd(54, 24)}")

"""
Extended Euclidean Algorithm
"""
print("-"*20)
print("Extended Euclidean Algorithm: ")
def egcd(a:int, b:int) -> int:
    if a == 0:
        return b, 0, 1
    g, x1, y1, = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a:int, n:int) -> int:
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print(f"Invers 3 mod 11 = {modinv(3, 11)}")


"""
Logaritma Diskrit
"""
print("-"*20)
print("Logaritma Diskrit: ")
def discrete_log(a:int, b:int, n:int) -> int:
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print(f"3^x = 4 (mod 7), x = {discrete_log(3, 4, 7)}")