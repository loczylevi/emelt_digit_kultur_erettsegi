import os 



if os.path.exists("autok_listaja.txt"):
    with open("autok_listaja.txt","r",encoding="UTF-8") as f:
        adat = [sor.strip() for sor in f]
        


lista = []
szotar = dict()

#TRU-234 Opel Astra 12 1 18600
for sor in adat:
    szeletelo = sor.split()
    szotar["rendszám"] = szeletelo[0]
    szotar["márka"] = szeletelo[1]
    szotar["tipus"] = szeletelo[2]
    szotar["életkor"] = int(szeletelo[3])
    if szeletelo[4] == "1":
        szotar["javitott-e?"] = True
    else:
        szotar["javitott-e?"] = False
    szotar["ár"] = int(szeletelo[5])

    lista.append(szotar)
    szotar = {}

#for sor in lista:
    #print(sor)



"""
1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!
(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)
"""

if os.path.exists("nyelvek.txt"):
    with open("nyelvek.txt", "r", encoding="utf-8") as f2:
        elso_sor_vagyis_a_link = f2.readline()
        masodik_sor = f2.readline()
        adat = [sor.strip() for sor in f2]

nyelvek = []
nyelv = {}
"""
https://en.wikipedia.org/wiki/Timeline_of_programming_languages
year;programming language;first name; last name of chief developer
1972;C;Dennis; Ritchie

"""
for sor in adat:
    szeletelo = sor.split(";")
    nyelv["year"] = int(szeletelo[0])
    nyelv["programming language"] = szeletelo[1]
    nyelv["first name"] = szeletelo[2]
    nyelv["last name"] = szeletelo[3]

    nyelvek.append(nyelv)
    nyelv = {}


print("\n____________________________________________________________________________________________________________________________________________\n")
for sor in nyelvek:
    print(sor)


if os.path.exists("nyelvek.txt"):
    with open("nyelvek.txt", "r", encoding="utf-8") as f2:
        elso_sor_vagyis_a_link = f2.readline()
        masodik_sor = f2.readline()
        adat = [sor.strip() for sor in f2]
        ket_dinyemzios = []
        for sor in adat:
            szeletelo = sor.split(";")
            ket_dinyemzios.append([int(szeletelo[0]),szeletelo[1],szeletelo[2],szeletelo[3]])
        

print("\n____________________________________________________________________________________________________________________________________________\n")

print(ket_dinyemzios)
