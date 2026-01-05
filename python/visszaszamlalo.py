szam = int(input("Hány másodperctől induljon a visszaszámlálás? "))

for i in range(szam, -1, -1):
    print(i)
print("KILÖVÉS!")

# A range 3 számot vár (start, stop, lépésszám)
# start: induló szám (szamlalo változó értéke)
# stop: -1, mert a range az utolsó számot már nem teszi bele. tehát 0-ig fog menni
# lépésszám: -1 (lefelé számol ennyi lépéssel)