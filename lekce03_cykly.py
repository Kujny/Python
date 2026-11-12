x = 10

while(x>5):
    print("ahoj")
    x=x-1
    if x == 7 :
        continue
    print(x)


print("konec?")

a = 10

while(a>5):
    print("ahoj")
    a = a-1
    if a == 7 :
        break
    print(a)


print("konečně konec?")

while True:
    print("Vyber možnost: A: napis ahoj, X: konec")
    y = input("Zadej volbu: ")
    if y == "A":
        print("Ahoj")
    if y == "X":
        break