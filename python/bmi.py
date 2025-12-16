testsuly = float(input("Add meg a testsúlyod kg-ban! "))
magassag = float(input("Add meg a magasságod méterben! "))


bmi = (testsuly / (magassag * magassag))
bmi = round(bmi, 2)
print(f"A BMI értéked: {bmi}")

# Függvény hívásánál
print(f"Eredmény: {round(25.48475, 1)}") # Eredmény: 25,5

#Egy tanuló adatainak használata

tanulo = {
    "nev": "Péter",
    "kor": 42,
    "magassag": "175"
}

# Helyörző használata

print("BMI értéked: {}".format(23.15))