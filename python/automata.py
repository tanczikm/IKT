ELFOGADOTT_CIMLETEK = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]

def Ar(termekkod):
    if termekkod == "1":
        return 500
    if termekkod == "2":
        return 450
    if termekkod == "3":
        return 300
    return 0

print("--- ITALAUTOMATA ---")
print("1: Cola (500), 2: Tea (450), 3: Víz (300)")

valasztas = input("Válasszon (kód): ")

if Ar(valasztas) == 0:
    print("Nincs ilyen termék!")

else:
    print("Fizetendő:", Ar(valasztas), "Ft")
    bedobott_penz = 0

    while bedobott_penz < Ar(valasztas):
        bedob = int(input("Dobja be a pénzt: "))
        elfogadva = False
        for cimlet in ELFOGADOTT_CIMLETEK:
            if bedob == cimlet:
                elfogadva = True
                
                bedobott_penz = bedobott_penz + bedob

                print("Még hiányzik:", Ar(valasztas) - bedobott_penz, "Ft")
                break
        
        if elfogadva != True:
            print("Ezt a címletet nem fogadom el!")
        
        
        
    print("Sikeres vásárlás!")
    visszajaro = (Ar(valasztas) - bedobott_penz) * -1
    print("Visszajáró:", visszajaro, "Ft")
    print("Köszönjük, hogy nálunk vásárolt!")