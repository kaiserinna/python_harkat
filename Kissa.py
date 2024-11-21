Kertaa = 0
while (Kertaa < 7):
    
    print("Kissa", end=" ")

    Kertaa = Kertaa + 1








for i in range(7):
    print(Alkuarvo + 1)




# Ohjelman aloitus
print("Tämä ohjela laskee huvipuiston lipputulot.")

# Muuttujat
Lippuhinta = int(12)
Ryhma = int(input("Anna ryhmän koko väliltä 1-10 henkilöä (0 lopettaa): "))

# Kysyy käyttäjältä huvipuistoon tulevien ryhmien kokoja
while (Ryhma != 0):
    homma(Ryhma)
    Ryhma = int(input("Anna ryhmän koko väliltä 1-10 henkilöä (0 lopettaa): "))
