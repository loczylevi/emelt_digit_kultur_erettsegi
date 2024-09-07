"""
1. Feladat
Írj eljárást, amely egy tetszőleges szöveget, ill. alakzatot ír ki a képernyőre!
"""

def mimoza():
    print("Dum spiro, spero.")
    for szam in range(10):
        print("0"*szam)
        if szam == 8:
            for szam in range(7, 0, -1):
                print("0"*szam)

    print("UwU")
    print(">:O")

mimoza()

"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
"""

def eldontom_helyetedd_is(szam):
    if szam > 0:
        print(f"A szám: {szam} pozitiv!")
    elif szam < 0:
        print(f"A szám: {szam} negativ!")
    elif szam == 0:
        print("A szám nulla!")

    print("Elkezdödödt a süsü brühühü .｡･ﾟﾟ･(>_<)･ﾟﾟ･｡.")


eldontom_helyetedd_is(7)

"""
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
"""


def melyik_nagyobb(num1,num2):
    if num1 > num2:
        print(f'A {num1} nagyobb mint a {num2}')
    elif num2 > num1:
        print(f'A {num2} nagyobb mint a {num1}')
    elif num1 == num2:
        print("A két szám egyenlő!")



print("\n_____________________________________\n")
melyik_nagyobb(6,7)
melyik_nagyobb(8,7)
melyik_nagyobb(8,8)

"""
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza,
és a képernyőre kiírja, melyik a legrövidebb szó!
"""


lista: list = []

for _ in range(3):
    bekeres = input("Kérek egy szót:\t")
    lista.append(bekeres)


def legkisebb(szavak):
    legkisebb = szavak[0]
    for szo in szavak:
        if len(szo) < len(legkisebb):
            legkisebb = szo

    print(f'A szavak közül ez a legrövidebb szó: {legkisebb}')
    print(f'Okositott min függvény: {min(szavak, key=len)}')
    print(f'Lambdás verzinnyo: {min(szavak, key=lambda x : len(x))}')


legkisebb(lista)


print("""
5.1 Feladat
A "Próbáld ki!" gombra kattintva elérhető egy program, ami egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt. 
Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki.
A lenti példában az eljárás hivása: mezot_rajzol(0,4)
""")

print("""\n\n____________________________________________________________________\nO O O O O O
O O O O O O
O O O O O O\n""")



def rajzolo(x,y):
    sor = x
    oszlop = y
    meddig = 0
    while meddig < 3:
        for szam in range(6):
            if meddig == sor and oszlop == szam:
                print("+",end=" ")
            else:
                print("O",end=" ")
        print()
        meddig = meddig + 1



x = False
y = False

import random

while True:
    try:
        x_kordinata = int(input("Az alábbi program 6x3-as mezőt rajzol hanyadik sorban rajzoljunk x-et? (1-3) "))
        if 1 <= x_kordinata <= 3:
            x = True
        else:
            print("\nBiiip-biiiip hiba, rosz intervallum! 1 és 3 között kérek számot!\n")
        y_kordinata = int(input("Hanyadik oszlopban rajzoljunk x-et? (1-6) "))
        if 1 <= y_kordinata <= 6:
            y = True
        else:
            print("\nBiiip-biiiip hiba, rosz intervallum! 1 és 6 között kérek számot!\n")
        if x == True and y == True:
            break
    except:
        print("A függvény csak számokkal [integer] tud dolgozni!")
        veletlen_x = random.randint(1,3)
        veletlen_y = random.randint(1,6)
        print(f"Példa bevitel: Rajzoljunk x-et a {veletlen_x}. sor {veletlen_y}. oszlopában!")
        print("____________________________\n")
        rajzolo(veletlen_x-1 , veletlen_y-1)
        print("\n____________________________")
    finally:
        print()

rajzolo(x_kordinata - 1 , y_kordinata - 1)


print("""
5.2 Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó adhassa meg a koordinátákat, ahová a program 'O' helyett '+' jelet ír.
A koordináták bekérése és a mező kirajzolása addig ismétlődjön, amíg a felhasználó negatív számot nem ad meg koordinátaként!
""")




def rajzolo(x,y):
    sor = x
    oszlop = y
    meddig = 0
    while meddig < 3:
        for szam in range(6):
            if meddig == sor and oszlop == szam:
                print("+",end=" ")
            else:
                print("O",end=" ")
        print()
        meddig = meddig + 1





import random

while True:
    try:
        x_kordinata = int(input("Az alábbi program 6x3-as mezőt rajzol hanyadik sorban rajzoljunk x-et? (1-3) "))
        if 1 <= x_kordinata <= 3:
            x = True
        else:
            print("\nBiiip-biiiip hiba, rosz intervallum! 1 és 3 között kérek számot!\n")
        y_kordinata = int(input("Hanyadik oszlopban rajzoljunk x-et? (1-6) "))
        if 1 <= y_kordinata <= 6:
            y = True
        else:
            print("\nBiiip-biiiip hiba, rosz intervallum! 1 és 6 között kérek számot!\n")
        if x_kordinata < 0 or y_kordinata < 0:
            break
        print()
        rajzolo(x_kordinata - 1 , y_kordinata - 1)

    except:
        print("A függvény csak számokkal [integer] tud dolgozni!")
        veletlen_x = random.randint(1,3)
        veletlen_y = random.randint(1,6)
        print(f"Példa bevitel: Rajzoljunk x-et a {veletlen_x}. sor {veletlen_y}. oszlopában!")
        print("____________________________\n")
        rajzolo(veletlen_x-1 , veletlen_y-1)
        print("\n____________________________")
    finally:
        print()







