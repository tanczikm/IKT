print("*** DUNGEONS & PYTHONS ***")
print("      ** FEGYVERTÁR **")

def TargyAr(kod):
    if kod == 1:
        return 50
    if kod == 2:
        return 150
    if kod == 3:
        return 100
    if kod == 4:
        return 200
    return 0

hatizsak = []

print("1 - Életerő ital (50 arany)")
print("2 - Vaskard (150 arany)")
print("3 - Pajzs (100 arany)")
print("4 - Varázstekercs (200 arany)")
print("******************************")

osszesen = int(input("Összesen hány tárgyat szeretnél vásárolni? "))

for i in range(osszesen):
    while True:
        targy_kod = int(input(f"{i+1}. tárgy kódja: "))
        ar = TargyAr(targy_kod)
        if ar == 0:
            print("Nincs ilyen tárgy a Fegyvertárban! Kérlek, válassz 1-4-ig!")
        else:
            print(f"A tárgy ára: {ar} arany")
            hatizsak.append(ar)
            break

fizetendo = 0
for szam in hatizsak:
    fizetendo = fizetendo + szam
print("------------------------")
print(f"Eredeti összeg: {fizetendo} arany")

kedvezmeny = 0
if fizetendo >= 400:
    print("Szintlépés! 10% bónusz az árból!")
    kedvezmeny = round(fizetendo * 0.1)
    print(f"Kedvezmény: {kedvezmeny} arany")

print(f"Fizetendő összesen: {fizetendo - kedvezmeny} arany")