magas = int(input("A torony magassága (m): "))

if magas < 30:
    print("A torony alacsony.")

elif magas > 100:
    print("A torony magas.")

elif magas >= 30 and magas <= 100:
    print("A torony megfelelő magasságú.")