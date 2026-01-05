# Írjon programot persely.py néven, ami addig kér be pénzösszegeket a felhasználótól, amíg össze nem gyűlik az 1000 Ft. Minden bekérés után írja ki, hogy mennyi hiányzik még az 1000 Ft-ig.

# Minta kód futtatáskor (ezt írja ki a programod, amikor teszteled!):
# (A félkövérrel írt számot a felhasználó írja be!)

# A cél: 1000 Ft összegyűjtése.
# Mennyit dobsz a perselybe? 500
# Még hiányzik: 500 Ft
# Mennyit dobsz a perselybe? 500
# Gratulálok! Összegyűlt 1000 Ft!

cel = 1000
print(f"A cél: {cel} Ft összegyűjtése.")
kell = cel
while True:
    bedob = int(input("Mennyi dobsz a perselybe? "))
    kell = kell - bedob
    if kell > 0:
        print(f"Még hiányzik: {kell} Ft")
    else:
        print(f"Gratulálok! Összegyűlt {cel} Ft!")
        break