import socket
import struct
import ipaddress

DNS_PORT = 53
DNS_ADDRESS = "1.1.1.1"
BIND_PORT = 50000

# Header
""" urobime si dns"""
transaction_id = socket.htons(0x1234)#host to network short, otoci littleEndina na BigEndian a naopak. ako short(ako cislo)
flags = socket.htons(0x0100)
questions = socket.htons(0x0001)
answer = 0x0000
autority = 0x0000
aditional = 0x0000

header = struct.pack("6h", transaction_id, flags, questions ,
                     answer ,autority, aditional)# ! pred  6 roby to iste ako htons

otazka = "www.uniza.sk"
labels = otazka.split(".")

body_of_query = b""

for label in labels:
    body_of_query += bytes([len(label)])

    for c in label:
        body_of_query += bytes([ord(c)])

body_of_query += bytes([0x00])

query_type = 0x0001
query_class = 0x0001

query_end = struct.pack("!2h",query_type, query_class)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#ideme udp

sock.bind(("0.0.0.0", BIND_PORT))

sock.sendto(header + body_of_query + query_end, (DNS_ADDRESS,DNS_PORT))#zlepene vsetko posledny tuple: kam chcem poslať na aky port

response , addr = sock.recvfrom(1024)

print (otazka + "ma adresu " + str(ipaddress.ip_address(response[-4:])))


sock.close()