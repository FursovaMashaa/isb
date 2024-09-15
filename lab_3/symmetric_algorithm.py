import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes

from files import FileFunctions


class Symmetric:
    def generate_symmetric_key(self, key_path: str) -> bytes:
        sym_key = os.urandom(16)
        with open(key_path, 'wb') as f:
            f.write(sym_key)
        return sym_key

    def encrypt_text(self, original_text_path: str, encryption_path: str, key: bytes) -> bytes:
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

    def decrypt_text(self, encrypted_text_path: str, decrypted_text_path: str, key: bytes) -> None:
        encrypted_text = FileFunctions.read_bytes(encrypted_text_path)

        iv = encrypted_text[:16]
        key = FileFunctions.deserialize_symmetric_key(key)
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        encrypted_text = encrypted_text[16:]
        decryptor = cipher.decryptor()
        encrypted_text = decryptor.update(
            encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        unpadder_dc_text = unpadder.update(
            encrypted_text) + unpadder.finalize()

        FileFunctions.write_txt(decrypted_text_path,
                                unpadder_dc_text.decode('UTF-8'))

        return unpadder_dc_text.decode('UTF-8')
    
    def encrypt_key(self, sym_key: bytes, public_key_path: str) -> bytes:
        pub_key = FileFunctions.deserialize_public_key(public_key_path)
        encrypted_key = pub_key.encrypt(
            sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return encrypted_key

    def decrypt_key(self, encrypted_key: bytes, private_key_path: str) -> bytes:
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


if __name__ == "__main__":


    # Создание симметричного ключа
    symmetric = Symmetric()


    # Путь к ключу
    key_path = r'C:\\Users\\furso\\Desktop\\isb\\lab_3\\key\\symmetric_key.txt'

    # Шифрование
    original_text_path = r'C:\\Users\\furso\\Desktop\\isb\\lab_3\\texts\\original_text.txt'
    encryption_path = r'C:\\Users\\furso\\Desktop\\isb\\lab_3\\texts\\encrypted_text.txt'
    symmetric.encrypt_text(original_text_path, encryption_path, key_path)

    # Дешифрование
    decrypted_text_path = r'C:\\Users\\furso\\Desktop\\isb\\lab_3\\texts\\decrypted_text.txt'
    symmetric.decrypt_text(encryption_path, decrypted_text_path, key_path)
