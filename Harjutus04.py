####################
#    Ülesanne 4    #
#  Kaspar Tõnisson #
#    03.02.2022    #
#      IT-21       #
####################

'''
#Ruut
a = int(input("Sisesta ruudu üks külg: "))
b = int(input("Sisesta ruudu teine külg: "))
if a == b:
    print("Tegemis on ruuduga")
else:
    print("Tegemist ei ole ruuduga")
'''

'''
#Matemaatika
earv = int(input("Sisesta esimene arv millega soovid tehet teha: "))
tehe = input("Sisesta mis tehet te soovite teha (+-*/)")
tarv = int(input("Sisesta teine arv millega soovid tehet teha: "))
if tehe == "+":
    vastsus = earv+tarv
elif tehe == "-":
    vastus = earv-tarv
elif tehe == "*":
    vastus = earv*tarv
else:
    vastus = earv/tarv
print("{earv}{tehe}{tarv}={vastus}")
'''

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