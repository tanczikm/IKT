tavasz = ["március", "április", "május"]
nyar = ["június", "július", "augusztus"]
osz = ["szeptember", "október", "november"]
tel = ["december", "január", "február"]

honap = ""
while True:
    honap = input("Milyen hónap van ma? ")

    if honap in tavasz:
        print("Tavasz van.")
        break
    elif honap in nyar:
        print("Nyár van.")
        break
    elif honap in osz:
        print("Ősz van.")
        break
    elif honap in tel:
        print("Tél van.")
        break
    else:
        print("Nem létező hónapot adtál meg, add meg újra, nézd meg hogy jól írtad-e be a hónap nevét.")