
"""
1. Feladat
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában.
Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót,
és írja ki a lista elemeit a képernyőre!
"""

import random

listacska = []

for szam in range(5):
    veletlen = random.randint(1,7)
    listacska.append(veletlen)


try:
    bekeres = int(input("Kérek egy számot/integer-t!\t"))
except:
    print("Error code: Zümmi zümm in line 19")
    bekeres = 19

finally:
    print("uwu")



van_e = False

index = 0
while index < len(listacska):
    if listacska[index] == bekeres:
        van_e = True
        break
    index = index + 1



if van_e:
    print(f"A fekhasználó által bekért szám: {bekeres} szerepel a listában: {listacska}")
else:
    print(f"A fekhasználó által bekért szám: {bekeres} NEM szerepel a listában: {listacska}")





"""2.1 Feladat
A program tároljon el egy szót egy változóban, majd írja ki egymás alá a szóban található betűket.
"""


szo = "Zümmi zümmmm"


for betu in szo:
    print(betu)


"""2.2 Feladat
A program tároljon el egy szót egy változóban. 
A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban!
Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!"""

szavacska = "cuius regio eius religio"

szamok = '<>#&@¤ß$Łłí][ĐđäÄ€Í÷×].0123456789"+!%/=()?-:;'

while True:
    bekeres = str(input("Kérek egy betüt!\t"))
    if len(bekeres) == 1 and bekeres not in szamok:
        break
    else:
        print("Egy betüt kértem, és véletlenül sem számot! A semmit nem tudom elemezni")


if bekeres.lower() in szavacska:
    print(f"A keresett betü: {bekeres} szerepel a szóban: {szavacska}")
else:
    print(f"A keresett betü: {bekeres} NEM szerepel a szóban: {szavacska}")


"""2.3 Feladat
Fejlesszük tovább a 2.2 programot úgy, hogy a felhasználónak többször is legyen lehetősége újabb tippet megadnia. 
A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!

Igyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói, 
például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).
"""


print("_____________________________________________________________UWU.exe__________________________________________________________________________---")
jo_betuk = ""

rosz_betuk = ""

szavacska = "cuius regio eius religio"

lista = []
for beti in szavacska:
    lista.append(beti)

print(lista)

szamok = '<>#&@¤ß$Łłí][ĐđäÄ€Í÷×].0123456789"+!%/=()?-:;'

while True:
    bekeres = str(input("Kérek egy betüt!\t"))
    print()
    if bekeres == "":
        break
    if len(bekeres) > 1 or bekeres in szamok:
        print("Egy betüt kértem, és véletlenül sem számot!")
        continue
    if bekeres.lower() in szavacska:
        print(f"A keresett betü: {bekeres} szerepel a szóban: {szavacska}")
        if bekeres.lower() in jo_betuk:
            pass
        else:
            jo_betuk = jo_betuk + bekeres.lower() + ", "
    else:
        print(f"A keresett betü: {bekeres} NEM szerepel a szóban: {szavacska}")
        if bekeres.lower() in rosz_betuk:
            pass
        else:
            rosz_betuk = rosz_betuk + bekeres.lower() + ", "
        
    print(f"Jó tippek/betük: {jo_betuk}\nRossz tippek/betük: {rosz_betuk}")



"""2.4 Feladat
Fejlesszük tovább a 2.3 programot úgy, hogy a program egy listában tároljon öt darab szót,
és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit."""



print("_____________________________________________________________UWU2.exe__________________________________________________________________________---")

jo_betuk = []

rosz_betuk = []

import random

szavak = ["carpe diem", "cuius regio eius religio", "divide et impera", "status quo", "in medias res", "deus ex machine", "Ave Caesar, morituri te salutant", "Cogito, ergo sum", "Dum spiro, spero", "Nomen est omen","Panem et circenses"]

szavacska = random.choice(szavak)

lista = []
for beti in szavacska:
    lista.append(beti)

print(lista)

szamok = '<>#&@¤ß$Łłí][ĐđäÄ€Í÷×].0123456789"+!%/=()?-:;'

while True:
    bekeres = str(input("Kérek egy betüt!\t"))
    print()
    if bekeres == "":
        break
    if len(bekeres) > 1 or bekeres in szamok:
        print("Egy betüt kértem, és véletlenül sem számot!")
        continue
    if bekeres.lower() in lista:
        print(f"A keresett betü: {bekeres} szerepel a szóban: {szavacska}")
        db = 0
        while True:
            if bekeres in lista:
                db = db + 1
                hol_toroljek = lista.index(bekeres)
                lista.pop(hol_toroljek)
            else:
                break
        jo_betuk.append(bekeres*db)


    else:
        print(f"A keresett betü: {bekeres} NEM szerepel a szóban: {szavacska}")
        if bekeres.lower() in rosz_betuk:
            pass
        else:
            rosz_betuk = rosz_betuk + bekeres.lower() + ", "
        
    print(f"Jó tippek/betük: {jo_betuk}\nRossz tippek/betük: {rosz_betuk}")
    print(lista)

