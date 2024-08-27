

lista = [4,4,4,4,4,1,2,3,4,5,6,7,8,9,10]          

lista.sort()
print(lista)

bekeres = int(input("szam:\t"))

index = 0

while True:
    if bekeres in lista:
        hol_toroljek = lista.index(bekeres)
        lista.pop(hol_toroljek)
    else:
        break
    
lista.sort()
print(lista)

