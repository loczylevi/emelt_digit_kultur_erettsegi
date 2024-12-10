"""1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát, és másold át azt egy fájlba úgy, hogy abba már csak a nyelv és az évszám kerüljön!

(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)
"""

with open("Timeline_of_ programming_languages.txt", 'r', encoding='utf-8') as forrasfajl, \
    open('Timeline_of_ programming_languages_masolata.txt', 'w', encoding='utf-8') as celfajl:
            elso = forrasfajl.readline()
            masodik = forrasfajl.readline()
            lista = [sor.strip().split(";") for sor in forrasfajl]
            for sor in lista:
                print(f"{sor[0]};{sor[1]}",file=celfajl)
      
            
            
            
  