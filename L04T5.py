print("Tämä ohjelma laskee Collatz-sarjoja.")
Arvo = int(input("Anna alkuarvo: "))
Termi = 0
Alkuarvo = Arvo
print("Luvun", Arvo, "Collatz-jakso on:")

while (Arvo != 1):
    
    if (Arvo % 2 == 1):
        print(int(Arvo), end=" -> ")
        Arvo = 3 * Arvo +1
        Termi = Termi + 1
    elif (Arvo % 2 == 0):
        print(int(Arvo), end=" -> ")
        Arvo = Arvo / 2
        Termi = Termi + 1
        
print(Arvo)
print("Luvun", Alkuarvo, "Collatz-jaksossa on", Termi + 1, "termiä.")
print("Kiitos ohjelman käytöstä.")
