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