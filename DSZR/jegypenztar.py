def Kedvezmeny(tipus, eletkor, tanulo):
    if eletkor < 14 or eletkor >= 65:
        return 100
    
    if tipus == "bérlet" and tanulo == "igen":
        return 90
    if tipus == "menetjegy":
        if eletkor >= 14 and eletkor <= 25:
            return 50
    return 0

def FizetendoOsszeg(fizetendo, kedvezmeny):
    return fizetendo - (fizetendo * (kedvezmeny / 100))

eletkor = int(input("Kérem, adja meg az életkorát! "))
tipus = input("Mit szeretne vásárolni? (bérlet / menetjegy) ")
tanulo = input("Rendelkezik nappali vagy esti tanulói jogviszonnyal? (igen / nem) ")

kedvezmeny = Kedvezmeny(tipus, eletkor, tanulo)
if kedvezmeny == 100:
    print("Ön ingyenes utazásra jogosult.")

else:
    if kedvezmeny != 0:
        print(f"Ön {kedvezmeny}% kedvezményre jogosult.")
    if kedvezmeny == 0:
        print("Ön nem jogosult kedvezményre.")

    if tipus == "bérlet":
        berlet_tipus = input("Milyen típusú bérletet szeretne? (vármegye / ország) ")

        if berlet_tipus == "vármegye":
            fizetendo = 9450
        if berlet_tipus == "ország":
            fizetendo = 18900
        
        fizetendo = FizetendoOsszeg(fizetendo, kedvezmeny)
        
    if tipus == "menetjegy":
        utazasi_tavolsag = int(input("Milyen messzire szeretne utazni? (km) "))

        fizetendo = 400
        if utazasi_tavolsag > 10:
            utazasi_tavolsag = utazasi_tavolsag - 10

            for km in range(utazasi_tavolsag):
                fizetendo = fizetendo + 50
        
        fizetendo = FizetendoOsszeg(fizetendo, kedvezmeny)

    print(f"Fizetendő: {round(fizetendo)} Ft")