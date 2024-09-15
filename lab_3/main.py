import argparse

from symmetric_algorithm import Symmetric
from asymmetric_algorithm import Asymmetric
from files import FileFunctions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str,
                        help="Mode of operation: generate_keys, encrypt, or decrypt")

    args = parser.parse_args()
    settings = FileFunctions.read_json("settings.json")
    symmetric = Symmetric()
    asymmetric = Asymmetric()

    match args.mode:
        case "generate_keys":
            sum_key = symmetric.generate_symmetric_key(
                settings["symmetric_key"])
            FileFunctions.serialize_symmetric_key(
                sum_key, settings["symmetric_key"])
            public_key, secret_key = asymmetric.generate_keys()
            FileFunctions.serialize_public_key(
                settings["public_key"], public_key)
            FileFunctions.serialize_secret_key(
                settings["secret_key"], secret_key)

        case "encrypt":
            symmetric.encrypt_text(
                settings["initial_file"],
                settings["encrypted_file"],
                settings["symmetric_key"])
            asymmetric.encrypt_text(
                settings["public_key"],
                settings["symmetric_key"],
                settings["encrypted_symmetric_key"])

        case "decrypt":
            asymmetric.decrypt_text(
                settings["secret_key"],
                settings["encrypted_symmetric_key"],
                settings["decrypted_symmetric_key"])
            symmetric.decrypt_text(
                settings["symmetric_key"],
                settings["encrypted_file"],
                settings["decrypted_file"])

        case _:
            print("Try again")

if __name__ == "__name__":
    main()
