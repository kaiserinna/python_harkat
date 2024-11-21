# Ohjelman alustus

print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
Kokonaisarvo = 0

# Loop
while (True):
    print("Valitse haluamasi toiminto:\n1) Kysy setelin arvo\n2) Kysy setelien lukumäärä\n3) Laske kokonaisarvo\n4) Tulosta tulos\n0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    if (Valinta == 1):
        Arvo = int(input("Anna analysoitavan setelin arvo: "))
        print()
    elif (Valinta == 2):
        Lukumaara = int(input("Anna setelien lukumäärä: "))
        print()
    elif (Valinta == 3):
        print("Setelien kokonaisarvo laskettu.")
        print()
    elif (Valinta == 4):
        Kokonaisarvo = Arvo * Lukumaara
        print("Setelien kokonaisarvo on", Kokonaisarvo, "euroa.")
        print()
    elif (Valinta == 0):
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta, yritä uudestaan.")

# Loppu
print()
print("Kiitos ohjelman käytöstä.")
