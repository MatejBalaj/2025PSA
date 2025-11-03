import random

kociek = int(input("Zdaj pocet kociek: "))
hadzani = int(input("Zdaj pocet hadzani: "))

for h in range(0,hadzani+1):
    print(f"Hadzanie {h}:")
    sucet = 0
    for k in range(1,kociek+1):
        padlo = random.randint(1,6)
        print("Kocka cislo {} padlo cislo {}".format(k,padlo ))
        sucet += padlo
    print(f"sucet kociek je {sucet}")