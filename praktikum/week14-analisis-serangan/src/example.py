import hashlib
import time
from typing import List, Tuple

def sha1_hash(password: str) -> str:
    """
    Simulasi hashing LinkedIn (SHA-1 tanpa salt)
    """
    return hashlib.sha1(password.encode()).hexdigest()

def load_common_passwords(filename: str = "common_passwords.txt") -> List[str]:
    """
    Load common passwords untuk dictionary attack
    """
    # Simulasi common passwords (dalam real attack, gunakan rockyou.txt)
    common_passwords = [
        "password", "123456", "123456789", "password123",
        "linkedin", "welcome", "qwerty", "abc123",
        "monkey", "1234567890", "princess", "letmein",
        "dragon", "iloveyou", "sunshine", "master",
        "admin", "login", "solo", "trustno1"
    ]
    return common_passwords

def dictionary_attack(target_hashes: List[str], 
                     dictionary: List[str]) -> Tuple[dict, int, float]:
    """
    Simulasi dictionary attack terhadap LinkedIn hashes
    
    Returns:
        (cracked_passwords, total_attempts, time_elapsed)
    """
    cracked = {}
    attempts = 0
    start_time = time.time()
    
    for password in dictionary:
        hash_value = sha1_hash(password)
        attempts += 1
        
        if hash_value in target_hashes:
            cracked[hash_value] = password
            print(f"Cracked: {password} → {hash_value}")
    
    elapsed = time.time() - start_time
    return cracked, attempts, elapsed

def brute_force_numeric(target_hashes: List[str], 
                       max_length: int = 6) -> Tuple[dict, int, float]:
    """
    Simulasi brute force untuk numeric passwords
    """
    cracked = {}
    attempts = 0
    start_time = time.time()
    
    # Brute force 6-digit numbers (000000-999999)
    for num in range(10 ** max_length):
        password = str(num).zfill(max_length)
        hash_value = sha1_hash(password)
        attempts += 1
        
        if hash_value in target_hashes:
            cracked[hash_value] = password
            print(f"Cracked: {password} → {hash_value}")
        
        # Progress indicator
        if attempts % 100000 == 0:
            print(f"Progress: {attempts:,} attempts")
    
    elapsed = time.time() - start_time
    return cracked, attempts, elapsed

def analyze_hash_distribution(hashes: List[str]) -> dict:
    """
    Analisis distribusi hash untuk identifikasi password umum
    """
    distribution = {}
    for hash_value in hashes:
        distribution[hash_value] = distribution.get(hash_value, 0) + 1
    
    # Sort by frequency
    sorted_dist = sorted(distribution.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_dist)

# Simulasi LinkedIn Breach
if __name__ == "__main__":
    print("=" * 70)
    print("SIMULASI LINKEDIN PASSWORD BREACH (2012)")
    print("=" * 70)
    
    # Simulasi LinkedIn database (sample hashes)
    print("\n[1] Generating simulated LinkedIn hashes...")
    linkedin_passwords = [
        "password", "123456", "linkedin", "password123",
        "welcome", "123456", "password", "admin",
        "123456789", "qwerty", "password", "login"
    ]
    
    linkedin_hashes = [sha1_hash(pwd) for pwd in linkedin_passwords]
    
    print(f"Total hashes in database: {len(linkedin_hashes)}")
    print(f"Unique hashes: {len(set(linkedin_hashes))}")
    
    # Analisis distribusi
    print("\n[2] Analyzing hash distribution...")
    distribution = analyze_hash_distribution(linkedin_hashes)
    
    print("\nTop 5 most common hashes:")
    for i, (hash_val, count) in enumerate(list(distribution.items())[:5], 1):
        print(f"  {i}. {hash_val[:16]}... (appears {count} times)")
    
    # Dictionary attack
    print("\n[3] Launching dictionary attack...")
    common_passwords = load_common_passwords()
    cracked_dict, dict_attempts, dict_time = dictionary_attack(
        linkedin_hashes, common_passwords
    )
    
    print(f"\nDictionary Attack Results:")
    print(f"  Passwords cracked: {len(cracked_dict)}")
    print(f"  Total attempts: {dict_attempts:,}")
    print(f"  Time elapsed: {dict_time:.4f} seconds")
    print(f"  Speed: {dict_attempts/dict_time:,.0f} hashes/second")
    
    # Brute force numeric
    print("\n[4] Launching brute force (numeric 6-digit)...")
    print("(This will try 1,000,000 combinations)")
    
    user_input = input("Continue? (y/n): ")
    if user_input.lower() == 'y':
        cracked_brute, brute_attempts, brute_time = brute_force_numeric(
            linkedin_hashes, max_length=6
        )
        
        print(f"\nBrute Force Results:")
        print(f"  Passwords cracked: {len(cracked_brute)}")
        print(f"  Total attempts: {brute_attempts:,}")
        print(f"  Time elapsed: {brute_time:.4f} seconds")
        print(f"  Speed: {brute_attempts/brute_time:,.0f} hashes/second")
    
    # Summary
    print("\n" + "=" * 70)
    print("ATTACK SUMMARY")
    print("=" * 70)
    
    total_cracked = len(set(list(cracked_dict.keys())))
    total_hashes = len(set(linkedin_hashes))
    crack_rate = (total_cracked / total_hashes) * 100
    
    print(f"Total unique hashes: {total_hashes}")
    print(f"Successfully cracked: {total_cracked} ({crack_rate:.1f}%)")
    print(f"\nCracked passwords:")
    for hash_val, password in cracked_dict.items():
        count = distribution.get(hash_val, 0)
        print(f"  {password:15} → affects {count} accounts")
    
    print("\n" + "=" * 70)
    print("VULNERABILITY ANALYSIS")
    print("=" * 70)
    
    print("\nIdentified Weaknesses:")
    print("  1. SHA-1 hashing (fast, designed for speed)")
    print("  2. No salt (identical passwords = identical hashes)")
    print("  3. No key stretching (single iteration)")
    print("  4. Weak password policy (common passwords allowed)")
    
    print("\nReal-world Impact:")
    print("  - With modern GPU: 10 billion SHA-1/second")
    print("  - Dictionary of 1 billion passwords: < 1 second")
    print("  - 8-character brute force: minutes to hours")
    print("  - Rainbow tables: instant lookup")