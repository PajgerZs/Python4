n = int(input("Adj meg egy egész számot (n): "))

szamok_lista = list(range(1, n + 1))

oszthatok = []  
osszeg = 0      

for szam in szamok_lista:
    if szam % 3 == 0:
        oszthatok.append(szam) 
        osszeg += szam         

print(f"A 3-mal osztható számok: {oszthatok}")
print(f"Ezek összege: {osszeg}")