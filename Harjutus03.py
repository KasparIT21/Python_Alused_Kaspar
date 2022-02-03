####################
#    Ülesanne 3    #
#  Kaspar Tõnisson #
#    03.02.2022    #
#      IT-21       #
####################
'''
#Korralik kasutajanimi
nimi = input("Sisesta nimi: ")
nimi = nimi.strip().capitalize()
print("Tere "+nimi+"!")
'''

'''
#Vandumine
tekst = input("Sisesta tekst: ")
print(tekst.replace("Kurat","*****"))
'''

'''
#Email
email = input("Sisestage email: ")
print("@" in email)
'''

'''
#Tundide ajad
algus = input("Sisesta tundide algus: ")
hh1,mm1 = algus.split(":")
lopp =input("Sisesta tundide lõpp: ")
hh2,mm2 = lopp.split(":")
#Teisendamine minutiteks
minutid = int(hh1)*60+int(mm1)
minutid2 = int(hh2)*60+int(mm2)
ajavahe = abs(minutid2-minutid)
hh = ajavahe // 60
mm = ajavahe % 60
print(f"Õpilase päeva pikkus on {hh}:{mm}")
'''

#Palindroom
palindroom = input("Sisesta suvaline tekst: ")
if(palindroom == palindroom[::-1]):
    print("Teie sisestatud tekst on palindroom")
else:
    print("Teie sisestatud tekst ei ole palindroom")




