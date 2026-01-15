szam = int(input("Adj meg egy egész számot: "))

if szam == 0:
    print("A szám nulla.")

elif szam > 0 and szam % 2 == 0:
    print("Pozitív páros.")

elif szam > 0 and szam % 2 != 0:
    print("Pozitív páratlan.")

elif szam < 0 and szam % 2 == 0:
    print("Negatív páros.")

else:
    print("Negatív páratlan.")