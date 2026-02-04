def Aktivitas(lepesekSzama):
    if lepesekSzama > 10000:
        return True
    else:
        return False

sikeres_napok = 0

for nap in range(1, 8):
    lepes = int(input(f"{nap}. nap lépésszáma: "))
    if Aktivitas(lepes) == True:
        print("Teljesítve")
        sikeres_napok = sikeres_napok + 1
    if Aktivitas(lepes) == False:
        print("Nincs teljesítve")

print(f"A héten {sikeres_napok} napon sikerült a cél!")