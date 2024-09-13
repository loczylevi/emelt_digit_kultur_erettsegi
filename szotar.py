"""4. Feladat
Készíts egy listát amely 8 diák adatait tartalmazza. A lista elemei szótárak legyenek, egy-egy szótár egy-egy diák adatait tárolja. A szótárban lévő kulcsok és a hozzájuk tartozó értékek:
"név": a vezeteknevek és a keresztnevek nevű listából véletlenszerűen választott és párosított elemek
"életkor": véletlenszám [14;19] intervallumban
"évfolyam": véletlenszám [9;12] intervallumban
"osztály": A, B, C vagy D lehet
"cím": beágyazott szótár melynek kulcsai:
"település": telepulesek nevű listából véletlenszerűen választva
"utca": utcak nevű listából véletlenszerűen választva
"házszám": véletlenszám [1;50] intervallumban

vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]
  
A program pprint modul pprint() függvénye segítségével áttekinthető módon jelenítse meg a diákok adatait a képernyőn!

Tipp: listából véletlenszerűen választani a random modul choice() függvényével tudunk a legegyszerűbben."""

vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]

import random
import pprint
diakok = [{},{},{},{},{},{},{},{}]

for elem in diakok:
    vezet = random.choice(vezeteknevek)
    kereszteslovag = random.choice(keresztnevek)
    elem.update({"név": vezet + " " + kereszteslovag})
    elem["életkor"] = random.randint(14,19)
    elem.update({"évfolyam": random.randint(9,12)})
    elem["osztály"] = random.choice(["A", "B", "C" , "D" ])
    elem.update({"cím": {"település": random.choice(telepulesek), "utca" : random.choice(utcak), "házszám" : random.randint(1,50)}})
    
#print(diakok)

pprint.pprint(diakok, depth=3, indent=4, sort_dicts=False, width=5)

"""
szoveg = pprint.pprint(diakok["cim"], sort_dicts=False)
eltavitando = ['[',']','{','}',"'"]

for k in eltavitando:
    szovegecske = szoveg.replace(k, '')
    
print(szoveg)"""


h = 10j

print(type(h))


    
    
    
