# 1., Köszönjön a programod a napszaknak megfelelően a felhasználónak!
#       - Kérd be a nevét!
#       - Kérd be, hogy hány óra van!
#       Ha  10 óra előtti órát ír, írd ki neki, hogy: "Jó reggelt, NÉV!"
#           10-18 óráig, írd ki neki hogy: "Jó napot, NÉV!"
#           18 óra után: "Jó estét, NÉV!"

print("------------------------------------------------------------------------------------------------------")
print("Köszönő program")
print("------------------------------------------------------------------------------------------------------")

nev = input("Kérem, adja meg a nevét!           Név: ")
ido = int(input("Kérem, adja meg, hány óra van!     Idő: "))

print("------------------------------------------------------------------------------------------------------")

if ido < 10:
    print(f"Jó reggelt, {nev}!")
elif ido >= 10 and ido <= 18:
    print(f"Jó napot, {nev}!")
elif ido > 18:
    print(f"Jó estét, {nev}!")

print("------------------------------------------------------------------------------------------------------")