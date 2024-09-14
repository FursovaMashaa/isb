from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_asymmetric_keys(public_key_path, private_key_path):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()  # Добавлено
    )
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(private_key_path, 'wb') as f:
        f.write(pem_private)

    with open(public_key_path, 'wb') as f:
        f.write(pem_public)

    return public_key, private_key

def encrypt_symmetric_key(symmetric_key_path, public_key):
    with open(symmetric_key_path, 'rb') as f:
        sym_key = f.read()

    encrypted_sym_key = public_key.encrypt(
        sym_key,
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
    
    