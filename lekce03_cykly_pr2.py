vstup = input("Zadejte číslo: ")
cislo= int(vstup)

while cislo >=0:
    print(cislo)
    cislo = cislo-1
    continue

for i in   range(cislo, -1, -1):
    print(cislo-i)

a=int(input("Císlo sem: "))
for i in range(a+1):
    print(a-i)

print("Konec")

# uživatel zada cislo vzpíśou se suda císla od nuly do znameho cisla

y = int(input("Zadejte číslo prosím: "))

for i in range(y+1):
    if y % 2 == 0:
      print(i)
#druha možnost
for i in range(0,y+1,2):
    print(i)
# uživatel zada číslo a program vypíše císlo od 0 do zadaného čísla včetně a vypíse zda je číslo sůdé či liché

z = int(input("Zadejte číslo: "))
for i in range(z+1):
    print(i)
    if i % 2 == 0:
        print("Číslo je sudé")
    else:
        print("Čislo je liché")