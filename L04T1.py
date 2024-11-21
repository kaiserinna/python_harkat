# Muuttujat
Alkuarvo = int(input("Anna alkuarvo: "))
Kertaa = int(input("Kuinka monta seuraavaa tulostetaan: "))
print()

#
# Toteutus for -lauseella:
print("Toteutus for-lauseella:")
for i in range(Alkuarvo, Alkuarvo + Kertaa + 1):
    print(i, end=" ")

#
# Toteutus while-lauseella:
print()
print()
print("Toteutus while-lauseella:")
I = 0
while (I < Kertaa + 1):
    if (I < Kertaa):
        Loppu = " "
    else:
        Loppu = "\n"
        
    print(Alkuarvo + I, end=Loppu)
    I = I + 1

#
# Kiitos:
print()
print()
print("Kiitos ohjelman käytöstä.")
