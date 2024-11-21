print("Tämä ohjelma laskee pituuksien yksikkömuunnoksia.")

Tuumina1 = float(input("Anna pituus tuumina: "))
Tuumina1d = round(Tuumina1, 1)
Muuntokerrointuumatocm = float(2.54)
Senttimetreina1 = Tuumina1 * Muuntokerrointuumatocm
Senttimetreina1d = round(Senttimetreina1, 1)

Tuumina = str(Tuumina1d)
Senttimetreina = str(Senttimetreina1d)
print("Pituus on " + Tuumina + " tuumaa eli " + Senttimetreina + " senttimetriä.")

Maileina1 = float(input("Anna pituus maileina: "))
Maileina1d = round(Maileina1, 2)
Maileina = str(Maileina1d)

Muuntokerroinmailitokm = 1.609344

Kilometreina1 = Maileina1 * Muuntokerroinmailitokm
Kilometreina1d = round(Kilometreina1, 2)
Kilometreina = str(Kilometreina1d)

print("Pituus on " + Maileina + " mailia", end=" ")
print("eli " + Kilometreina + " kilometriä.")
print("Kiitos ohjelman käytöstä.")
