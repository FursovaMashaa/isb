import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa


class FileFunctions:
    """
    A utility class for handling file operations, including reading and writing 
    text, JSON, and binary data, as well as serializing and deserializing 
    asymmetric keys

    Methods:
        read_txt(file_path: str) -> str:
            Reads text from a specified text file
        read_json(file_name: str) -> dict[str, str]:
            Reads JSON data from a specified file
        write_txt(path: str, data: str) -> None:
            Writes the given text to a specified file
        write_bytes(path: str, data: bytes) -> None:
            Writes binary data to a specified file
        read_bytes(path: str) -> bytes:
            Reads binary data from a specified file
        serialize_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
            Serializes and saves a private RSA key to a specified file
        serialize_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
            Serializes and saves a public RSA key to a specified file
        deserialize_private_key(path: str) -> rsa.RSAPrivateKey:
            Loads and deserializes a private RSA key from a specified file
        deserialize_public_key(path: str) -> rsa.RSAPublicKey:
            Loads and deserializes a public RSA key from a specified file
        serialize_symmetric_key(key: bytes, path: str) -> None:
            Serializes and saves a symmetric key to a specified file
        deserialize_symmetric_key(path: str) -> bytes:
            Loads and deserializes a symmetric key from a specified file
    """
    def __init__(self):
        pass
    def read_txt(file_path: str) -> str:
        """
        Reads text from a text file

        Args:
            file_path(str): The path to the text file to be read

        Returns:
            str: The text content read from the file
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
        Read JSON from the specified file name

        Args:
            file_name (str): The name of the file to read

        Returns:
            dict[str, str]: A dictionary containing the JSON data from the file
        """
        with open(file_name, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def write_txt(path: str, data: str) -> None:
        """
        Write the given text to a specified file

        Args:
            data(str): The text to be written to the file
            path(str): Path to the file where data was saved

        Returns:
            None
        """
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(data)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    def write_bytes(path: str, data: str) -> None:
        """
        Writes binary data to a specified file

        Args:
            path (str): Path to the file where binary data will be saved
            data (bytes): The binary data to be written to the file

        Returns:
            None
        """
        with open(path, 'wb') as f:
            f.write(data)

    def read_bytes(path: str) -> bytes:
        """
        Reads binary data from a specified file

        Args:
            path (str): The path to the binary file to be read

        Returns:
            bytes: The binary content read from the file

        """
        with open(path, 'rb') as f:
            data = f.read()
            return data

    def serialize_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serializes and saves a private RSA key to a specified file

        Args:
            path (str): The path where the private key will be saved
            private_key (rsa.RSAPrivateKey): The private RSA key to serialize

        Returns:
            None
        """
        pem_private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(path, 'wb') as f:
            f.write(pem_private)

    def serialize_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
        """
        Serializes and saves a public RSA key to a specified file

        Args:
            path (str): The path where the public key will be saved
            public_key (rsa.RSAPublicKey): The public RSA key to serialize

        Returns:
            None
        """
        pem_public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(path, 'wb') as f:
            f.write(pem_public)

    def deserialize_private_key(path: str) -> rsa.RSAPrivateKey:
        """
        Loads and deserializes a private RSA key from a specified file

        Args:
            path (str): The path to the private key file

        Returns:
            rsa.RSAPrivateKey: The deserialized private RSA key
        """
        with open(path, 'rb') as f:
            pem_private = f.read()
        return load_pem_private_key(
            pem_private,
            password=None
        )

    def deserialize_public_key(path: str) -> rsa.RSAPrivateKey:
        """
        Loads and deserializes a public RSA key from a specified file

        Args:
            path (str): The path to the public key file

        Returns:
            rsa.RSAPublicKey: The deserialized public RSA key
        """
        with open(path, 'rb') as f:
            pem_public = f.read()
        return load_pem_public_key(pem_public)

    def serialize_symmetric_key(key: bytes, path: str) -> None:
        """
        Serializes and saves a symmetric key to a specified file

        Args:
            key (bytes): The symmetric key to serialize and save
            path (str): The path where the symmetric key will be saved

        Returns:
            None
        """
        with open(path, 'wb') as f:
            f.write(key)

    def deserialize_symmetric_key(path: str) -> bytes:
        """
        Loads and deserializes a symmetric key from a specified file

        Args:
            path (str): The path to the symmetric key file

        Returns:
            bytes: The deserialized symmetric key
        """
        with open(path, 'rb') as f:
            return f.read()
