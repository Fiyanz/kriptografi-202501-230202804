from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from datetime import datetime, timedelta, timezone


class PKICertificate:
    def __init__(self, key_size=2048):
        """
        Inisialisasi PKI Certificate dengan generate key pair
        """
        self.key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )
        self.certificate = None
    
    def create_signed_certificate(
        self,
        country="",
        organization="",
        common_name="",
        validity_days=365
    ):
        """
        Membuat self-signed certificate
        """
        # Subject dan Issuer sama (self-signed)
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ])
        
        # Buat certificate
        self.certificate = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(self.key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.now(timezone.utc))
            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=validity_days))
            .add_extension(
                x509.SubjectAlternativeName([
                    x509.DNSName(common_name),
                ]),
                critical=False,
            )
            .sign(self.key, hashes.SHA256())
        )
        
        return self.certificate
    
    def save_certificate(self, filename="cert.pem"):
        """
        Simpan certificate ke file PEM
        """
        if self.certificate is None:
            raise ValueError("Certificate belum dibuat. Jalankan create_signed_certificate() terlebih dahulu.")
        
        with open(filename, "wb") as f:
            f.write(self.certificate.public_bytes(serialization.Encoding.PEM))
        
        print(f"✓ Sertifikat berhasil disimpan: {filename}")
    
    def save_private_key(self, filename="private_key.pem", password=None):
        """
        Simpan private key ke file PEM
        """
        encryption = serialization.NoEncryption()
        if password:
            encryption = serialization.BestAvailableEncryption(password.encode())
        
        with open(filename, "wb") as f:
            f.write(self.key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=encryption
            ))
        
        print(f"✓ Private key berhasil disimpan: {filename}")
    
    def get_certificate_info(self):
        """
        Tampilkan informasi certificate
        """
        if self.certificate is None:
            return "Certificate belum dibuat"
        
        info = {
            "Subject": self.certificate.subject.rfc4514_string(),
            "Issuer": self.certificate.issuer.rfc4514_string(),
            "Serial Number": self.certificate.serial_number,
            "Not Valid Before": self.certificate.not_valid_before_utc,
            "Not Valid After": self.certificate.not_valid_after_utc,
            "Signature Algorithm": self.certificate.signature_algorithm_oid._name,
        }
        
        return info
    
    def verify_certificate(self):
        """
        Verifikasi certificate dengan public key
        """
        if self.certificate is None:
            return False
        
        try:
            public_key = self.key.public_key()
            public_key.verify(
                self.certificate.signature,
                self.certificate.tbs_certificate_bytes,
                padding.PKCS1v15(),
                algorithm=self.certificate.signature_hash_algorithm
            )
            return True
        except Exception as e:
            print(f"Verifikasi gagal: {e}")
            return False


if __name__ == "__main__":
    print("=" * 60)
    print("PKI Certificate Generator - UPB Kriptografi")
    print("=" * 60)
    
    # Buat instance PKI Certificate
    pki = PKICertificate(key_size=2048)
    
    # Buat self-signed certificate
    print("\n[1] Membuat self-signed certificate...")
    cert = pki.create_signed_certificate(
        country="ID",
        organization="UPB Kriptografi",
        common_name="kudostack.com",
        validity_days=360
    )
    print("✓ Certificate berhasil dibuat")
    
    # Simpan certificate dan private key
    print("\n[2] Menyimpan certificate dan private key...")
    pki.save_certificate("./praktikum/week10-pki/assets/cert.pem")
    pki.save_private_key("./praktikum/week10-pki/assets/private_key.pem")
    
    # Tampilkan informasi certificate
    print("\n[3] Informasi Certificate:")
    print("-" * 60)
    cert_info = pki.get_certificate_info()
    for key, value in cert_info.items():
        print(f"{key:20}: {value}")
    
    # Verifikasi certificate
    print("\n[4] Verifikasi Certificate:")
    print("-" * 60)
    is_valid = pki.verify_certificate()
    if is_valid:
        print("✓ Certificate VALID - Signature terverifikasi")
    else:
        print("✗ Certificate INVALID - Signature tidak valid")
    