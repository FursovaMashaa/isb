import json
import math
import mpmath

from typing import Dict

from const import PATH, PI


def read_json(file_name: str) -> Dict[str, str]:
    """
    Read JSON from the specified file name.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        dict[str, str] | None: A dictionary containing the JSON data from the file or None if there was an error.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("the file was not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None


def frequency_bitwise_test(bit_sequence: str) -> float:
    total_sum = sum(1 if bit == '1' else -1 for bit in bit_sequence)
    S_obs = abs(total_sum) / len(bit_sequence)
    p_value = math.erfc(S_obs / math.sqrt(2))
    return p_value


def the_same_consecutive_bits(bits: str) -> float:
    n = len(bits)
    a = bits.count("1") / n

    if abs(a - 0.5) >= 2 / math.sqrt(n):
        return 0

    V = 1
    for i in range(1, n):
        if bits[i] != bits[i - 1]:
            V += 1
    c = abs(V - 2 * n * a * (1 - a))
    d = (2 * math.sqrt(2 * n) * a * (1 - a))
    p_value = math.erfc(c/d)
    return p_value


def max_consecutive_ones(block: str) -> int:
    max_count = 0
    current_count = 0
    for bit in block:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


def analyze_sequence(sequence: str) -> float:
    block_size = 8
    blocks = [sequence[i:i + block_size]
              for i in range(0, len(sequence), block_size)]
    V = [0] * 4
    for block in blocks:
        max_length = max_consecutive_ones(block)

        if max_length == 0 or max_length == 1:
            V[0] += 1
        elif max_length == 2:
            V[1] += 1
        elif max_length == 3:
            V[2] += 1
        elif max_length > 3:
            V[3] += 1

    x_squared = sum((V[i] - 16 * PI[i]) ** 2 / (16 * PI[i]) for i in range(4))

    p_value = mpmath.gammainc(1.5, x_squared / 2)

    return p_value


def main() -> None:
    data = read_json(PATH)
    cpp_data = data.get("cpp")
    print(frequency_bitwise_test(cpp_data))
    print(the_same_consecutive_bits(cpp_data))
    print(analyze_sequence(cpp_data))
    print("--------------")
    java_data = data.get("java")
    print(frequency_bitwise_test(java_data))
    print(the_same_consecutive_bits(java_data))
    print(analyze_sequence(java_data))


if __name__ == "__main__":
    main()
