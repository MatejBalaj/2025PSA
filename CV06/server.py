from threading import Thread
import json
from enum import IntEnum
import socket

SERVER = "0.0.0.0" #počuvam na všetkých adresách, treba ako str
PORT = 50000 #čislo portu
MLEN = 1000 #dlžka správy ktoru posielam v bitoch
QLEN = 10 #počet obsluhovanych naraz

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

def HandleClient(paClientSocket, paClientAddr, paPouzivatelia):

    while (True):
        message = paClientSocket.recv(MLEN)
        jsonStr = message.decode()
        sprava = json.loads(jsonStr, object_hook=Sprava.json_decoder)
        
        if sprava.operacia == Operacia.LOGIN:
            paPouzivatelia.append(sprava.od)
            print("Prihlasil sa {} z IPadresy: {} a PORTU:{}".format(sprava.od, paClientAddr[0],paClientAddr[1]))
            continue

        if sprava.operacia == Operacia.EXIT:
            paPouzivatelia.remove(sprava.od)
            print("Odhlasil sa" + sprava.od)
            paClientSocket.close()
            return

        if sprava.operacia == Operacia.USERS:
            odpoved = Sprava("", sprava.od, Operacia.USERS.value, 
                             paPouzivatelia)
            jsonStr = json.dumps(odpoved.__dict__)
            paClientSocket.send(jsonStr.encode())
            continue
        
        
        print("Sprava od: {}, komu:{}, \n\tSPRAVA:{}".format(sprava.od,sprava.komu, sprava.text))



if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))
    sock.listen(QLEN)

    print("Spustil sa server. Hura.")
    pouzivatelia = list()

    while True:
        (clientSock, clientAddr) = sock.accept()
        t = Thread(target=HandleClient, 
                   args=(clientSock, clientAddr, pouzivatelia))
        t.start()
    sock.close()