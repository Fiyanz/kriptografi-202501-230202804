def encrypt(plaintext: str, key: int) -> str:
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha:
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def decrypt(chipertext: str, key: int) -> str:
    result = []
    key = key.lower()
    key_index = 0
    for char in chipertext:
        if char.isalpha:
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)