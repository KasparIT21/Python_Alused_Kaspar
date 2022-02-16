####################
#    Ülesanne 7    #
#  Kaspar Tõnisson #
#    16.02.2022    #
#      IT-21       #
####################


nimi = input("Sisesta nimi: ")
keel = input("Vali keel en/et/de: ")

def tervita(nimi, keel='de'):
    if keel == "et":
        print(f"Tere, {nimi}!")
    elif keel == "en":
        print(f"Hello, {nimi}!")
    else:
        print(f"Hallo, {nimi}!")

tervita(nimi, keel)


import math
def kuubi_ruumala(a):
    v=a**3
    return v

def kera(r):
    v = round(4/3*math.pi*r**3,2)
    return v

def koonus(r,h):
    v = round(1/3*math.pi*r**2*h,2)
    return v

def silinder(r,h):
    v = round(math.pi*r**2*h,2)
    return v

print("********** LEIAME RUUMALA **********")
print("Vali kujund")
print("1 Kuup")
print("2 Kera")
print("3 Koonus")
print("4 Silinder")
print()

kujund = int(input("Sisesta soovitud kujundi number: "))

if kujund == 1:
    a = int(input("Valisid kuubi. Sisesta kuubi külg: "))
    v = kuubi_ruumala(a)
    print("Kuubi ruumala on: ",v)
    
elif kujund == 2:
    r = int(input("Valisid kera. Sisesta kera raadius: "))
    v = kera(r)
    print("Kera ruumala on:", v)
    
elif kujund == 3:
    r = int(input("Valisid koonuse. Sisesta koonuse raadius: "))
    h = int(input("Valisid koonuse. Sisesta koonuse kõrgus: "))
    v = koonus(r,h)
    print("Koonuse ruumala on: ",v)
else:
    r = int(input("Valisid silindri. Sisesta silindri raadius: "))
    h = int(input("Valisid silindri. Sisesta silindri kõrgus: "))
    v = silinder(r,h)
    print("Silindri ruumala on: ",v)
