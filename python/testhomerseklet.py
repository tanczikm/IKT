#  <36          -   kihűlt
#  36-37        -   normál
#  37,1-38      -   hőemelkedés
#  38,1-39,5    -   lázas
#  39,5-42      -   nagyon magas láz

import time

testho = float(input("Kérlek add meg a testhőmérsékleted: "))

if testho < 36:
    valasz = "Kihűltél, takarózz be, igyál meleg teát."

elif testho >= 36 and 37 >= testho:
    valasz = "Normál teshőmérsékleted van, jól vagy."

elif testho >= 36.1 and 38 >= testho:
    valasz = "Hőemelkedésed van, pihenj le."

elif testho >= 38.1 and 39.5 >= testho:
    valasz = "Lázas vagy, szedjél be valami szert aztán aludjál."

elif testho >= 39.5 and 42 >= testho:
    valasz = "Ez már nem vicc, hívjál mentőt, irány a kórház."

elif testho >= 42.1:
    valasz = "Meleg vagy."

print("")
print("")
print("")
print("-------------------------------------------------------------------------------")
print("                                ORVOSI DIAGNÓZIS                               ")
print("     Kiállította: Dr Python")
print("     Dátum: 2025. 11. 18.")
print("")
print("     Diagnózis:", valasz)
print("")
print("-------------------------------------------------------------------------------")
