# Két számot fogunk összehasonlítani
# Érdemes üdvözölni a felhasználót vagy leírni neki, hogy mit fogunk tőle kérni.

print("Két szám összehasonlítása")

# Be kell kérni a két értéket a felhasználótól
# Az input() mindig szövegként (stringként) jelenik meg, ezért int() függvénnyel számmá kell alakítani.
elso = int(input("Add megg az első számot: "))
masodik = int(input("Add meg a második számot: "))

# Elágazás (if - elif - else) segítségével döntjük el, melyik szám a nagyobb.

# Ha azt első szám (elso) nagyobb mint a második szám (masodik), akkor írja ki (print), hogy a nagyobb szám, az (elso).
if elso > masodik:
    print("A nagyobb szám:", elso)
# Ha azt második szám (masodik) nagyobb mint az első szám (elso), akkor írja ki (print), hogy a nagyobb szám, a (masodik).
elif masodik > elso:
    print("A nagyobb szám:", masodik)
# Egyéb esetben írja ki, hogy a két szám egyenlő.
else:
    print("A két szám egyenlő.")