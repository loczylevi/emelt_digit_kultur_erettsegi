"""
1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!

(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)
"""
lista = []
with open("Timeline_of_ programming_languages.txt", "r", encoding="UTF-8") as f:
    link = f.readline()
    szeletelo = f.readline()
    for sor in f:
        adatok = sor.strip().split(';')
        #year;programming language;first name; last name of chief developer
        szotar = {'year': int(adatok[0]), 'language': adatok[1], 'first': adatok[2], 'last':adatok[3]}
        lista.append(szotar)

for sor in lista:
    print(sor)
    
ket_dinyemzios_lista = []
with open("Timeline_of_ programming_languages.txt", "r", encoding="UTF-8") as f:
    link = f.readline()
    szeletelo = f.readline()
    for sor in f:
        adatok = sor.strip().split(';')
        #year;programming language;first name; last name of chief developer
        egyik_lista = [int(adatok[0]), adatok[1],adatok[2], adatok[3]]
        ket_dinyemzios_lista.append(egyik_lista)
        
for sor in ket_dinyemzios_lista:
    print(sor)

print(ket_dinyemzios_lista)

"""
2. Feladat
A mellékelt fájl Rainer Maria Rilke: A párduc című versét tartalmazza Szabó Lőrinc fordításában (forrás: Magyar Elektronikus Könyvtár). Az általad írt program olvassa be a fájl tartalmát a read() metódussal, és adja meg a válaszokat az alábbi kérdésekre:
- hány betűt tartalmaz a vers,
- hány magánhangzót tartalmaz a vers,
- hány szó fordul elő a versben?
"""

with open("Rilke_A_parduc.txt", "r",encoding="UTF-8") as f:
   vers = f.read()
    
print(vers)

magyar_maganhangzok = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']

magany = len([betu for betu in vers if betu.lower() in magyar_maganhangzok])


print(f"""- {len([karakter for karakter in vers if karakter.isalpha()])} betűt tartalmaz a vers, 
- {magany} magánhangzót tartalmaz a vers,
- {len(vers.split())} szó fordul elő a versben""")

# 	(づ ◕‿◕ )づ
