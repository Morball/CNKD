from Crypto import Random
from Crypto.Cipher import AES
import os
class AEScrypt():
    def __init__(self, key):
        self.key=key


    def pad(self, s):
        return s+b"\0"*(AES.block_size-len(s)%AES.block_size)

    def encrypt(self, message, key, keysize=256):
        message=self.pad(message)
        iv=Random.new().read(AES.block_size)
        cipher=AES.new(key, AES.MODE_CBC, iv)
        return iv+cipher.encrypt(message)

    def encrypt_file(self, filename):
        with open(filename, "rb") as file:
            text=file.read()
        enc=self.encrypt(text, self.key)
        with open(filename+".cnkd", "wb") as cfile:
            cfile.write(enc)
        os.remove(filename)


