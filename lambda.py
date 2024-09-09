"""
1. Feladat
Írj egy programot, amely a listában tárolt sztringeket a 2. betű alapján rendezi sorba lambda függvény segítségével.
"""

lista = ["alma","adika","aadika","mimoza","tumor","nyunyor","cecil","ccecil"]


print(sorted(lista))
print(sorted(lista, key=lambda betu : betu[1]))






"""
2. Feladat
Írj egy programot, amely a fenti listában tárolt azonosítókat írja ki a képernyőre a számok sorrendjének megfelelően!
"""
azonositok = ['id10', 'id100', 'id23', 'id2', 'id13', 'id1']    

print(azonositok)
#print(sorted(azonositok))
#print(azonositok[0][2:])

print(sorted(azonositok, key=lambda id : int(id[2:])))

"""
3. Feladat
Írj egy programot, amely a fenti listából kiszűri az 'l' betűt tartalmazó szavakat kétféleképpen:
filter() + lambda függvény és list comprehension segítségével is!
"""
szavak = ['alma', 'ló', 'padló', 'citrom', 'kávé', 'nyugalom']


[print(szo, end=", ") for szo in szavak if "l" in szo.lower()]
print()

print(list(filter(lambda betu : "l" in betu.lower(), szavak)))


