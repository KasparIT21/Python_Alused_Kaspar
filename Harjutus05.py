####################
#    Ülesanne 5    #
#  Kaspar Tõnisson #
#    10.02.2022    #
#      IT-21       #
####################

'''
#Nimede lisamine loendisse
nimed = []
for i in range(5):
    nimi = input("Sisestage nimi (Ilma täpitähtedeta):")
    nimed.append(nimi)
nimed.sort()
for i in range (len(nimed)):
    print(nimed[i])
'''
'''
#Õpilased
nimi = ["mati", "kalle", "pille", "peeter", "juhan"]
for n in range(len(nimi)):
    print(n+1,nimi[n])
nr = int(input("Vali number:"))
del nimi[nr-1]
print("------------------")
lisa = input("Sisesta uus nimi:")
nimi.insert(nr-1, lisa)
print("------------------")
for n in range(len(nimi)):
    print(n+1,nimi[n])
'''
'''
#Duplikaadid
nimed = ["mati", "kalle", "pille", "peeter", "mati"]
nimed = list(set(nimed))
for n in range(len(nimed)):
    print(n+1,nimed[n])
'''
'''
#Vanused
import random
vanused = []
for i in range(5):
    vanused.append(random.randint(1,99))
print("Inimeste vanused:",vanused)    
print("Kõige vanem inimene:",max(vanused))
print("Kõige noorem inimene:",min(vanused))
print("Inimeste vanused kokku",sum(vanused))
print("Inimeste keskmine vanus",sum(vanused)/len(vanused))
'''

#Tärnid
import random
arvud = []
for i in range(6)
    arvud.append(random.randint(1,15))

