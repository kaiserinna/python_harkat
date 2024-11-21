Sana = input("Anna merkkijono: ")

print("Antamasi merkkijonon pituus oli " + str(len(Sana)) + " merkkiä.\n")

print("Antamasi merkkijonon kaksi ensimmäistä kirjainta ovat " + Sana[0:2])

print("Merkkijonon viisi viimeistä kirjainta ovat " + Sana[-5:])

print("Kirjaimet 5, 6, 7 ja 8 ovat " + Sana[4:9] + "\n")

print("Merkkijonon joka toinen kirjain alkaen ensimmäisestä kirjaimesta: " + Sana[0::2] + "\n")

print("Antamasi merkkijono '" + Sana + "' on takaperin '" + Sana[::-1] + "'.\n")

Aloituspaikka = int(input("Anna aloituspaikka: "))
Lopetuspaikka = int(input("Anna lopetuspaikka: "))
Siirtymä = int(input("Anna siirtymä: "))
print("Antamillasi asetuksilla merkkijono " + Sana + " tulostuu näin: " + Sana[Aloituspaikka:Lopetuspaikka:Siirtymä] + "\n")
print("Kiitos ohjelman käytöstä.")
