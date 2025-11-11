# Véletlen szám generálása
import random

# A játékos és a gép dob a dobókockával 1-től 6-ig
jatekos = random.randint(1,6)
gep = random.randint(1,6)

# Írjuk ki, hogy milyen számot dobott a játékos és a gép
print("A játékos dobása:", jatekos)
print("A gép dobása:", gep)

# El kell dönteni, hogy ki nyert, egyszerű elágazással.
if jatekos > gep:
    print("A játékos nyert.")
elif gep > jatekos:
    print("A gép nyert.")
else:
    print("Döntetlen.")