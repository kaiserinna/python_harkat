print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.\nValitse haluamasi toiminto:")

print("1) Tulosta merkkijonon ensimmäinen puolikas")
print("2) Tulosta merkkijonon toinen puolikas")
print("3) Tulosta merkkijonon pituus")
print("0) Lopeta")

Valinta = int(input("Anna valintasi: "))
Merkkijono = input("Anna merkkijono: ")
Merkkijononpituus = len(Merkkijono)
Keskipiste = Merkkijononpituus//2
Kiitos = "\nKiitos ohjelman käytöstä."

if (Valinta == 1):
         print("Merkkijonon ensimmäinen puolikas on '" + Merkkijono[:Keskipiste] + "'." + Kiitos)
elif (Valinta == 2):
         print("Merkkijono toinen puolikas on '" + Merkkijono[Keskipiste:] + "'." + Kiitos)
elif (Valinta == 3):
        print("Merkkijonon pituus on " + str(Merkkijononpituus) + "." + Kiitos)
    
elif (Valinta == 0):
    print("Lopetetaan." + Kiitos)
else:
    print("Tuntematon valinta." + Kiitos)
