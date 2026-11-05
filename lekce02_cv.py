zad_stra = input("Zadejte stranu a: ")
zad_strb = input("Zadejte stranu b: ")
zad_strc = input("zadejte stranu c: ")

a = float(zad_stra)
b = float(zad_strb)
c = float(zad_strc)

if a+b>c and a+c >b and b+c>a :
    print("Trojůhelník je sestrojitelný")
else :
    print("Tento trojůhelník nelze sestrojit")