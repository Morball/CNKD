from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP 


def decrypt_aes_key(msg, rsakey):
    key=RSA.importKey(rsakey)
    cipher=PKCS1_OAEP.new(key)
    decrypted=cipher.decrypt(msg)
    return decrypted

