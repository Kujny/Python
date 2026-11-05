zad_cislo = input("Zadejte číslo: ")

cislo = int(zad_cislo)

zbytek = cislo % 2
if zbytek == 0 :
    print(f"Číslo {cislo} je sudé")
else:
    print(f"číslo {cislo} je liché") 