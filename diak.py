class Diak:
    def __init__(self, nev, eletkor, jegyek):
        self.nev = nev              
        self.eletkor = eletkor      
        self.jegyek = jegyek        

    def atlag(self):
        if len(self.jegyek) == 0:  
            return 0
        return sum(self.jegyek) / len(self.jegyek)

    def bemutatkozas(self):
        print(f"Szia, {self.nev} vagyok, {self.eletkor} éves.")

    def szinten(self):
        aktualis_atlag = self.atlag()
        
        if aktualis_atlag >= 4.0:
            return "Jó"
        elif aktualis_atlag >= 3.0:
            return "Közepes"
        else:
            return "Gyenge"

diak1 = Diak("Anna", 17, [5, 4, 5, 5, 4])
diak2 = Diak("Péter", 16, [2, 3, 2, 4, 1])

print("--- 1. Diák ---")
diak1.bemutatkozas()
print(f"Átlag: {diak1.atlag()}")
print(f"Szint: {diak1.szinten()}")

print("\n--- 2. Diák ---")
diak2.bemutatkozas()
print(f"Átlag: {diak2.atlag()}")
print(f"Szint: {diak2.szinten()}")