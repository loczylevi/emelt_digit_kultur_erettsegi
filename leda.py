# E == E karakterű mezőre lép,előreugorhat még ugyanannyit, mint amennyivel ide jutott.

# V == V karakterű mezőre lép, a bábunak vissza kell térnie oda, ahonnan ide ugrott.

import os


if os.path.exists("osvenyek.txt"):
    with open("osvenyek.txt","r", encoding="utf-8") as f:
        osvenyek = [sor.strip() for sor in f]


#print(osvenyek)


try:
    with open("dobasok.txt","r",encoding="utf-8") as falj:
        elso_sor = falj.readline()
        finomitas = elso_sor.strip().split()
        dobasok = list(map(int, finomitas))

except:
    print("Nem létezik a fálj töki, és tarsd meg az aprót te mocskos állat!")


finally:
    print("UWU - Há' eddig MÉG működik a kód!")


#print(dobasok)


db = 0
for sor in osvenyek:
    if sor != '':
        db = db +1 

print(f'''2. feladat
A dobások száma: {len(dobasok)}
Az ösvények száma: {db} ''')


#3. Határozza meg, hogy melyik ösvény áll a legtöbb mezőből, és jelenítse meg az ösvény sorszámát és a mezők számát! Ha több ilyen is van, elegendő egyet megjelenítenie. 


hanyadik = 0
legnagyob = osvenyek[0]

for sor in osvenyek:
    if len(sor) > len(legnagyob):
        legnagyob = sor
    hanyadik = hanyadik + 1



print(f'''3. feladat
Az egyik leghosszabb a(z) {hanyadik}. ösvény, hossza: {len(legnagyob)} ''')

print('3. feladat')
leghosszabb = max(osvenyek, key=len)
print(f'Az egyik leghosszabb a(z) {osvenyek.index(leghosszabb) + 1}. ösvény, '
        f'hossza: {len(leghosszabb)}')



print("4. feladat")

bekeres1= int(input("Adja meg egy ösvény sorszámát!\t"))


tarolo = "Hiba, rossz intervallum"
bekeres2 = int(input("Adja meg a játékosok számát!\t"))
if 2 <= bekeres2 <= 5:
    tarolo = bekeres2




print("5. feladat")

elemzes = osvenyek[bekeres1-1]

m = 0
v = 0
e = 0
for karakter in elemzes:
    if karakter.lower() == "m":
        m += 1
    if karakter.lower() == "v":
        v += 1
    if karakter.lower() == "e":
        e += 1

print(f'''M: {m} darab
V: {v} darab
E: {e} darab ''')




print("\n______________________________________________________________________\n")

print(f'''M: {osvenyek[bekeres1-1].count("M")} darab
V: {osvenyek[bekeres1-1].count("V")} darab
E: {osvenyek[bekeres1-1].count("E")} darab ''')

