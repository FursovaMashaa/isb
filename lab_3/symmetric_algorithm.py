import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes

from files import FileFunctions


class Symmetric:
    """
    A class for generating and managing symmetric encryption keys

    Methods:
        generate_symmetric_key(key_path: str) -> bytes:
            Generates a random symmetric key 
        encrypt_text(original_text_path: str, encryption_path: str, key: bytes) -> bytes:
            Encrypts the plaintext from a specified file and writes the 
            encrypted content to another file
        decrypt_key(encrypted_key: bytes, private_key_path: str) -> bytes:
            Decrypts an encrypted symmetric key using a specified private key
    """
    def __init__(self):
        pass

    def generate_symmetric_key(key_path: str) -> bytes:
        """
        Generates a random symmetric key

        Args:
            key_path (str): The path where the generated symmetric key will 
            be saved

        Returns:
            bytes: The generated symmetric key
        """
        sym_key = os.urandom(16)
        with open(key_path, 'wb') as f:
            f.write(sym_key)
        return sym_key

    def encrypt_text(original_text_path: str, encryption_path: str, key: bytes) -> bytes:
        """
        Encrypts the plaintext from a specified file and writes the 
        encrypted content to another file

        Args:
            original_text_path (str): The path to the file containing 
            the plaintext to be encrypted
            encryption_path (str): The path where the encrypted content 
            will be written
            key (bytes): The symmetric key to be used for encryption

        Returns:
            bytes: The complete encrypted data including the IV
        """
        padder = padding.PKCS7(128).padder()
        text = FileFunctions.read_bytes(original_text_path).decode('utf-8')
        padded_text = padder.update(text.encode('utf-8')) + padder.finalize()
        iv = os.urandom(16)
        symmetric_key = FileFunctions.deserialize_symmetric_key(key)
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        text = iv + encryptor.update(padded_text) + encryptor.finalize()
        FileFunctions.write_bytes(encryption_path, text)
        return text

    def decrypt_key(encrypted_key: bytes, private_key_path: str) -> bytes:
        """
        Decrypts an encrypted symmetric key using a specified private key

        Parameters:
            encrypted_key (bytes): The encrypted symmetric key to be decrypted
            private_key_path (str): The file path to the private key used for decryption

        Returns:
            bytes: The decrypted symmetric key

        """
        secret_key = FileFunctions.deserialize_private_key(private_key_path)
        decrypted_key = secret_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return decrypted_key
