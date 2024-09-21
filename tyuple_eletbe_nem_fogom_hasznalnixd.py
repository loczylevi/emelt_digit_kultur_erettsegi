"""
2. Feladat
Írj egy programot, amely a felhasználótól bekér egy RGB színkód három összetvőjét!
A program állapítsa meg és írja ki a képernyőre, hogy az adott szín tartalmaz-e zöld komponenst, illetve melyik komponensből van a legtöbb,
és melyikből a legkevesebb!
"""





oksa = [False, False, False]
while True: 
    try:   
        bekeres = int(input("Kérem az RGB kód 1. színét:\t"))
        bekeres2 = int(input("Kérem az RGB kód 2. színét:\t"))    #spagetti kód confirmed
        bekeres3 = int(input("Kérem az RGB kód 3. színét:\t"))
        rgb = (bekeres, bekeres2, bekeres3)
        for index,szam in enumerate(rgb, start=0):
            if 0 <= szam <= 255:
                oksa[index] = True

        if all(oksa):
            print("RGB szinek 0 és 255 között vannak!")
            break
        else:
            print("Az RGB szinek nem a 0 és 255 intervallumban esnek igy a bolygók eggyüttállásának köszönhetően is folytatodik a bekérés mindaddig mig helyes nem lesz!")
    except:
        print("valami nem jó gec (ﾒ﹏ﾒ)\nSzámot kértem nem mást!")
        bekeres = 0
        bekeres2 = 127
        bekeres3 = 255
        rgb = (bekeres, bekeres2, bekeres3)
        print(f"Alapértelmezett RGB szinek betáplálva: ({rgb[0]}, {rgb[1]}, {rgb[2]})")
        break



#print(rgb)

if rgb[1] > 0:
    print("Tartalmaz zöld árnyalatot is az RGB kód!")
else:
    print("NEM Tartalmaz zöld árnyalatot az RGB kód!")


szotar = [["red", rgb[0]],["green", rgb[1]],["blue", rgb[2]]]

legnagyobb = max(szotar, key=lambda x : x[1])
legkevesebb = min(szotar, key=lambda x : x[1])

print(f"Ebbö a 'komponensből' van a legtöbb: szine: '{legnagyobb[0]}' kódja: {legnagyobb[1]}")

print(f"Ebbö a 'komponensből' van a legkevesebb: szine: '{legkevesebb[0]}' kódja: {legkevesebb[1]}")










    
    
