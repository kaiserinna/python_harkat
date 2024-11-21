Nimi = input("Kerro nimesi: ")
Syote = input("Anna haalarimerkkien määrä kokonaislukuna: ")
Maara = int(Syote)
Syote2 = input("Anna haalarimerkkien hinta desimaalilukuna: ")
Hinta = float(Syote2)
Arvo = Maara * Hinta

print(Nimi, "annoit lukumääräksi", Maara, "ja hinnaksi", Hinta)
print("Haalarimerkkien arvo on tällöin", Arvo)
print("Kiitos ohjelman käytöstä.")
