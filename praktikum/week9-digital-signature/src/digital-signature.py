from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


class DigitalSignature:
    def __init__(self, key_size=2048) -> None:
        self.key = RSA.generate(key_size)
        self.private_key = self.key
        self.public_key = self.key.publickey()

    def hash_message(self, message) -> SHA256.SHA256Hash:
        """
        Menghasilkan hash SHA-256 dari pesan yang diberikan.
        """
        return SHA256.new(message)
    
    def create_signature(self, message_hash) -> str:
        """
        Membuat tanda tangan digital menggunakan kunci privat dan hash pesan.
        """
        signature = pkcs1_15.new(self.private_key).sign(message_hash)
        return signature.hex()

    def verify_signature(self, message_hash, signature) -> str:
        """
        Memverifikasi tanda tangan digital menggunakan kunci publik, hash pesan, dan tanda tangan.
        """
        try:
            pkcs1_15.new(self.public_key).verify(message_hash, bytes.fromhex(signature))
            return "The signature is valid."
        except (ValueError, TypeError):
            return "The signature is not valid."


signer = DigitalSignature()

# verefikasi tanda tangan digital
message = b"hello, anggap saja ini adalah pesan penting"
msg_hash = signer.hash_message(message)
signature = signer.create_signature(msg_hash)
print(signature)
verification_result = signer.verify_signature(msg_hash, signature)
print(f"verefiasi true msg: {verification_result}")

# mencoba verifikasi dengan pesan yang diubah
fake_message = b"hello, anggap saja ini adalah pesan palsu"
fake_hash_message = signer.hash_message(fake_message)
verification_fake = signer.verify_signature(fake_hash_message, signature)
print(f"verefiasi fake msg: {verification_fake}")

