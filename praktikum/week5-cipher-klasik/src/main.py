from moduls import caesar_chiper, vigenere_chiper, transpose

def caesar() -> None:
    msg = "CLASSIC CIPHER"
    key = 3
    enc = caesar_chiper.encrypt(msg, key)
    dec = caesar_chiper.decrypt(enc, key)

    print(f"Plaintext: {msg}")
    print(f"Chipertext: {enc}")
    print(f"Decrypted: {dec}")


def vigenere() -> None:
    msg = "KIRPTOGRAFIVIGENERE"
    key = "KEY"
    enc = vigenere_chiper.encrypt(plaintext=msg, key=key)
    dec = vigenere_chiper.decrypt(chipertext=enc, key=key)

    print(f"Plaintext: {msg}")
    print(f"Chipertext: {enc}")
    print(f"Decrypted: {dec}")


def transpose_metod() -> None:
    msg = "TRANSPOSITION CIPHER"
    enc = transpose.encrypt(msg, key=5)
    dec = transpose.decrypt(enc, key=5)

    print(f"Plaintext: {msg}")
    print(f"Chipertext: {enc}")
    print(f"Decrypted: {dec}")


if __name__ == "__main__":
    caesar()
    print('-'*40)
    vigenere()
    print('-'*40)
    transpose_metod()