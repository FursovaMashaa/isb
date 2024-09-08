import json
import math

from const import PATH

from mpmath import erfc


def read_json(file_name: str) -> dict[str, str] | None:
    """
    Read JSON from the specified file name.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        dict[str, str] | None: A dictionary containing the JSON data from the file or None if there was an error.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            name = json.load(file)
            return name
    except FileNotFoundError:
        print("the file was not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None


def analyze_bit_sequence(bit_sequence):
    n = len(bit_sequence)
    total_sum = sum(1 if bit == '1' else -1 for bit in bit_sequence)
    S_obs = abs(total_sum) / n
    p_value = erfc(S_obs / math.sqrt(2))
    return p_value


def main() -> None:
    java_data = read_json(PATH)

    if java_data is not None:
        java_bits = java_data['java']
        analyze_bit_sequence(java_bits)
    else:
        print('No data found!')


if __name__ == "__main__":
    main()
