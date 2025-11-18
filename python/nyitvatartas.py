nyitvatartas = int(input("Kérlek add meg, hány óra van! "))

if nyitvatartas < 8:
    print("A bolt zárva van még, 8 órakor fog nyitni. Várnod kell még", 8 - nyitvatartas, "órát.")

elif nyitvatartas < 16:
    print("A bolt nyitva van, vásárolj nyugodtan, van még", 16 - nyitvatartas, "órád a zárásig.")

elif nyitvatartas >= 16:
    print("A bolt zárva van, holnap fog nyitni majd 8-kor. Menj haza, aludj egyet.")