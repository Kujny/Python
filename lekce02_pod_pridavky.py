zdany_vek = input("Kolik vám je let? ")
vek = int(zdany_vek)

if(vek) >= 18 :
    print("Jste dospělý a je vám " + str(vek))
else :
    print("Nejste dospělý")
    chyby = 18 - vek
    if chyby <= 4 :
     if chyby <= 1:
         print("Do dospělosti vám zbývá " + str(chyby) + " rok.")
     else :
        print("Do dospělost vám zbívají " + str(chyby) + " roky.")
    else :
     print("DO dospelosti vám chybý " + str(chyby) + " let")
