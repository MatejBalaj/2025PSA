import json
from enum import IntEnum
import socket
import time

SERVER = "127.0.0.1" #Adresa
PORT = 50000 #na ktorom je server

class Sprava:
#"pa" je parameter 
    def __init__(self, paOd, paKomu, paOperacia, paText):
        self.od = paOd
        self.komu = paKomu
        self.operacia = paOperacia
        self.text = paText

    @staticmethod
    def json_decoder(paObj):
        return Sprava(paObj["od"],paObj["komu"]
                      ,paObj["operacia"],paObj["text"])

class Operacia(IntEnum):
    LOGIN = 1
    EXIT = 2
    USERS = 3

def Napoveda():
    print("***Napoveda***")
    print("   \q Pre ukoncenie programu")
    print("   \l List pouzivatelov")
    print("   \h Zohraz napovedu")
    print("   Spravy posielajte v tvrare prijemca:sprava")
 

print("Vita vas program Chat 3.0")
od = input("Zadajte svoje meno: ")
Napoveda()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

sprava = Sprava(od,"", Operacia.LOGIN.value, "")
jsonStr = json.dumps(sprava.__dict__)
sock.send(jsonStr.encode())

bezim = True
while(bezim):
    prikaz = input("Zadajte spravu:")
    if(prikaz[0] == "\\"):
        if prikaz[1] == "q":
            sprava = Sprava(od,"", Operacia.EXIT.value, "")
            jsonStr = json.dumps(sprava.__dict__)
            sock.send(jsonStr.encode())
            bezim = False
            continue
            
        if prikaz[1] == "l":
            sprava = Sprava(od,"", Operacia.USERS.value, "")
            jsonStr = json.dumps(sprava.__dict__)
            sock.send(jsonStr.encode())

            message = sock.recv(1000)
            jsonStr = message.decode()
            sprava = json.loads(jsonStr, object_hook=Sprava.json_decoder)

            print("Zoznam pouzivatelov: " )
            print(sprava.text)
            continue
        if prikaz[1] == "h":
            Napoveda()
            continue

    vystupPrikazu = prikaz.split(":", 1)
    sprava = Sprava(od,vystupPrikazu[0], "",vystupPrikazu[1])
    jsonStr = json.dumps(sprava.__dict__)
    sock.send(jsonStr.encode())

        


sock.close()
print("Program sa ukoncil.")