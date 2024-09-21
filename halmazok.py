a_halmaz = {0,2,4,6,8,10,12,14,16,18,20}
b_halmaz = {0,3,6,9,12,15,18,21}
a_halmaz.add(69)
a_halmaz.discard(101)
a_halmaz.discard(2)
b_halmaz.remove(0)
print(type(a_halmaz))

print("\n_____________________________halmazok:_________________________________\n")

print(f"'A' halmaz: {a_halmaz}\n")
print(f"'B' halmaz: {b_halmaz}")

print("______________________________________________________________________\n")

metszet = a_halmaz & b_halmaz   # & (and) jel a metszet

unio = a_halmaz | b_halmaz   # a (pipe) pedig az unio minden közös

kulombseg = a_halmaz - b_halmaz  # minusz jel (-) két halmza külömbsége

kulombseg2 = b_halmaz - a_halmaz

vagy_vagy = a_halmaz ^ b_halmaz   # nem értem ennek mi értelme van olyan mint az unio ¯\_(ツ)_/¯

print(f'valamelyik halmaznak a része: {unio}')

print(f'a két halmaznak a közös része: {metszet}')

print(f'Az "A" halmaz külömbsége: A-nak eleme de B-nek nem {kulombseg}')

print(f'Az "B" halmaz külömbsége: B-nek eleme de A-nak nem {kulombseg2}')

print(f'Vagy az "A" halmaznak vagy a "B" halmaznak része {vagy_vagy}')


print("""
1. Feladat
Adott két függvény (y=2x+3 és y=3x+1), mindkettő értelmezési tartománya az egész számok [0;10] intervallumon.
A program készítsen egy-egy halmazt a függvények értékkészleteivel, írja ki ezeket a képernyőre, majd jelenítse meg a halmazok metszetét,
unióját és különbségét!
""")

def fuggveny1(x):
    return 2 * x + 3             # értelmezési tartomány az amit az x felvehet


def fuggveny2(x):
    return 3 * x + 1              # # érték készlet az amit az y felvehet
halmzaz1 = set()

halmzaz2 = set()

for szam in range(0,11):
    szamocska = fuggveny1(szam)
    halmzaz1.add(szamocska)

for szam in range(0,11):
    szamocska = fuggveny2(szam)
    halmzaz2.add(szamocska)


print(f"'A' halmaz elemei: {halmzaz1}")           
print(f"'B' halmaz elemei: {halmzaz2}")
print(f"'A' és 'B' halmaz metszete: {halmzaz2 & halmzaz1}")
print(f"'A' és 'B' halmaz uniója: {halmzaz2 | halmzaz1}")
print(f"'A' és 'B' halmaz külömbsége: {halmzaz2 - halmzaz1}")
print(f"'B' és 'A' halmaz külömbsége: {halmzaz1 - halmzaz2}")


"""
2. Feladat
A program generáljon 5 egész számot [0;10] intervallumon, tárolja egy halmazban.
A felhasználónak meg kell próbálni kitalálni ezeket, olyan módon, hogy megad 5 számot, melyeket szintén halmazban tárol a gép.
A program tájékoztassa a felhasználót, a következőkről: hány darab számot talált el, és melyek ezek; hány számot nem talált el,
és melyek ezek; mely számok kerültek rögzítésre a generálás vagy a felhasználó miatt; mely számok nem szerepeltek egyik halmazban sem!
"""

import random 

halmaz = set()

tippek = set()



while len(halmaz) != 5:
    veletlen = random.randint(0,10)
    halmaz.add(veletlen)



print("Adjon meg 5db különböző számot!")
while len(tippek) != 5:
    try:
        bekeres = int(input("Kérem adjon meg számokat [0-10] intervallumban!\t"))
        tippek.add(bekeres)
    except:
        print("Valami nem jó (>_<)")



nem_talalt = 0
nem_jo = set()
db = 0
melyek = set()
for szam in halmaz:
    for tipp in tippek:
        if szam == tipp:
            db = db + 1
            melyek.add(szam)
        else:
            nem_talalt = nem_talalt + 1
            nem_jo.add(szam)

print(f"random számok: {halmaz}")
print(f"tippjeid: {tippek}")


print(halmaz & tippek)
print(len(halmaz & tippek))
print(halmaz ^ tippek)
print(halmaz - tippek)


"""
3. Feladat
A megadott halmazok alapján a program értékelje ki, és az eredményt jelenítse meg a képernyőn az alábbiakat vizsgálva:
- hány olyan étel van, amit mind a két gyerek szeret, és melyek ezek,
- melyek azok az ételek, amiket Peti szeret, de Kriszti nem,
- melyek azok az ételek, melyeket csak egyikük szeret!
"""

Peti_kedvencei = {'halászlé', 'bécsi szelet', 'bukta', 'rakott krumpli', 'almás rétes' }

Kriszti_kedvencei = {'borsóleves', 'bécsi szelet', 'túrós tészta', 'lecsó', 'almás rétes' }



print(f"Ételek száma melyeket mind a két gyerek szeret:\t{len(Peti_kedvencei & Kriszti_kedvencei)} és maguk az ételek:\t{Peti_kedvencei & Kriszti_kedvencei}")

print(f"Ételek melyeket Peti szeret, de Kriszti nem:\t{Peti_kedvencei - Kriszti_kedvencei}")

print(f"Ételek melyeket csak egyikük szeret:\t{Peti_kedvencei ^ Kriszti_kedvencei}")



