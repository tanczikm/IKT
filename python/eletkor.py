kor = int(input("Add meg az életkorod! "))

if 0 <= kor <= 14:
    print("Gyermek vagy.")

elif 15 <= kor <= 24:
    print("Fiatal vagy.")

elif 25 <= kor <= 64:
    print("Felnőtt vagy.")

elif 65 <= kor:
    print("Idős vagy.")
