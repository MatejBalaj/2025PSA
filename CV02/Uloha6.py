import random

zadane = int(input("zadaj cislo: "))

print(f"{zadane}, ", end="")
while zadane != 1 :
    if zadane % 2 == 0 :
        zadane  = zadane // 2
    else :
        zadane = 3 * zadane + 1
    print(zadane, end="")