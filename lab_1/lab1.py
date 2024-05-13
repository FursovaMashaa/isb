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
    

def read_json(file_name: str) -> 'dict[str, str]':
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = json.load(file)
            return text
    except FileNotFoundError:
        print ("the file was not found")
    except Exception as e:
        print(f"error: {e}")
    

def write_txt(file_name: str, text: str) -> None:
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def main() -> None:
    file_name_txt = 'lab_1/task1/original_text.txt'
    read_txt(file_name_txt)

    file_name_json = 'lab_1/task1/key.json'
    read_txt(file_name_json)



if __name__ == "__main__":
    main()
