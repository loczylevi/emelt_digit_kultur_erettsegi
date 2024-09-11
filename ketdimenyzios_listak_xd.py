"""
1. Feladat
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál,
és ezeket a listákat egy 'tarolo' nevű listába helyezi. A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
"""

import random

tarolo = [[],[],[],[]]


index = 0
for szam in range(4):
    for szam in range(3):
        veletlen = random.randint(0,25)
        tarolo[index].insert(0,veletlen)
    index += 1

print("_________________________________________________________")
print(tarolo)
print(tarolo[0][0])

   # érték módosítása
tarolo[0][1] = 22

print(tarolo)
  
      # érték beszúrása
tarolo[0].insert(0, 0)
print(tarolo)
      # sor beszúrása
tarolo.insert(1, [0, 0, 0])
print(tarolo)
      # érték törlése, a pop() metódus visszatérési értéke a törölt érték
del tarolo[0][0]
print(tarolo)
tarolo[0].pop(0)
print(tarolo)
  
      # sor törlése
del tarolo[1]
print(tarolo)
tarolo.pop(1)
print(tarolo)

print("uwU")


"""
2.1 Feladat
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista! Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '. A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki. A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!

    O O O
    O O O
    O O O 

"""

tarolo = [['O ','O ','O '],['O ','O ','O '],['O ','O ','O ']]

def megjelenito(tarolo):
        for o_betu in tarolo:
            print(''.join(o_betu))

megjelenito(tarolo)


"""
2.2 Feladat
Egészítsd ki úgy a programot, hogy a felhasználó megadhasson egy koordinátát (a bal felső rácspont koordinátája (0;0),
a jobb alsó pedig (2;2)), és ekkor a program rajzolja ki úgy a 3x3-as rácsot, hogy a megadott koordinátán 'O ' helyett, '+ ' legyen!
"""


def megjelenito(tarolo, x,y):
        tarolo[x][y] = '+ '
        for o_betu in tarolo:
            print(''.join(o_betu))


print("___________________________________________2.2_________________________________________________________________________________")
print("Melyik pozicióban legyen 'O ' helyett, '+ '?")

while True:
      try:
            x = int(input("Kérek egy vizszintes kordinátát! (1-3)\t"))
            y = int(input("Kérek egy függőleges kordinátát! (1-3)\t"))
            if 1 <= x <= 3 and 1 <= y <= 3:
                  break
            else:
                  print("Rossz intervallum ¯\_(ツ)_/¯")
      except:
            print("\nSzámokkal tudok dolgozni töki ¯\_(ツ)_/¯\n")

            


megjelenito(tarolo, x-1, y-1)


"""
2.3 Feladat
Alakítsd át úgy a programot, hogy a koordinátapárok bekérése addig folytatódjon, míg a felhasználó intervallumon kívüli értéket nem ad meg!
A program minden bekérés után rajzolja ki a rácsot úgy, hogy megjeleníti a már korábban megadott koordináták esetében is a '+' jelet!
"""


print("___________________________________________2.3_________________________________________________________________________________")
print("Melyik pozicióban legyen 'O ' helyett, '+ '?")

while True:

      try:
            x = int(input("Kérek egy vizszintes kordinátát! (1-3)\t"))
            y = int(input("Kérek egy függőleges kordinátát! (1-3)\t"))
            if 1 <= x <= 3 and 1 <= y <= 3:
                  megjelenito(tarolo, x-1, y-1)
            else:
                  break
      except:
            print("\nSzámokkal tudok dolgozni töki ¯\_(ツ)_/¯\n")

"""
3. Feladat
Készíts egy programot, amely egy kétdimenziós listában tárol ötször három darab véletlenszámot [-5;5] intervallumon.
A program írja ki a kétdimenziós lista elemeit, majd fésülje át a lista tartalmát és törölje belőle a negatív számokat.
Végül ismét kerüljön kiírásra lista tartalma!

  Véletlenszámok:
  [[2, -3, 0], [5, 5, 1], [-4, -2, 3], [-5, 0, -1], [1, 2, 1]]
  
  Nemnegatív véletlenszámok:
  [[2, 0], [5, 5, 1], [3], [0], [1, 2, 1]]
    
"""

veletlenszamok = [[],[],[],[],[]]
import random
index = 0
for szam in range(5):
      for szam in range(3):
            veletlen = random.randint(-5,5)
            veletlenszamok[index].insert(0, veletlen)
      index = index + 1


tarolo = ["alma","gg","dasdasd"]
tarolo.insert(1,"mimozaaaaaaaaaaaaa")
print(tarolo)
tarolo.pop(2)
print(tarolo)

print(f"\nVéletlenszámok lista: {veletlenszamok}")

"""
elem= 0
index = 0
while elem < len(veletlenszamok):
      while index < 2:
            if veletlenszamok[elem][index] < 0:
                  veletlenszamok[elem].pop(index)
            index = index + 1

      elem = elem + 1
"""

for szam, index in enumerate(veletlenszamok, start=0):
      for sz, index2 in enumerate(index, start=0):
            if index2 < 0:
                  #veletlenszamok[szam].pop(sz)
                  del veletlenszamok[szam][sz]

print(f"\nNemnegatív véletlenszámok: {veletlenszamok}")

