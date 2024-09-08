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


def the_same_consecutive_bits(bits):
    n = len(bits)
    a = sum(bits)/ n
    
    if abs(a - 0.5) >= 2 / math.sqrt(n):
        return 0
    
    V = 1
    for i in range(1, n):
        if bits[i] != bits[i - 1]:
            V += 1
    c=abs(V - 2 * n * a * (1 - a))
    d=(2 * math.sqrt(2 * n) * a * (1 - a))
    print(f"c: {c}, d: {d}")
    p_value = math.erfc(c/d)
    return p_value



def main() -> None:
    java_data = read_json(PATH)

    if java_data is not None:
        java_bits = java_data['java']
        analyze_bit_sequence(java_bits)
    else:
        print('No data found!')

    bit_sequence_str = "1001101011"
    bit_sequence = [int(bit) for bit in bit_sequence_str]
    p_value = the_same_consecutive_bits(bit_sequence)
    if p_value == 0:
        print("Тест неуспешен.")
    else:
        print(f"P-значение: {p_value}")   

if __name__ == "__main__":
    main()
