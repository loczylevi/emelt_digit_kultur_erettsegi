
#feladat forrása:  UwU           (づ ◕‿◕ )づ                (づ ◕‿◕ )づ                    (づ ◕‿◕ )づ                      (づ ◕‿◕ )づ

#       https://sulipy.hu/adattipusok/szotar_gyakorlatban?tab=video


"""
Kiss Péter 17 10.A 1
Horváth Emma 16 10.C 1  
Szabó Rolnad 17 10.A 1
Nagy Botond 18 10.B 1
Vámosi Kitti 17 10.B 0
Veszprémi András 16 10.A 0
Kiss Júlia 16 10.A 1
Kovács Donát 16 10.B 1
Füzi Levenete 17 10.C 1
"""


with open("diak_adatok.txt", "r", encoding="UTF-8") as f:
    adat = [sor.strip() for sor in f]


#print(adat)


diak_szotar = {}
diakok = []

for elem in adat:
    szeletelo = elem.split(" ")
    #print(szeletelo)
    diak_szotar.update({"családi, vezeték név": szeletelo[0]})
    diak_szotar.update({"kereszt név, sima": szeletelo[1]})
    diak_szotar.update({"életkor": int(szeletelo[2])})
    diak_szotar.update({"osztály": szeletelo[3]})
    if szeletelo[4] == "1":
        diak_szotar["kollégiumos-e"] = True
    elif szeletelo[4] == '0':
        diak_szotar["kollégiumos-e"] = False
        
    diakok.append(diak_szotar)
    diak_szotar = {}

#print(diakok)

import pprint

#pprint.pprint(diakok, indent=4, depth=3, sort_dicts=False,width=3)



"""
Kiss Péter 17 10.A 1
Horváth Emma 16 10.C 1
Szabó Rolnad 17 10.A 1
Nagy Botond 18 10.B 1
Vámosi Kitti 17 10.B 0
Veszprémi András 16 10.A 0
Kiss Júlia 16 10.A 1
Kovács Donát 16 10.B 1
Füzi Levenete 17 10.C 1
"""
"""

with open("diak_adatok.txt", encoding="utf-8") as f:
    addatok = [sor.strip() for sor in f]


diakkok = []

diak = {}

for elem in addatok:
    #print(elem)
    szeletelo = elem.split(" ")
    diak.update({"nev1": szeletelo[0]})
    diak.update({"nev2": szeletelo[1]})
    diak.update({"életkor": szeletelo[2]})
    diak.update({"osztaly": szeletelo[3]})
    diak.update({"kollegista-_E": szeletelo[4]})

    diakkok.append(diak)
    diak = {}

import pprint


pprint.pprint(diakkok, indent=4, depth=3, sort_dicts=False,width=3)
"""

"""10a osztályosok nevei"""

print("________________________________________________________________________________________________________________")



print("\nEgész lista:\n")

for elem in diakok:
    print(elem)


print("________________________________________________________________________________________________________________\n")
print("10a osztályosok nevei:\n")
for elem in diakok:
    if elem["osztály"] == "10.A":
        print(elem["családi, vezeték név"], elem["kereszt név, sima"])
    #if "10.A" in elem["osztály"]:
        #print(elem["családi, vezeték név"], elem["kereszt név, sima"])


print("________________________________________________________________________________________________________________\n")
print("konpenziv lista vagy micsoda\n")

a10_nevek = [print(sor["családi, vezeték név"], sor["kereszt név, sima"]) for sor in diakok if sor["osztály"] == "10.A"]

print("________________________________________________________________________________________________________________\n")
print("10B osztályosok adtai:\n")

tiz_be = [print(sor["családi, vezeték név"], sor["kereszt név, sima"], sor["életkor"], sor["osztály"], sor["kollégiumos-e"]) for sor in diakok if sor["osztály"] == "10.B"]

b10_minden = [print(sor) for sor in diakok if sor["osztály"] == "10.B"]


eletkorok = [sor["életkor"] for sor in diakok]

print("________________________________________________________________________________________________________________\n")
print(f"A diákok életkorainak átlaga: {sum(eletkorok)/len(eletkorok):.3f}")



legnagyobb = max(diakok, key=lambda x:x["életkor"])  # (づ ◕‿◕ )づ egy soros megolás flex XDDDDDDDDDDDDDDDDDDD

print("________________________________________________________________________________________________________________\n")
print("A legidősebb diák: \n")

print("'A.' megoldás: A legidősebb diák neve:", legnagyobb["családi, vezeték név"] + " " + legnagyobb["kereszt név, sima"], "\tkora:", legnagyobb["életkor"])

# több soros megoldás

nagyobb = diakok[0]["életkor"]

legidosebb_diak_neve = ""

for elem in diakok:
    if elem["életkor"] > nagyobb:
        nagyobb = elem["életkor"]
        legidosebb_diak_neve = elem["családi, vezeték név"] + elem["kereszt név, sima"]


print(f"'B.' megoldás: A legidősebb diák neve: {legidosebb_diak_neve}\tKora: {nagyobb}")




legeslegjobb = max([sor["életkor"] for sor in diakok])

legeslegjobb_neve = [[sor["családi, vezeték név"], sor["kereszt név, sima"], sor["életkor"]] for sor in diakok if sor["életkor"] == legeslegjobb]

print(f"'C.' megoldás: A legidősebb diák neve: {legeslegjobb_neve[0][0]} {legeslegjobb_neve[0][1]}\tKora: {legeslegjobb}")





