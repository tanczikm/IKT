def KezelesiKoltseg(osszeg):
    if osszeg < 10000:
        return 200
    else:
        return 500
    
osszesBevetel = 0

print("Csekkbefizetés - Egyszerűsített")

while True:
    csekkOsszeg = int(input("Adja meg a csekk összegét (0 a kilépés): "))
    if csekkOsszeg == 0:
        print("A posta teljes bevétele a költségekből:", osszesBevetel, "Ft")
        break
    else:
        print("A fizetendő költség:", KezelesiKoltseg(csekkOsszeg), "Ft")
        osszesBevetel = osszesBevetel + KezelesiKoltseg(csekkOsszeg)