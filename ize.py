# E == E karakterű mezőre lép,előreugorhat még ugyanannyit, mint amennyivel ide jutott.

# V == V karakterű mezőre lép, a bábunak vissza kell térnie oda, ahonnan ide ugrott.
"""
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
"""
lista = [8,12, -10, 101, -54 ,72]

print(lista, "\n\n")
print(sorted(lista), "\n\n")
print(sorted(lista, reverse=True, key=abs), "\n\n")
print(sorted(lista, key=abs), "\n\n")


tegla = [[9,2], [6,4], [5,1]]

def xd(tegla):
    return tegla[1]

print(max(tegla, key=xd), "\n\n")

print(max(tegla, key=lambda teglacska: teglacska[1]), "\n\n")

print(min(tegla, key=lambda teg: teg[1] * teg[0]), "\n\n")


szamok = ['1','2','3','4','5','6']

print(sorted(list(map(int, szamok)),reverse=True))


szamok2 = sorted(list(map(int, szamok)),reverse=True)

print(type(szamok2))
print(szamok2)


keresztnevek = ["gizi","béla", "nyunyorka", "lingo", "mimozaaaaaa"]


nevek = list(map(lambda nevek: nevek[0] == "l", keresztnevek))

print(nevek)


szamok = [1, 2, 3, 4, 5]

print(list(filter(lambda szam: szam % 2 != 0, szamok)))
# list comprehension-nel
print([szam for szam in szamok if szam % 2 != 0])  



