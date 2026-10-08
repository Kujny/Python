vek = 14
print("Můj vek je: " + str(vek))

if vek >= 18 :
    print("Jsem dospělý.")
    print("A můžu řídit.")
if vek >= 65:
    print("Jsem důchodce")
    print("dostanu hypoteku na 90 let")
elif vek >= 15 and vek <=17:
    print("Jsem maldictví")
    print("Nejsem dospělý a mužu řídit jen pod dozorem rodičů")
elif vek <=14:
    print("jsem špunt")

print("Tečka.")

print("*"*20)

muj_vek = 21
if muj_vek >= 18:
    print("jsem dospělý, protože je mi " + str(muj_vek))
    if muj_vek >= 65 : 
        print("Dostavám peníze za krmení holubů")
    else:
        print("Codím do školy")
else: 
    print("Jsem dítě")