import os 

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from files import FileFunctions

class Symmetric:
    def generate_symmetric_key(key_path)->bytes:
        sym_key = os.urandom(16)  
        with open(key_path, 'wb') as f:
            f.write(sym_key)

if __name__ == "__main__":
    generate_symmetric_key('C:\\Users\\furso\\Desktop\\isb\\lab_3\\key\\symmetric_key.txt')