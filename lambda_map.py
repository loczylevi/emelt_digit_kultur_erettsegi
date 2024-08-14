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


legnagyobb = osvenyek[0]
for sor in osvenyek:
    if sor > legnagyobb:
        legnagyobb = sor


legnagyobb = legnagyobb[0]

k = 0
for karakter in legnagyobb:
    k += 1
#print(k)


statisztika = dict()

for sor in osvenyek:
    ev = str(sor)
    statisztika[ev] = statisztika.get(ev, 0) + 1

#evek = [ print(f' {ev}: {db} db.') for ev, db in statisztika.items() ]

g = "0"
for ev, db in statisztika.items():
    if len(ev) > len(g):
        g = ev

        #print(g)

#print(len(g))



print("4. feladat")

bekeres1= int(input("Adja meg egy ösvény sorszámát!\t"))


tarolo = "Hiba, rossz intervallum"
bekeres2 = int(input("Adja meg a játékosok számát!\t"))
if 2 <= bekeres2 <= 5:
    tarolo = bekeres2

print(tarolo)


print("5. feladat")

elemzes = osvenyek[bekeres1-1]

m = 0
v = 0
e = 0
for karakter in elemzes:
    for k in karakter:
        if k == m:
            m += 1
        if k == v:
            v += 1
        if k == e:
            e += 1

print(f'''M: {m} darab
V: {v} darab
E: {e} darab ''')

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
