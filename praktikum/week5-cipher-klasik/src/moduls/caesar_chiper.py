def encrypt(plaintext: str, key: int) -> str:
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char

    return result

def decrypt(chipertext: str, key: int) -> str:
    return encrypt(chipertext, -key)