honap = int(input("Add meg milyen hónap van (1-12): "))

tavasz = [3, 4, 5]
nyar = [6, 7, 8]
osz = [9, 10, 11]
tel = [12, 1, 2]

if honap in tavasz:
    print("Tavasz van!")
elif honap in nyar:
    print("Nyár van!")
elif honap in osz:
    print("Ősz van!")
elif honap in tel:
    print("Tél van!")
else:
    print("Nincs ilyen hónap!")