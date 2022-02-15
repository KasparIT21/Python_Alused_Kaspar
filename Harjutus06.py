####################
#    Ülesanne 6    #
#  Kaspar Tõnisson #
#    15.02.2022    #
#      IT-21       #
####################
from collections import Counter
count = 0
count1 = 0
erakonnad = []
with open('s6pru_l6ustaraamatus.txt', 'r') as s6brad:
    for rida in s6brad:
        a = rida.split(" ")
        print(f'{a[0]:11}{a[1]:11}{a[2]:4}{a[3]:5}', end="")
        if a[2] not in erakonnad:
            erakonnad.append(a[2])
            
        
print()
print()



with open("s6pru_l6ustaraamatus.txt") as f:
    contents = f.read()
    count = contents.count("RE")

print("Reformierakondi:", count)

with open("s6pru_l6ustaraamatus.txt") as f1:
    content1 = f1.read()
    count1 = contents.count("KE")

print("Keskerakondi:", count1)

if a[2] not in erakonnad:
    erakonnad.append(a[2])
    
erakond = set(erakonnad)
kokku = len(erakond)
print("Erakondi kokku:", kokku)

