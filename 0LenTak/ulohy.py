#
# 
# 
# 1
vstup = input("Zadaj")
samohlasky = "aeiouáéíóúyýAEIOUÁÉÍÓÚYÝ"
for i in vstup:
    if i in samohlasky:
        print(i, end=" ")
#
# 
# 
# 2
veta = input("zadaj")
slova = veta.split()
najdlhsie = max(slova,key=len)

print(najdlhsie)

#
# 
# 
# 3
text = input("Zadaj: ")
slova = text.split()
cisla = 0

for s in slova:
    if s.isdigit():
        cisla += int(s)

print(cisla)



ahoj = input("Zadaj meno a rok narodenia ")
rok = 0
for i in ahoj.split():
    if i.isdigit():
        rok = i
    else:
        meno = i

print(f"Ahoj {meno} narodil si sa v roku {rok} ")


subor = open("C:\\Users\\matej\\Desktop\\2025PSA\\CV01","r")
riadok = subor.readline()
while riadok != "":
    print(riadok, end= " ")
    riadok = subor.readline()
subor.close()




#
# 
# 
# CV2 ULOHA1

prvyDen =int(input("kolko KM v 1. den: "))
pocetDni = 1
ciel = int(input("Kolko KM do ciela: "))

while prvyDen < ciel:
    a = prvyDen*0.1
    prvyDen += a
    pocetDni += 1

print(f"na {pocetDni} prešiel preterak {round(prvyDen,2)}")
#
#
# 
# CV2 ULOHA 2
import math
a = input("Zadaj cisla s medzerou ").split()
b = []
for i in a:
    if i.isdigit():
        b.append(int(i))
print(b)

#
# 
# 
# CV2 ULOHA 3

npocet = [None, 1, None, None]
n = (None, 1, None, None)
def vyhod_none(ntica):
    nova = []
    for i in ntica:
        if i != None:
            nova.append(i)

    return nova

print(vyhod_none(n))

#
# 
# 
# CV2 UHOLA 4 
cislo = 123456789111213
def ciferny_sucet(cifSuc):
    a=0
    for i in cifSuc:
        a += int(i)
    return a
print(ciferny_sucet(str(cislo)))

cifry = 1234567

def prerob(cislo):
    neg = cislo < 0
    cislo = str(abs(cislo))

    # zoskupovanie sprava po trojiciach
    skupiny = []
    while cislo:
        skupiny.append(cislo[-3:])
        cislo = cislo[:-3]

    vysledok = "_".join(reversed(skupiny))
    return "-" + vysledok if neg else vysledok

print(prerob(cifry))
#
# 
# 
# a
import random
from random import randint as ri
def pocitaj(i,j = 5):
    for abc in range(i):

        def pocet(j):
            opakovani = int(j)
            spocitana = 0
            hody =  []
            for i in range(opakovani):
                while(spocitana < 21):
                    cislo = ri(1,4)
                    spocitana += cislo
                    hody.append(cislo)
            for c in hody:
                print(str(c)+",", end= " ")
            if(spocitana == 21):
                print("hura")
            elif(spocitana < 21 or spocitana > 21):
                print("skoda")
        
pocitaj(2, j = 6)
#
# 
# 
#b

from random import randint
def sumuluj_hru(pocet):
    pole_hodov = []
    sucet_hodov = 0

    while sucet_hodov < pocet:
        pripocitane = randint(1,4)
        sucet_hodov += pripocitane
        pole_hodov.append(pripocitane)

    for i in pole_hodov:

        print(str(i),end=", ")
    if sucet_hodov < pocet or sucet_hodov > pocet:
        print("smola")
    else:
        print("hura")

sumuluj_hru(22)
