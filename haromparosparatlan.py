szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))
szam3 = int(input("Kérem a harmadik számot: "))

if szam1 % 2 == 0 and szam2 % 2 == 0 and szam3 % 2 == 0:
    print("Mindhárom páros.")

elif szam1 % 2 != 0 and szam2 % 2 != 0 and szam3 % 2 != 0:
    print("Mindhárom páratlan.")

else:
    print("Kevert.")