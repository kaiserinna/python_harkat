# Aloitus
print("Tämä ohjelma tarkistaa käyttäjätunnuksen oikeellisuuden.")
Minimipituus = input("Anna tunnuksen minimipituus: ")
Ekamerkki = input("Anna tunnuksen ensimmäinen merkki: ")
print()
Tunnus = None
Kielletty1 = " "
Kielletty2 = "!"
Kielletty3 = ";"

# Loop
while (True):
    Tunnus = input("Anna tarkistettava tunnus: ")
    if (int(len(Tunnus)) < int(Minimipituus)):
        print("Tunnus ei ole riittävän pitkä, yritä uudelleen.")
    elif (Kielletty1 in Tunnus) or (Kielletty2 in Tunnus) or (Kielletty3 in Tunnus):
        print("Tunnus ei saa sisältää välilyöntiä tai merkkejä '!' ja ';', yritä uudelleen.")
    elif (Tunnus[0] != Ekamerkki):
        print("Tunnuksen ensimmäinen merkki ei ole '" + Ekamerkki + "', yritä uudelleen.")
    else:
        print("Tunnus täyttää ehdot, lopetetaan.")
        break

# Loppu
print("Kiitos ohjelman käytöstä.")


