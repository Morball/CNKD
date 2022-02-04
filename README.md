# CNKD
Minimalistic Windows ransomware written in Python (Still a work in progress)<br/>



The following constants must be modified in order to deploy:<br/>
    DECRYPTOR_PATH<br/>
    DB_PASSWD<br/>
    SERV_HOST<br/>
    BACKGROUND_URL<br/>
    
To build the ransomware and decryptor simply use pyinstaller after installing the required dependencies<br/>


Import the included .sql file into the mysql database hosted on your server. <br/>




TO-DO:<br/>
-Add persistency<br/>
-Server-Client communication over TOR<br/>
-GUI for decryptor<br/>
