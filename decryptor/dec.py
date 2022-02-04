from Crypto.Cipher import AES
import os
class AESDecrypt():
    def __init__(self, key):
        self.key=key

    def decrypt(self, message, key):
        iv=message[:AES.block_size]
        cipher=AES.new(key, AES.MODE_CBC, iv)
        ptext=cipher.decrypt(message[AES.block_size:])
        return ptext.rstrip(b"\0")

    def decrypt_file(self, filename):
        with open(filename, "rb") as file:
            text=file.read()
        dec=self.decrypt(text, self.key)
        with open(filename[:-4], "wb") as decfile:
            decfile.write(dec)
        os.remove(filename)

