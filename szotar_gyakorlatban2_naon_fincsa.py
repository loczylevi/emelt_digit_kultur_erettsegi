"""
1. Feladat
Írj egy programot, amelyben könyvek adatait (szerző, cím) tudja rögzíteni a felhasználó.
A könyvek adatainak tárolására használjon a program szótárakat, amelyek egy lista elemei legyenek!
Az adatbekérés addig folytatódjon, amíg a felhasználó a szerző megadásakor nem gépel be adatot, csupán ENTER-t üt!
A program ekkor listázza ki a már bevitt adatokat, és fejezze be a működését!
"""

konyvek = []

konyv = {}

while True:
    cim = input("Kérem a könyv cimét:\t")
    szerzo = input("Kérem a könyv szerzőjének cimét:\t")
    if szerzo == "" or cim == "":
        break
    else:
        #konyv["szerző"] = szerzo
        #konyv["cím"] = cim
        konyv.update({"szerző": szerzo})
        konyvek.append({"cim": cim})
        konyvek.append(konyv)
        konyv = {}

import pprint

pprint.pprint(konyvek,indent=4,width=3,depth=1,sort_dicts=False)

szoveg = pprint.pformat(konyvek, sort_dicts=False)

eltavolatindo = ['{','}','[',']', "'"]

for karakter in eltavolatindo:
    szoveg = szoveg.replace(karakter, '')

print((szoveg))




"""
2. Feladat
A mellékelt ZIP állományban találsz egy forrásfájlt (autok_lista.txt), amely tartalmazza egy autószerelő műhelyben lévő autók adatait.
Az adatok sorrendben a következők: rendszám, márka, típus, életkor, 0 = még nincs megjavítva 1 = megjavított, javítás költsége.

A muhely.py nevű fájlban lévő program pedig beolvassa ezeket az adatokat és eltárolja egy szótárakat tartalmazó listában.

Folytatsd a muhely.py programot az alábbiak szerint!
A program írja ki a képernyőre a legöregebb autó rendszámát, márkáját, típusát és korát! (Csak egy ilyen van!)
"""
print("\n__________________________________________________________________________________________________________________________________\n")



with open("autok_listaja.txt", "r", encoding="UTF-8") as f:
    lista = [sor for sor in f]

kocsik = []
kocsi = {}

#                   TRU-234 Opel Astra 12 1 18600

for elem in lista:
    szeletelo = elem.split()
    kocsi.update({"rendszám" : szeletelo[0]})
    kocsi["márka"] = szeletelo[1]
    kocsi["tipus"] = szeletelo[2]
    kocsi["életkor"] = int(szeletelo[3])
    if int(szeletelo[4]) == 1:
        kocsi["megjavitott-e"] = True
    else:
        kocsi["megjavitott-e"] = False
    kocsi["javitás_költsége"] = int(szeletelo[5])

    kocsik.append(kocsi)
    kocsi = {}


print(kocsik)

print("""\n1. A program írja ki a képernyőre a legöregebb autó rendszámát, márkáját, típusát és korát! (Csak egy ilyen van!)\n""")


legoregebb_auto = max(kocsik, key=lambda x : x["életkor"])

#print(legoregebb_auto)

print(f'''\n    ------------- 1. feladat -------------\t\t\ta, megoldás
A legöregebb autó: {legoregebb_auto["rendszám"]}, {legoregebb_auto["márka"]}, {legoregebb_auto["tipus"]}, {legoregebb_auto["életkor"]}\n''')


rendszam = ""
marka = ""
tipus = ""
eletkor = kocsik[0]["életkor"]

for elem in kocsik:
    if elem["életkor"] > eletkor:
        eletkor = elem["életkor"]
        rendszam = elem["rendszám"]
        marka = elem["márka"]
        tipus = elem["tipus"]

print(f'''\n    ------------- 1. feladat -------------\t\t\tb, megoldás
A legöregebb autó: {rendszam}, {marka}, {tipus}, {eletkor}\n''')

legnagyobb = max([sor["életkor"] for sor in kocsik])

legnagyobb_adatai = [[sor["rendszám"], sor["márka"], sor["tipus"], sor["életkor"]] for sor in kocsik if sor["életkor"] == legnagyobb]


print(f'''\n    ------------- 1. feladat -------------\t\t\tc, megoldás
A legöregebb autó: {legnagyobb_adatai[0][0]}, {legnagyobb_adatai[0][1]}, {legnagyobb_adatai[0][2]}, {legnagyobb_adatai[0][3]}\n''')



print("""2. A program írja ki a képernyőre a már megjavított autók rendszámát!""")


print(f"""    
    ------------- 2. feladat -------------\t\t\ta, megoldás
    A már megjavított autók rendszáma:
""")

megjavitott_autok = [print(sor["rendszám"]) for sor in kocsik if sor["megjavitott-e"]]

print("\n")

szures = list(filter(lambda elem: elem["megjavitott-e"] == True, kocsik))

print(f"""    
    ------------- 2. feladat -------------\t\t\tb, megoldás
    A már megjavított autók rendszáma:
""")
for szam in szures:
    print(szam["rendszám"])

print("\n")

print("""3. A program számolja ki, és írja ki a képernyőre az egy autóra eső átlagos szervízköltséget!""")


koltsegek = [sor["javitás_költsége"] for sor in kocsik]

atlag = sum(koltsegek) / len(koltsegek)

print(f'''
    
    ------------- 3. feladat -------------
    Az egy autóra jutó átlagos javítási költség: {atlag:.0f} Ft.
    
\n''')

print("4. A program kérjen be egy rendszámot, vizsgálja meg és tájékoztassa a felhasználót, hogy az adott rendszámú autó a műhelyben van-e.")



print('''
    ------------- 4. feladat -------------''')

bekeres = input("Adjon meg egy rendszámot (pl. ABC-123)!  ")


#A megadott rendszámú autó a műhelyben van.

kereso = [sor["megjavitott-e"] for sor in kocsik if bekeres == sor["rendszám"]]

kereso_2 = list(filter(lambda elem : bekeres == elem["rendszám"], kocsik))

      
if len(kereso_2) > 0:
    print("A megadott rendszámú autó a műhelyben van.")
else:
    print("A megadott rendszámú autó nincs a műhelyben.")























