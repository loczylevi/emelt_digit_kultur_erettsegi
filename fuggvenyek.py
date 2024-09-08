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
        

