import os 


def generate_symmetric_key():
     return os.urandom(16)

def serialize_key(self, filename):
        with open(filename, 'wb') as file:
            file.write(self.key)

def deserialize_key(self, filename):
        with open(filename, 'rb') as file:
            self.key = file.read()