elso = int(input("Add meg az 1. jegyet! "))
masodik = int(input("Add meg az 2. jegyet! "))
harmadik = int(input("Add meg az 3. jegyet! "))

atlag = round(((elso + masodik + harmadik) / 3), 2)

print("Átlag:", atlag)
if atlag >= 2.0:
    print("Megfelelt.")

else:
    print("Nem felelt meg.")