"""
1.1 Feladat
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt!
A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!
"""
lista = []
#ize_bize = ["asdasd","dasdasd","mimozaaaXD"]
#ize_bize2 = [1,2,3,4,56,7,8,9,10j]

#ize_bize3 = list(map(str, ize_bize2))

while True:
    try:
        bekeres = input("Kérek egy számot!\t")
        if type(int(bekeres)) is int:
            lista.append(int(bekeres))
        print(lista)

    except ValueError:
        if bekeres == "":
            print(lista)
            break
        elif type(float(bekeres)) is float:
            lista.append(float(bekeres))
            print(lista)

finomitott_lista = list(map(str,lista))
print('A lista elemei:', ', '.join(finomitott_lista))

#print(', '.join(ize_bize))
#print(', '.join(ize_bize3))

if len(lista) > 0:

    legkisebb = lista[0]
    legnagyobb = lista[0]

    for szam in lista:
        if szam > legnagyobb:
            legnagyobb = szam
        if szam < legkisebb:
            legkisebb = szam

    print(f'''
A lista lenagyobb eleme: {legnagyobb}
A lista legnagyobb eleme: {max(lista)}
a lista legkisebb eleme: {legkisebb}
A lista legkisebb eleme: {min(lista)}''')


"""
1.2 Feladat
Alakítsd át úgy az előbbi programot, hogy az 'X' vagy 'x' megadása eredményezze az adatbekérés végét!
"""

print("""1.2 Feladat
Alakítsd át úgy az előbbi programot, hogy az 'X' vagy 'x' megadása eredményezze az adatbekérés végét!""")
            
lista = []
#ize_bize = ["asdasd","dasdasd","mimozaaaXD"]
#ize_bize2 = [1,2,3,4,56,7,8,9,10j]

#ize_bize3 = list(map(str, ize_bize2))

while True:
    try:
        bekeres = input("Kérek egy számot!\t")
        if type(int(bekeres)) is int:
            lista.append(int(bekeres))
        print(lista)

    except ValueError:
        if bekeres == "X" or bekeres == "x":
            print(lista)
            break
        elif type(float(bekeres)) is float:
            lista.append(float(bekeres))
            print(lista)

finomitott_lista = list(map(str,lista))
print('A lista elemei:', ', '.join(finomitott_lista))

#print(', '.join(ize_bize))
#print(', '.join(ize_bize3))


legkisebb = lista[0]
legnagyobb = lista[0]

for szam in lista:
    if szam > legnagyobb:
        legnagyobb = szam
    if szam < legkisebb:
        legkisebb = szam

print(f'''
A lista lenagyobb eleme: {legnagyobb}
A lista legnagyobb eleme: {max(lista)}
a lista legkisebb eleme: {legkisebb}
A lista legkisebb eleme: {min(lista)}''')



print("__________________________________________________________________alternativ verzió_______________________________________________________")

lista = []
amig = True

while amig:
    bekeres = input("Kérek be egy számot:\t")
    if bekeres == "X" or bekeres == "x":
        amig = False
    else:
        lista.append(int(bekeres))


listab = list(map(str, lista))

print("lista:", ',  '.join(listab))

legkisebb = lista[0]
legnagyobb = lista[0]

for szam in lista:
    if szam > legnagyobb:
        legnagyobb = szam
    if szam < legkisebb:
        legkisebb = szam

print(f'''
A lista lenagyobb eleme: {legnagyobb}
A lista legnagyobb eleme: {max(lista)}
a lista legkisebb eleme: {legkisebb}
A lista legkisebb eleme: {min(lista)}''')


print("""
1.3 Feladat
Alakítsd át úgy az előbbi programot, hogy a legkisebb és legnagyobb páros számot határozza meg! UWU uWu
""")

lista = []
amig = True

while amig:
    bekeres = input("Kérek be egy számot:\t")
    if bekeres == "X" or bekeres == "x":
        amig = False
    else:
        lista.append(int(bekeres))


listab = list(map(str, lista))

print("lista:", ',  '.join(listab))

legkisebb = lista[0]
legnagyobb = lista[0]

for szam in lista:
    if szam > legnagyobb and szam % 2 == 0:
        legnagyobb = szam
    if szam < legkisebb and szam % 2 == 0:
        legkisebb = szam


def paros_szamok(lista):
    return [szam for szam in lista if szam % 2 == 0]




print(f'''
A lista lenagyobb eleme: {legnagyobb}
A lista legnagyobb eleme lambda: {max(lista, key=lambda x : x if x % 2 == 0 else 0)}
               sima  max {max(lista)}
     sima fuggvenyes max {max(lista)}
a lista legkisebb eleme: {legkisebb}
A lista legkisebb eleme: {min(lista)}''')
#print(max(tegla, key=lambda teglacska: teglacska[1]), "\n\n")1

