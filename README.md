# CNKD
Minimalistic Windows ransomware written in Python (Still a work in progress)



The following constants must be modified in order to deploy:
    DECRYPTOR_PATH
    DB_PASSWD
    SERV_HOST
    BACKGROUND_URL
    
To build the ransomware and decryptor simply use pyinstaller after installing the required dependencies


Import the included .sql file into the mysql database hosted on your server. 




TO-DO:
-Add persistency
-Server-Client communication over TOR
-GUI for decryptor
