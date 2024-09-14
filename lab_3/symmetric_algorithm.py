import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from files import FileFunctions


class Symmetric:
    def generate_symmetric_key(self, key_path: str) -> bytes:
        sym_key = os.urandom(16)
        with open(key_path, 'wb') as f:
            f.write(sym_key)
        return sym_key

    def encrypt_text(self, original_text_path: str, encryption_path: str, key: bytes) -> bytes:
        padder = padding.PKCS7(128).padder()

        # Чтение оригинального текста из файла
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


if __name__ == "__main__":
    original_text_file = "C:\\Users\\furso\\Desktop\\isb\\lab_3\\texts\\original_text.txt"
    encrypted_file = "C:\\Users\\furso\\Desktop\\isb\\lab_3\\texts\\encrypted_text.txt"
    symmetric_key_file = "C:\\Users\\furso\\Desktop\\isb\\lab_3\\key\\symmetric_key.txt"
    decrypted_file = "C:\\Users\\furso\\Desktop\\isb\\lab_3\\texts\\decrypted_text.txt"

    symmetric = Symmetric()
    sym_key = symmetric.generate_symmetric_key(symmetric_key_file)
    symmetric.encrypt_text(
        original_text_file, encrypted_file, symmetric_key_file)
    symmetric.decrypt_text(encrypted_file, decrypted_file, symmetric_key_file)

    print("Симметричный ключ сгенерирован, текст зашифрован и расшифрован.")
