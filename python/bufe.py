def Ar(kod):
    if kod == 1:
        return 350
    if kod == 2:
        return 400
    if kod == 3:
        return 1000
    if kod == 4:
        return 700
    if kod == 5:
        return 400
    if kod == 6:
        return 300
    if kod == 7:
        return 350
    if kod == 8:
        return 250
    return 0

kosar = []

print("--- A BÜFÉ KÍNÁLATA ---")
print("1 - Sajtos-sonkás szendvics (350 Ft)")
print("2 - Körözöttes szendvics (400 Ft)")
print("3 - Hamburger (1000 Ft)")
print("4 - Hot-dog (700 Ft)")
print("5 - Kóla (400 Ft)")
print("6 - Ásványvíz (300 Ft)")
print("7 - Kakaó (350 Ft)")
print("8 - Gumicukor (250 Ft)")
print("--------------------------------")

darabSzam = int(input("Összesen hány terméket szeretnél vásárolni? "))

for darab in range(1, darabSzam+1):
    termekKodja = int(input(f"{darab}. termék kódja: "))
    ar = Ar(termekKodja)
    if ar > 0:
        print(f"A termék ára: {ar} Ft")
        kosar.append(ar)
    else:
        print("Hibás kód!")


print("--------------------------------")


fizetendo = sum(kosar)
if fizetendo >= 2500:
    fizetendo = round(fizetendo * 0.9)
    print("Nagy bevásárlás, 10% kedvezmény jár!")
print(f"Fizetendő összeg: {fizetendo} Ft")