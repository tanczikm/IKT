def Birsag(kesesIdo):
    if kesesIdo <= 5:
        birsag = 0
    elif kesesIdo <=10:
        birsag = 500
    else:
        birsag = 1000
    return birsag

beszedettBirsag = 0

print("Könyvtári Késés Kalkulátor")

while True:
    kesesNap = int(input("Hány napot késett? (-1 a kilépés): "))

    if kesesNap < -1:
        print("Hibás adat!")

    elif kesesNap == -1:
        print("A teljes beszedett bírság:", beszedettBirsag, "Ft")
        break
    else:
        print("A bírság:", Birsag(kesesNap), "Ft")
        beszedettBirsag = beszedettBirsag + Birsag(kesesNap)
