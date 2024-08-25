"""
Készíts egy programot, amely a felhasználó által megadott szót csupa nagybetűs formában írja ki a képernyőre!

A megoldáshoz használd a sztringek upper() metódusát! A használatáról itt tájékozódhatsz.

"""



bekeres = input("kérek egy szót:\t")

[print(x.upper(), end="") for x in bekeres]    # ahhhhh yamate kudasai

print("\n")


"""1.2 Feladat
Készíts egy programot, amely listaelemek leképezésével megvalósítja a következő funkciót:
egy szavakat tartalmazó lista elemeiből generál egy másik listát, amelyben az eredeti szavak
csupa nagybetűs formában szerepelnek! A program írja ki az eredeti és a generált listát is a képernyőre!"""


paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke', "fű"]
print(f'Eredeti lista: {paletta}\nGenerált list: ')
uj_lista = [print(szin.upper(), end=", ") for szin in paletta]



"""1.3 Feladat
Az előbbi programot módosítsd úgy, hogy csak a 3 betűnél hosszabb szavak kerülnek átalakítva a másik listába!"""


print(f'Eredeti lista: {paletta}\nGenerált list amiben csak a 3 betünél hpsszabb szavak kaptak átalakitást: ')
uj_lista = [print(szin.upper(), end=", ") for szin in paletta if len(szin) > 3]



"""1.1 Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot,
 és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre
   az összegüket és a lista elemeit!"""

import random 

szamok = []

for szam in range(5):
    veletlen = random.randint(1,10)
    szamok.append(veletlen)

print()
#print(szamok)

osszeg = 0
for szam in szamok:
    osszeg += szam

print(f'A lista elemei: {szamok}\na számok összegei: {osszeg} ')


"""1.2 Feladat
Módosítsd úgy a fenti programot, hogy a program csak a páros számokat adja össze!"""

osszeg = 0
for szam in szamok:
    if szam % 2 == 0:
        osszeg += szam

print(f'A lista elemei: {szamok}\na páros számok összegei: {osszeg} ')


"""
2. Feladat
Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. 
A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! 
A program írja ki a megadott intervallumba eső számokat és az összegüket!"""

try:
    lista = []
    while True:
        bekeres2 = int(input("Kérek egy számot [-5;5] intervallumban! "))
        if -5 <= bekeres2 <= 5:
            lista.append(bekeres2)
        else:
            break

except ValueError:
    print("hiba")



osszeg2 = 0
for szam in lista:
    osszeg2 += szam



print(f'A [-5;5] intervallumban eső számok: {lista}\nÖsszegei: {osszeg2}')




fakt = int(input("kérek egy számot: "))

faktorialis = []
for szam in range(1,fakt+1):
    faktorialis.append(szam)



osszeg3 = 1
for szam in faktorialis:
    osszeg3 *= szam


karakterlanc = []


for c, szam in enumerate(faktorialis, start=1):
    if c != fakt:
        karakterlanc.append(str(szam) + '*')
    else:
        karakterlanc.append(str(szam))


faktorialis.sort(reverse=True)


ize_xd = ""

for xd in karakterlanc:
    ize_xd = ize_xd + xd







print(f'A bekert szam: {fakt} ez átalakitva faktoriálista: {fakt}! vagyis: {ize_xd}\nami ugye összeszorozva: {osszeg3}')

