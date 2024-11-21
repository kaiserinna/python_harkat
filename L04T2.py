# Ohjelman aloitus
print("Tämä ohjelma laskee huvipuiston lipputulot.")

# Muuttujat
Lippuhinta = int(12)
KumulatTuotto = 0
Montakohlo = 0
Montakoryhmaa = 0

# Kysyy käyttäjältä huvipuistoon tulevien ryhmien kokoja
while (True):
    Ryhma = int(input("Anna ryhmän koko väliltä 1-10 henkilöä (0 lopettaa): "))
    if (Ryhma >= 1) and (Ryhma <= 10):
        Tuotto = Ryhma * Lippuhinta
        Montakohlo = Montakohlo + Ryhma
        KumulatTuotto = KumulatTuotto + Tuotto
        Montakoryhmaa = Montakoryhmaa + 1
    elif (Ryhma == 0):
        break
    else:
        print("Syöte ei ole annetulla välillä, yritä uudestaan.")
        
print("Päivän tuotto oli", round(float(KumulatTuotto), 1), "euroa.")


# Tulostaa niiden keskiarvon pyöristettynä kokonaisluvuksi
Keskiarvo = Montakohlo / Montakoryhmaa
print("Ryhmän keskimääräinen koko oli", round(Keskiarvo), "henkilöä.")

# Lopetus
print("Kiitos ohjelman käytöstä.")









    
