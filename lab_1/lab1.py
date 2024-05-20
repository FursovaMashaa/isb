import json


def read_txt(file_name: str) -> str:
    """
    Reads text from a text file.

    Args:
        file_name (str): The path to the text file to be read.

    Returns:
        str: The text content read from the file.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            return text

    except FileNotFoundError:
        print("the file was not found")
    except Exception as e:
        print(f"error: {e}")


def read_json(file_name: str) -> dict[str, str]:
    """
    Read JSON from the specified file name.

    Parameters:
    file_name (str): The name of the file to read.

    Returns:
    dict[str, str]: A dictionary containing the JSON data from the file.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = json.load(file)
            return text
    except FileNotFoundError:
        print("the file was not found")
    except Exception as e:
        print(f"error: {e}")


def write_txt(file_name: str, text: str) -> None:
    """
    Write the given text to a specified file.

    Parameters:
    file_name (str): The name of the file to write text to.
    text (str): The text to be written to the file.

    Returns:
    None
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def caesar_cipher(text: str, key: int) -> str:
    """
    Apply Caesar cipher encryption/decryption to the given text using the specified key.

    Parameters:
    text (str): The text to be encrypted/decrypted.
    key (int): The integer key used for encryption/decryption.

    Returns:
    str: The result of applying Caesar cipher to the input text with the key.
    """
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)


def main():
    input_text = read_txt(
        'C:\\Users\\furso\\Desktop\\isb\\lab_1\\task1\\original_text.txt')
    json_data = read_json(
        'C:\\Users\\furso\\Desktop\\isb\\lab_1\\task1\\key.json')
    key = int(json_data["caesar_cipher_key"])
    encrypted_text = caesar_cipher(input_text, key)
    write_txt(
        'C:\\Users\\furso\\Desktop\\isb\\lab_1\\task1\\encrypted.txt', encrypted_text)
    print("Успешно")


if __name__ == "__main__":
    main()
