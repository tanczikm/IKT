import allat

# 2. az iratrendező ahová az állatok kerülnek
allatfajok = []

# a "_" azt csinálja hogy nem jön létre külön változó pl "i" néven

# 3. adatbekérés, példányosítás és lefűzzük a mappába
for _ in range(3):
    fajnev = input("Add meg egy állatfaj nevét! ")
    tomeg = int(input("Hány kilogramm a tömege egy példánynak? "))
    allatfaj = allat.Állatfaj(fajnev,tomeg)
    allatfajok.append(allatfaj)


for allat in allatfajok:
    print(f"A(z) {allat.fajnev} tömege {allat.tomeg} kg.")

# 4. maxmimum elv - a legnehezebb álat megkeresése
legnehezebb = allatfajok[0]

for allatfaj in allatfajok:
    if allatfaj.tomeg > legnehezebb.tomeg:
        legnehezebb = allatfaj


# 5. minimum elv - legkönnyebb súlyú állat megkeresése
legkonnyebb = allatfajok[0]
for allatfaj in allatfajok:
    if allatfaj.tomeg > legkonnyebb.tomeg:
        legkonnyebb = allatfaj


# 6. fájlba kiíratás
fajl = open("legnehezebb.txt", "w")
fajl.write(f"A(z) {legnehezebb.fajnev} a legnehezebb.")
fajl.close()