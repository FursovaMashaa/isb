import json
from cryptography.hazmat.primitives import serialization, hashes

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
                


    def write_txt(data: str, path: str) -> None:
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




