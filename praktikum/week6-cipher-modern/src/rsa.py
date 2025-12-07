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