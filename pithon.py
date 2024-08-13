# E == E karakterű mezőre lép,előreugorhat még ugyanannyit, mint amennyivel ide jutott.

# V == V karakterű mezőre lép, a bábunak vissza kell térnie oda, ahonnan ide ugrott.



with open("dobasok.txt","r",encoding="UTF-8") as f:
    dobasok = [sor.strip().split() for sor in f] 

with open("osvenyek.txt","r",encoding="UTF-8") as f:
    osvenyek = [sor.strip().split() for sor in f] 

db = 0

for sor in osvenyek:
    if len(sor) != 0:
        db += 1



db2 = 0
for sor in dobasok:
    for karakter in sor:
        db2 += 1





print(f'''2. feladat
A dobások száma: {db2}
Az ösvények száma: {db} ''')


