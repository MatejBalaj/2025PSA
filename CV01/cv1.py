# 1      
pi = 3.14159264

polomer = int(input("Zadaj polomer: "))

print("Obovod je" + str(2*pi * polomer))

print("Obsah je: " + str(pi * polomer * polomer))

print("Obsah je {}".format(pi*polomer**2))

print("obvod je {} a obsah je {}".format(2*pi*polomer, pi*polomer**2))

# 2       
n = int(input("zadaj n-tú poziciu: "))
print("na {} policku je : {} cislo".format(n, 2**(n-1)))

#  3      
n = int(input("Zadaj: "))

for i in range(1,n+1):
    print("*"*i)
#4
import random

n = int(input("Zadaj: "))

ludi = 100

for i in range(1,n+1):
    nastupilo = random.randint(0,9)
    vystupilo = random.randint(0,9)
    ostalo = ludi + nastupilo - vystupilo
    print("Vo vlaku bolo {} ludi, {} nastupilo {}, vystupilo. zostalo {}".format(ludi, nastupilo, vystupilo, ostalo))
    ludi = ostalo