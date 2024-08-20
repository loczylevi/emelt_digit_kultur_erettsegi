paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']



szin = input('Adj meg egy színt!\t')




db = 0
van_e = False

for sz in paletta:
	if szin.lower() == sz.lower():
		db = db+ 1
		van_e = True
		

if van_e == True:
	print(f'A megadott szín szerepel a listában, ennyiszer: {db}')
else:
	print('A megadott szín nem szerepel a listában.')
	
paletta.append(szin)

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')



"""2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, 
a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot
[1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából,
majd írja ki a módosított listát a képernyőre!
"""

import random

lista = []

for szam in range(9):
	veletlen = random.randint(1,3)
	lista.append(veletlen)


try:
    while True:
        bekeres = int(input("\nAdj egy számot [1;3] intervallumon\t"))
        if 1 <= bekeres <= 3:
            break
        else:
            print("Rossz bemenet")
			
except ValueError:
	print("Igen????\nAZT MONDTAM HOGY SZÁMOT NEM KARAKTERLÁNCOT!\nSzámot kértem erre szöveget irsz be??? Te ilyen viccnyes úrfi/kisasszony vagy???")
	


index = 0
meddig = len(lista) -1
while True:
  if bekeres in lista:
    kereso = lista.index(bekeres)
    lista.pop(kereso)
  if index == meddig:
    break
  index = index + 1
	
		

print(lista)


"""3. Feladat
Írj egy programot, amely a felhasználótól betűket kér be mindaddig, amíg az nem ad meg betűt, csupán egy ENTER-t üt!

A program vizsgálja meg a megadott betűt, és tárolja el egy listában, ha az még nem szerepel benne (a felhasználó korábban még nem adta meg)! 
A program NE különböztesse meg a kis- és nagybetűket egymástól, de olyan formában tárolja el a betűket mindig, ahogy a felhasználó megadta.

Ha a megadott betű már szerepel a listában írja ki, a képernyőre, hogy "Ezt a betűt már rögzítettem."!

Minden egyes adatbekérés után írja ki a már rögzített betűket ábécé sorrendben (elöl a nagybetűk, utána a kisbetűk ábécé sorrendben)!
"""


lista = []

while True:
      bekeres = input("Kérek egy betűt! [kilépéshez nyomj enter-t!]\t")
      if bekeres == "":
            break
      

      if bekeres.lower() in [sor.lower() for sor in lista]:
          print("\nEzt a betűt már rögzítettem!\n")
      else:
          lista.append(bekeres)
    
    
      lista.sort()
      print(lista)
      
      
