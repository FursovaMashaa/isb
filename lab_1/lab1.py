import json



def read_txt(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
            
    except FileNotFoundError:
        print ("the file was not found")
    except Exception as e:
        print(f"error: {e}")
    print("Успешно")
    
    

def read_json(file_name: str) -> dict[str, str]:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = json.load(file)
            return text
    except FileNotFoundError:
        print ("the file was not found")
    except Exception as e:
        print(f"error: {e}")
    print("Успешно")
    

def write_txt(file_name: str, text: str) -> None:
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def caesar_cipher(text: str, key: int) -> str:
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)


def main():
    input_text = read_txt('C:\\Users\\furso\\Desktop\\isb\\lab_1\\task1\\original_text.txt')
    json_data = read_json('C:\\Users\\furso\\Desktop\\isb\\lab_1\\task1\\key.json')
    key = int(json_data["caesar_cipher_key"])
    encrypted_text = caesar_cipher(input_text, key)
    write_txt('C:\\Users\\furso\\Desktop\\isb\\lab_1\\task1\\encrypted.txt', encrypted_text)
    print("Успешно")
  




if __name__ == "__main__":
    main()
