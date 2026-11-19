#cv 1 - list o libovolných 5 čisel pomoci for cyklu spočítat součet čísel. Výsledek vypište
jednoduchy_list = [3, 9, 7, 4, 1]

soucet= 0

for i in range(len(jednoduchy_list)):
    soucet= soucet + jednoduchy_list[i]

print(soucet)

#cv 2 list 5 libovolnych čísel a pomoci for cyklu vypište je v opačném pořadí

for i in range(len(jednoduchy_list)-1, -1, -1):
   # print(i)
    print(jednoduchy_list[i])

#cv 3 list pěti libovolných čísel a spočítejte pomoci for cyklu aritmetický průměr

muj_list = [1, 5, 5, 5, 7, 1, 2, 3]

soucet = 0
for i in range(len(muj_list)):
    soucet += muj_list[i]     # je to x = x+ 1  neboli    x += 1
   
prumer = soucet / len(muj_list)
print(prumer) 
# uloha 4 vytvořte list 5 čísel a vyberte nejvyší číslo z listu

nejlepsi_list = [9, 56 , 5, 0, 4, 6, 7, 66, 5]

max = nejlepsi_list[0]
for i in range(1, len(nejlepsi_list)):
    if nejlepsi_list[i] > max :
        max= nejlepsi_list[i]

print(max)
#další možnost 
# for item in nejlepsi_list:
#  print(item) ale vypisuje všechny prvky seznamu

#uloha 5:  vytvořte list 5 čísel a vyberte 2 největší číslo z listu
posledni_list = [1, 1, 3, 3, 3, 3, 4, 6, 8, 9, 7, 8, 7]


if posledni_list[0] > posledni_list[1]:
    max0 = posledni_list[0]
    max1 =posledni_list[1]
else :
    max0 = posledni_list[1]
    max1 = posledni_list[0]

for i in range(2, len(posledni_list)):
    if posledni_list[i] > max0:
        max1 = max1
        max0 = posledni_list[i]
    elif posledni_list[i] > max1:
        max1 = posledni_list[i]

print(f"Největší číslo je {max0} a druhé největší je {max1}")
