# Ülesanne03
# Kaspar Tõnisson
# 02.02.2022


#Kütusekulu
kytus_liiter = int(input("Sisesta tangitud kütuse liitrid:"))
labitud_km = int(input("Siseta läbitud kilomeetrid:"))
kytuse_kulu = round((labitud_km/kytus_liiter)*100)
print("Sinu keskmine kütusekulu on",kytuse_kulu,"km/l")

print("_________________________________")

#Arvusüsteemid
kumnend = int(input("Sisesta arv:"))
kahend = bin(kumnend)
kuusteist = hex(kumnend)
print("Teie arv 2nd süsteemis:",kahend)
print("Teie arv 16nd süsteemis:",kuusteist)

print("_________________________________")

#Ajateisendus
aeg = int(input("Sisesta aeg minutites:"))
tund = 60
tunnid = aeg//tund
minutid = aeg % tund
print("Kell on",tunnid,":",minutid)

print("_________________________________")

#Hüpotenuus
a,b = 16,9
hupotenuus = pow(a,2) + pow(b,2)
import math
c = math.sqrt(hupotenuus)
print("Kolmnurga hüpotenuus on",round(c,2))

print("_________________________________")

#Rulluisutajad
kiirus = 29.9
aeg = 0.4
vahemaa = kiirus*aeg
print("Rulluisutaja jõuan 24 minutiga",round(vahemaa,2),"km kaugusele" )

print("_________________________________")

#Pitsa
sobrad = 3
pitsa = 12.9
jootraha = 0.1
kogusumma = ((pitsa*jootraha)+pitsa)/sobrad
print("Iga inimene peab maksma",kogusumma,"€")

print("_________________________________")

#3 toote hind
hind = 36.75
soodus = 0.4
kogus = 3
summa = (hind-(hind*soodus))*kogus
print(kogus, "toote hind on",summa,"€")

print("_________________________________")

# Kolmnurga ümbermõõt
a,b,c = 15,16,18
p = a+b+c
print("Kolmnurga ümbermõõt:",p)
