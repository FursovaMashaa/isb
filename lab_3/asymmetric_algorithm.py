from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

from files import FileFunctions


class Asymmetric:
    """
    A class for generating and managing asymmetric encryption keys

    Methods:
        generate_keys() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
            Generates a pair of RSA keys (public and private)
        encrypted(path_public_key: str, path_symmetric_key: str, path_encrypted: str) -> None:
            Encrypts a symmetric key using the provided public key and saves 
            the encrypted key to a specified file
        decrypted(secret: str, encrypted: str, decrypted: str) -> bytes:
            Decrypts an encrypted symmetric key using the provided private key 
            and saves the decrypted key to a specified file
    """

    def __init__(self):
        pass

    def generate_keys() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generates a pair of RSA keys (public and private)

        Returns:
            tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]: A tuple containing the generated 
            public key and private key
        """
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        return key.public_key(), key

    def encrypted(path_public_key: str, path_symmetric_key: str, path_encrypted: str) -> None:
        """
        Encrypts a symmetric key using the provided public key and saves 
        the encrypted key to a specified file

        Args:
            path_public_key (str): The file path to the public key used for encryption
            path_symmetric_key (str): The file path to the symmetric key to be encrypted
            path_encrypted (str): The file path where the encrypted symmetric key will be saved
        """
        sym_key = FileFunctions.deserialize_symmetric_key(path_symmetric_key)
        pub_key = FileFunctions.deserialize_public_key(path_public_key)
        encrypted_key = pub_key.encrypt(
            sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ),
        )
        FileFunctions.write_bytes(path_encrypted, encrypted_key)

    def decrypted(secret: str, encrypted: str, decrypted: str) -> bytes:
        """
        Decrypts an encrypted symmetric key using the provided private key 
        and saves the decrypted key to a specified file

        Args:
            secret (str): The file path to the private key used for decryption
            encrypted (str): The file path to the encrypted symmetric key
            decrypted (str): The file path where the decrypted symmetric key will be saved

        Returns:
            bytes: The decrypted symmetric key
        """
        symmetric_encrypted = FileFunctions.deserialize_symmetric_key(
            encrypted)
        secret_key = FileFunctions.deserialize_private_key(secret)
        decrypted_key = secret_key.decrypt(
            symmetric_encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        FileFunctions.serialize_symmetric_key(decrypted_key, decrypted)
        return decrypted_key
