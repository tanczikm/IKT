testsuly = float(input("Add meg a testsúlyod kg-ban! "))
magassag = float(input("Add meg a magasságod méterben! "))


bmi = (testsuly / (magassag * magassag))
bmi = round(bmi, 2)
print("A BMI értéked:", bmi)

