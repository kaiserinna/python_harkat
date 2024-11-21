# Hinta alle 5e - A
# Hinta alle 10e - B
# Hinta alle 25e - C
# Hinta alle 50e - D
# Hinta 50e tai enemmän - E

print("Selvitetään tuotteen hintaluokka.")
Hinta = float(input("Anna tuotteen hinta: "))
print("Selvitetäänkö luokka\n1) yhdellä monihaaraisella valintarakenteella\n2) useilla erillisillä valintarakenteilla?")
Valinta = int(input("Anna valintasi: "))
print()
print("Annoit tuotteen hinnaksi", Hinta, "euroa.")
Kiitos = "Kiitos ohjelman käytöstä."

if (Valinta == 1):
    #tapa1
    if (Hinta < 5.0):
        Luokka = "A"
    elif (Hinta < 10.0):
        Luokka = "B"
    elif (Hinta < 25.0):
        Luokka = "C"
    elif (Hinta < 50.0):
        Luokka = "D"
    elif (Hinta >= 50.0):
        Luokka = "E"
elif (Valinta == 2):
    #tapa2
    if (Hinta < 5.0):
        Luokka = "A"
    if (Hinta < 10.0):
        Luokka = "B"
    if (Hinta < 25.0):
        Luokka = "C"
    if (Hinta < 50.0):
        Luokka = "D"
    if (Hinta >= 50.0):
        Luokka = "E"
else:
    #reject
    print("Tuntematon valinta.")

print("Tuotteen hintaluokka on tällöin " + Luokka + ".")
print(Kiitos)
