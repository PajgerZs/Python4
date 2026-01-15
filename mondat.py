mondat = input("Írj be egy mondatot: ").lower()

maganhangzok_kesszlet = "aáeéiíoóöőuúüű"

osszes_db = 0
reszletes_lista = {} 

for betu in mondat:
    if betu in maganhangzok_kesszlet:
        
        osszes_db += 1
        
        if betu in reszletes_lista:
            reszletes_lista[betu] += 1  
        else:
            reszletes_lista[betu] = 1   

print(f"Összes magánhangzó száma: {osszes_db}")
print("Részletezés:")

for maganhangzo, darab in reszletes_lista.items():
    print(f" - '{maganhangzo}': {darab} db")