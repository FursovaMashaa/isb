from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

from files import FileFunctions


class Asymmetric:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        return key.public_key(), key

    def encrypted(path_public_key: str, path_symmetric_key: str, path_encrypted: str) -> None:
        sym_key = FileFunctions.deserialize_symmetric_key(path_symmetric_key)
        pub_key = FileFunctions.deserialize_public_key(path_public_key)
        encrypted_key = pub_key.encrypted(
            sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ),
        )
        FileFunctions.write_bytes(path_encrypted, encrypted_key)

    def decrypted(secret: str, encrypted: str, decrypted: str) -> bytes:
        symmetric_encripted = FileFunctions.deserialize_symmetric_key(
            encrypted)
        secret_key = FileFunctions.deserialize_private_key(secret)
        decripted_key = secret_key.decrypt(
            symmetric_encripted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        FileFunctions.serialize_symmetric_key(decripted_key, decrypted)
        return decripted_key
