def Siker(magassag):
    if magassag > 150:
        return "Átment"
    else:
        return "Leverte"
    
legnagyobb = 0

for kiserlet in range(1, 7):
    magassag = int(input(f"{kiserlet}. ugrás magassága (cm): "))

    if magassag > legnagyobb:
            legnagyobb = magassag

    if magassag < 50:
        print("Ez túl alacsony!")
        continue

    print(f"Eredmény: {Siker(magassag)}")

        
        
    
print("A legnagyobb próbálkozás:", legnagyobb, "cm")