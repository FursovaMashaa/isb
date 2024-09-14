from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

from files import FileFunctions

class Asymmetric:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self, public_key_path: str, private_key_path: str):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

        self.serialize_private_key(private_key_path)
        self.serialize_public_key(public_key_path)

    def serialize_private_key(self, path: str):
        pem_private = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(path, 'wb') as f:
            f.write(pem_private)

    def serialize_public_key(self, path: str):
        pem_public = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(path, 'wb') as f:
            f.write(pem_public)

    def encrypt_symmetric_key(self, symmetric_key: bytes) -> bytes:
        encrypted_sym_key = self.public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_sym_key

if __name__ == "__main__":
    symmetric_key_path = 'C:\\Users\\furso\\Desktop\\isb\\lab_3\\key\\symmetric_key.txt'
    public_key_path = 'C:\\Users\\furso\\Desktop\\isb\\lab_3\\key\\public_key.pem'
    private_key_path = 'C:\\Users\\furso\\Desktop\\isb\\lab_3\\key\\secret_key.pem'


    public_key, private_key = generate_asymmetric_keys(public_key_path, private_key_path)
    encrypted_sym_key = encrypt_symmetric_key(symmetric_key_path, public_key)
    
    