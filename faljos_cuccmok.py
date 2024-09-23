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

"""
2. Feladat
A mellékelt fájl Rainer Maria Rilke: A párduc című versét tartalmazza Szabó Lőrinc fordításában (forrás: Magyar Elektronikus Könyvtár).
Az általad írt program olvassa be a fájl tartalmát a read() metódussal, és adja meg a válaszokat az alábbi kérdésekre:
- hány betűt tartalmaz a vers,
- hány magánhangzót tartalmaz a vers,
- hány szó fordul elő a versben?
"""

if os.path.exists("rozsdaszin_parducXD.txt"):
    with open("rozsdaszin_parducXD.txt", "r",encoding="UTF-8") as f:
        tarolo = f.read()

    
#print(f"\n\n{tarolo}\n\n")
#print(len(tarolo))

db = 0
for sor in tarolo:
    if sor.isalpha():
        db += 1

print(f"Ennyi betüt tartalmaz a vers: {db}")

magyar_maganhangzok = ['a', 'e', 'i', 'o', 'ö', 'u', 'ü', 'á', 'é', 'í', 'ó', 'ő', 'ú', 'ű']

magan_db = 0
for betu in tarolo:
    if betu in magyar_maganhangzok:
        magan_db += 1

print(f"Ennyi magánhangzót tartalmaz a vers: {magan_db}")

szavak = tarolo.strip().split(" ")


tarolo = ['A', 'PÁRDUC\n\nSzeme', 'a', 'rácsok', 'futásába', 'veszve\núgy', 'kimerűlt,', 'hogy', 'már', 'semmit', 'se', 'lát.\nUgy', 'érzi,', 'mintha', 'rács', 'ezernyi', 'lenne\ns', 'ezer', 'rács', 'mögött', 'nem', 'lenne', 'világ.\n\nPuha', 'lépte', 'acéllá', 'tömörűl\ns', 'a', 'legparányibb', 'körbe', 'fogva', 'jár:\naz', 'erő', 'tánca', 'ez', 'egy', 'pont', 'körűl,\nmelyben', 'egy', 'ájúlt,', 'nagy', 'akarat', 'áll.\n\nCsak', 'néha', 'fut', 'fel', 'a', 'pupilla', 'néma\nfüggönye.', 'Ekkor', 'egy', 'kép', 'beszökik,\nátvillan', 'a', 'feszült', 'tagokon', 'és', 'a\nszívbe', 'ér', '-', 'és', 'ott', 'megszünik.']
nem_betuk = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  # Számok
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 
    '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',  # Speciális karakterek és írásjelek
    ' ', '\t', '\n'  # Szóköz, tabulátor, új sor
]

for szo in tarolo:
    if szo.isalpha() == False:
        for xd in nem_betuk:
            szo = szo.replace(xd, "")


print(f'Ennyi szót tartalmaz a vers: {len(szavak)}')








