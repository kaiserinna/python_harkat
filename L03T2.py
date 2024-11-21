print("Selvitetään sanojen aakkosjärjestys.")
Sana1 = input("Anna sana 1: ")
Sana2 = input("Anna sana 2: ")
if Sana1 < Sana2:
    print("'" + Sana1 +"' on aakkosissa aiemmin kuin '" + Sana2 + "'.\n")
elif Sana1 > Sana2:
    print("'" + Sana2 + "' on aakkosissa aiemmin kuin '" + Sana1 + "'.\n")
else:
    print("'" + Sana1 + "' on sama kuin '" + Sana2 + "'.\n")

print("Selvitetään merkin sisältyminen merkkijonoon.")
Valinta = input("Anna etsittävä merkki: ")
if (Valinta in Sana1):
    print("Merkki '" + Valinta + "' sisältyy merkkijonoon '" + Sana1 + "'.")
else:

    print("Merkki '" + Valinta + "' ei sisälly merkkijonoon '" + Sana1 + "'.")

if (Valinta in Sana2):
    print("Merkki '" + Valinta + "' sisältyy merkkijonoon '" + Sana2 + "'.\n")
else:
    print("Merkki '" + Valinta + "' ei sisälly merkkijonoon '" + Sana2 + "'.\n")

print("Selvitetään, onko sana palindromi.")
Testisana = input("Anna testattava sana: ")
Kiitos = "\nKiitos ohjelman käytöstä."
if (Testisana == Testisana[::-1]):
    print("Sana '" + Testisana + "' on palindromi." + Kiitos)
else:
    print("Sana ei ole palindromi.\nSana on etuperin '" + Testisana + "' ja takaperin '" + Testisana[::-1] + "'." + Kiitos)
