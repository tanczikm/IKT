# 1. KONSTANSOK (állandó értékek) meghatározása
ALAP_JEGYAR = 2000             # Az alap jegyár forintban
GYEREK_KORHATAR = 14           # Ez alatt a kor alatt gyereknek számít 
GYEREK_KEDVEZMENY = 0.5        # 50%-os kedvezmény gyerekeknek

# 2. Üdvözlés (print)
print("Mozijegy kalkulátor")

# 3. Adatbekérés a felhasználótól (input)
nev = input("Add meg a neved: ")    # A néző neve szövegként
kor_szoveg = input("Add meg a korodat: ")   # Életkor szövegként

# 4. típusváltás (szöveget számmá alakítunk)
kor = int(kor_szoveg)   # '15' -> 15 (int), tehát számként

# 5. Elágazás (gyerek vagy felnőtt)
if kor < GYEREK_KORHATAR:
    # Ha a néző 14 év alatti, akkor gyerek jegyet kap
    fizetendo = int(ALAP_JEGYAR * GYEREK_KEDVEZMENY)
    print("Gyerek jegyet kapsz")
else:
    # Különben felnőtt jegyet fizet
    fizetendo = ALAP_JEGYAR
    print("Felnőtt jegyet kapsz")

# 6. Végösszeg kiiratása (print + változók)
print(nev, "jegyek ára:", fizetendo, "Ft")
