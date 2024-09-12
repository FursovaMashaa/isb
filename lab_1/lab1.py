import json

from path import path_to_file


def read_txt(file_name: str) -> str:
    """
    Reads text from a text file

    Args:
        file_name (str): The path to the text file to be read

    Returns:
        str: The text content read from the file
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
    Read JSON from the specified file name

    Args:
        file_name (str): The name of the file to read

    Returns:
        dict[str, str]: A dictionary containing the JSON data from the file
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
    Write the given text to a specified file

    Args:
        file_name (str): The name of the file to write text to
        text (str): The text to be written to the file

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
    Apply Caesar cipher encryption/decryption to the given text using the specified key

    Args:
        text (str): The text to be encrypted/decrypted.
        key (int): The integer key used for encryption/decryption

    Returns:
        str: The result of applying Caesar cipher to the input text with the key
    """
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)


def write_json(name: str, data: dict) -> dict[str, str]:
    """
    The function for writing to a json file

    Args:
        name: path to the file to write
        data: data to write to a file
    Returns:
        dict[str, str]: A dictionary containing the JSON data from the file
    """
    try:
        with open(name, 'w', encoding='utf-8') as f:
            res = json.dump(data, f, ensure_ascii=False, indent=1)
        return res
    except Exception as e:
        print(f"An error occurred while writing the JSON file: {str(e)}.")


def frequency(path: str, text: str) -> None:
    """
    Calculates the frequency of characters appearing in the text and writes the result to a JSON file

    Args:
        path: The path to the file where the result will be written
        text: The text for which the character frequency needs to be calculated

    Returns:
        None
    """
    frequency = {}
    l = len(text)
    text_litters = []
    for i in text:
        if text_litters.count(i) == 0:
            text_litters.append(i)
    for i in text_litters:
        frequency[i] = text.count(i) / l
    write_json(path, frequency)


def decryption(path_sourse_text: str, path_key: str, path_encrypted_text: str, path_text_analysis: str) -> None:
    """ 
    Decrypts the text using the encryption key.

    Args:
        path_sourse_text: Path to the file where the decrypted text will be written.
        path_key: Path to the file with the encryption key (JSON format).
        path_encrypted_text: Path to the encrypted text file.
        path_text_analysis: The path to the file to record the analysis of the frequency of letters in the text.

    Returns:
        None.
    """
    text: str = read_txt(path_encrypted_text)
    key: dict = read_json(path_key)
    frequency(path_text_analysis, text)
    new_text: str = ""
    for letter in text:
        if letter in key:
            new_text += key[letter]
    write_txt(path_sourse_text, new_text)


def main():

    paths = read_json(path_to_file)

    input_text = read_txt(paths["original_text_task1"])
    json_data = read_json(paths["key_task1"])
    key = int(json_data["caesar_cipher_key"])
    
    encrypted_text = caesar_cipher(input_text, key)
    write_txt(paths["encrypted_text_task1"], encrypted_text)
    print("Шифрование успешно")


    path_source_text = paths["text_decrypted_task2"]
    path_key = paths["key_task2"]
    path_encrypted_text = paths["text_encrypted_task2"]
    
    decryption(path_source_text, path_key, path_encrypted_text, paths["frequency"])
    print("Дешифрование успешно")

if __name__ == "__main__":
    main()
