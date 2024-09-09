"""
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat)
összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!
"""




def osszegzo(*szamok):
    ossz = 0
    for szam in szamok:
        ossz += szam
    return ossz


fuggveny_hivas = osszegzo(1,2,3,4,5,6,7,8,9,10,101)
print(f"A szamok összeadása az osszegzo fugveny használatával: {fuggveny_hivas}")


"""
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza,
ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False!
A program tartalmazza a függvény hívását is!
"""

def paros_e(*lista):
    van_e = False
    for szam in lista:
        if szam % 2 == 0:
            van_e = True 
            break
    return van_e
        

van_e_paros = paros_e(1,2,3,4,5,6,7,8,9,10,11,12,23,34,45,56,67,78,89,69)

if van_e_paros:
    print("Van páros szám a listában")
else:
    print("Nincs páros szám a listában")
        

"""
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt,
amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van,
és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!
"""

def harommal_oszthatok(*lista):
    db = 0
    for szam in lista:
        if szam % 3 == 0:
            db += 1
    return db


hany_db_3_mal_oszthato = harommal_oszthatok(0,1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,69)


print(f"A listában ennyi 3-mal osztható szám van: {hany_db_3_mal_oszthato}")



"""
3.2 Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában,
és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)
"""

def harommal_oszthatok(szamok):
    db = 0
    for szam in szamok:
        if szam % 3 == 0:
            db += 1
    return db

lista: list = []



while True:
    try:
        bekeres = input("Kérek egy számot!\t")
        if int(bekeres) < 0:
            break
        else:
            lista.append(int(bekeres))
    except:
        print("Kérem [integert] számot adjon meg!")



hany_db_3_mal_oszthato = harommal_oszthatok(lista)


print(f"A listában ennyi 3-mal osztható szám van: {hany_db_3_mal_oszthato}")



"""
4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is!
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet,
1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!
A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
"""


def negyzet(szam):
    return 4*szam

def teglalap(szam,oldalak):
    return 2*szam + 2*oldalak

def haromszog(szam, oldalak):
    return szam + oldalak[0] + oldalak[1]

def sokszog(szam, oldalak):
    return szam + sum(oldalak)



def kerulet(szam, *args):
    hany = len(args)
    if hany == 0:
        return negyzet(szam)
    if hany == 1:
        return teglalap(szam, args)
    if hany == 2:
        return haromszog(szam, args)
    if hany >= 3:
        return sokszog(szam, args)


print(kerulet(4, 2, 3,7,6,5,4,3))


"""
5. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír!
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza.
A program írja ki, hogy melyik volt a megadott legkisebb szám!
"""

lista: list = []

while True:
    try:
        bekeres = input("Kérek egy számot!\t")
        if int(bekeres) < 0:
            break
        else:
            lista.append(int(bekeres))
    except:
        print("Kérem [integert] számot adjon meg!")


def legkisebb(szamok):
    return min(szamok)


print(f"A listában a legkisebb szám: {legkisebb(lista)}")



"""
1. Feladat
Írj egy programot, amely generál egy véletlenszámot [1; 10] intervallumon, és a játékosnak ezt kell kitalálnia.
A próbálkozások száma nincs megkötve, de a program számolja a tippelési alkalmakat.

A program tartalmazzon
egy kitalalando nevű változót, ebben kerüljön tárolásra a generált véltelenszám,
egy tipp nevű változót, ez tárolja az éppen aktuális tippet,
egy main nevű függvényt, amely tartalmazza a főprogramot,
egy eltalalta nevű függvényt, amelynek
- 2 paramétere van, a játékos éppen aktuális tippje és az kitalálandó szám,
- visszatérési értéke True vagy False, attól függően, hogy a paraméterként átvett értékek megegyeznek-e egymással vagy nem,
egy tipp_bekero nevű függvényt, amelynek
- nincs paramétere,
- bekéri a felhasználó tippjét, és azzal tér vissza.

    Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!
    Tippelj! 4
    Nem találtad el. Ez volt a 1. próbálkozásod.
    Tippelj! 2
    Nem találtad el. Ez volt a 2. próbálkozásod.
    Tippelj! 3
    Gratulálok eltaláltad 3 próbálkozásból!
    Játék vége!
"""

def tipp_bekero():
    while True:
        try:
            bekeres = int(input("Kérek egy tippet:\t"))
            if type(bekeres) == int:
                break
        except:
            print("Számot kérek köcce! :3")
    return bekeres

def eltalalta(tipp, kitalalando):
    if tipp == kitalalando:
        return True
    else:
        return False

import random

kitalalando = random.randint(1,10)
print(kitalalando)

tippek_szama = 0
def main(tippek_szama):
    print("Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!")
    while True:
        tipp = tipp_bekero()

        eltalalta_e = eltalalta(tipp, kitalalando)
        if eltalalta_e:
            return "Gratulálok eltaláltad 3 próbálkozásból!\nJáték vége!"
        else:
            tippek_szama += 1
            print(f"Nem találtad el. Ez volt a {tippek_szama}. próbálkozásod.")




print(main(tippek_szama))       



