import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa


class FileFunctions:
    def read_txt(file_path: str) -> str:
        """
        Reads text from a text file.

        Args:
            file_path(str): The path to the text file to be read.

        Returns:
            str: The text content read from the file.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print("the file was not found")
        except Exception as e:
            print(f"error: {e}")

    def read_json(file_name: str) -> dict[str, str]:
        """
        Read JSON from the specified file name.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            dict[str, str]: A dictionary containing the JSON data from the file.
        """
        with open(file_name, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def write_txt(path: str, data: str) -> None:
        """
        Write the given text to a specified file.

        Args:
            data(str): The text to be written to the file.
            path(str): Path to the file where data was saved

        Returns:
            None
        """
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(data)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    def write_bytes(path: str, data: str) -> str:
        with open(path, 'wb') as f:
            f.write(data)

    def read_bytes(path: str) -> bytes:
        with open(path, 'rb') as f:
            data = f.read()
            return data

    def serialize_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
        pem_private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(path, 'wb') as f:
            f.write(pem_private)

    
    def serialize_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
        pem_public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(path, 'wb') as f:
            f.write(pem_public)

    def deserialize_private_key(path: str) -> rsa.RSAPrivateKey:
        with open(path, 'rb') as f:
            pem_private = f.read()
        return load_pem_private_key(
            pem_private,
            password=None
        )

    def deserialize_public_key(path: str) -> rsa.RSAPrivateKey:
        with open(path, 'rb') as f:
            pem_public = f.read()
        return load_pem_public_key(pem_public)

    def serialize_symmetric_key(key: bytes, path: str) -> None:
        with open(path, 'wb') as f:
            f.write(key)

    def deserialize_symmetric_key(path: str) -> bytes:
        with open(path, 'rb') as f:
            return f.read()
