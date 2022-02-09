####################
#    Ülesanne 4    #
#  Kaspar Tõnisson #
#    03.02.2022    #
#      IT-21       #
####################


#Ruut
a = int(input("Sisesta ruudu üks külg: "))
b = int(input("Sisesta ruudu teine külg: "))
if a == b:
    print("Tegemis on ruuduga")
else:
    print("Tegemist ei ole ruuduga")

print("----------------------------")

#Matemaatika
earv = int(input("Sisesta esimene arv millega soovid tehet teha: "))
tehe = input("Sisesta mis tehet te soovite teha (+-*/)")
tarv = int(input("Sisesta teine arv millega soovid tehet teha: "))
if tehe == "+":
    vastus = earv+tarv
elif tehe == "-":
    vastus = earv-tarv
elif tehe == "*":
    vastus = earv*tarv
else:
    vastus = earv/tarv
print(f"{earv}{tehe}{tarv}={vastus}")

print("----------------------------")

#Juubel
from datetime import date
todays_date = date.today()
aasta = int(input("Sisesta oma sünniaasta: "))
paasta = todays_date.year
vanus = paasta-aasta
juubel = vanus/5
if juubel == int(juubel):
    print("Sul on juubeliaasta")
else:
    print("Sul ei ole juubeliaasta")

print("----------------------------")

#Myyk
hind = int(input("Sisestra valitud toote hind:"))
kymme = hind+(hind*0.1)
kakskymme = hind+(hind*0.2)
if hind <= 10:
    print(f"Toote lõpphind on: {kymme} €" )
else:
    print(f"Toote lõpphind on: {kakskymme} €")

print("----------------------------")

#Jalgpalli meeskond
sugu = input("Sisesta oma sugu M/N:")

if sugu == "M":
    vanus = int(input("Sisesta oma vanus:"))
    if (vanus>=16 and vanus<=18):
        print("Sa oled jalgpalli meeskonda vastu võetud :)")
    else:
        print("Vanus ei sobi")
else:
    print("Naised ei ole lubatud jalgpalli tiimi!!!")

print("----------------------------")

#Tärnid
for i in range(1,6):
    for j in range(1,6):
        print('* ', end='')
    print()
    
print("----------------------")
for k in range(0,5):
    for l in range(0, k+1):
        print('*', end='')
    print()

print("----------------------")
for m in range(5,0,-1):
    for n in range(0,m):
        print('*', end='')
    print()

print("----------------------------")

#Loto
import random
suvalinenr = random.randint(10000,99999)
print(f"Sinu suvaline number on: {suvalinenr}")

print("----------------------------")

#Paaris ja paaritu
import random
random = random.randint(1,100)
jaak = random%2

print(f"Teie suvaline arv on {random}")
if jaak==0:
    print("Paarisarv")
else:
    print("Paaritu arv")

print("----------------------------")

#Pisike korrutustabel
num = 5
for i in range(1,11):
    print(num, 'x', i, '=', num*i)

print("----------------------------")

#Viisikud
for i in range(1,21):
    for j in range(5,6):
        print(i*j)

print("----------------------------")

#Arvamismäng
import random
nr = random.randint(1,10)
loop = 1
kordade_arv = 0

while loop == 1:
    arva = int(input("Sisesta arv mis sa arvad, et on õige:"))
    if kordade_arv >= 2:
        kordade_arv += 1
        print("GAME OVER")
        loop == 3
        break
    
    elif arva == nr:
        kordade_arv += 1
        print("Palju õnne sa said õige arvu", kordade_arv, "korraga!!!")
        loop == 3
    elif arva > nr:
        kordade_arv += 1
        print("Loositud arv on väiksem.")
    elif arva < nr:
        kordade_arv += 1
        print("Loositud arv on suurem.")

print("----------------------------")

#Pank
raha = float(input("Sisesta raha summa mida soovid panka lisada:"))
konto = 0
konto = konto + raha
intress = 0.05
print("Aasta | Algsumma | Intrest | Aasta lõpuks")
for c in range(1,6):
    kasum = konto*intress
    print(f" {c}: {round(konto,2):10},{round(kasum,2):10},{round(konto+kasum,2):10}")
    konto = konto+kasum
 
print("----------------------------")
   
#Ruutude ja kuupide tabel  
print("   Arv | Ruut | Kuup")
for d in range(1,11):
    print(f" {d:6}|{d*d:6}|{d*d*d:6}")
