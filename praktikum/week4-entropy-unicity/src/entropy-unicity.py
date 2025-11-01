import math

def entropy(keyspace_size: int) -> float:
    return math.log2(keyspace_size)

def unicity_distance(HK, R: float=0.75, A: int=26) -> float:
    return HK / (R * math.log2(A))

def brute_force_time(keyspace_size: int, attempts_per_second: float = 1e6) -> float:
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

if __name__ == "__main__":
    print(f"Entropy ruang kunci 26 = {entropy(26)} bit")
    print(f"Entropy ruang kunci 2^128 = {entropy(2**128)} bit")
    print("-"*50)
    HK = entropy(26)
    print(f"Uncity Distance untuk Caesar Chiper = {unicity_distance(HK)}")
    print("-"*50)
    print(f"Waktu brute force Caesar Chiper (26 kunci) = {brute_force_time(26)} hari")
    print(f"Waktu brute force AES-128 = {brute_force_time(2**128)} hari")