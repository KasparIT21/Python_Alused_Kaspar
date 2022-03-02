#########################
#    Iseseisev töö 13   #
#    Kaspar Tõnisson    #
#      02.03.2022       #
#         IT-21         #
#########################


#Anname arvule tühja väärtuse
arv = ''

#Kontrollime kas kasutaja on midagi sisestanud, kui ei ole küsime uuesti arvu
while True:
    arv = input("Sisesta arv et teada saada kas see on paaris või paaritu: ")
    if arv:
        print()
        break

#Arvutame jäägi, mille abi saame teada kas arv on paaris või paaritu
jaak = int(arv)%2

#Vaatame mida kasutaja sisestas ja kui ta sisestas nulli siis ütleme talle, et ei tohi ja vaatame kas arv on paaris või paaritu
if int(arv)==0:
    print("NULLI EI TOHI SISESTADA!")
elif jaak==0:
    print("Teie valitud arv",arv, "on paaris.")
else:
    print("Teie valitud arv ",arv, "on paaritu.")
