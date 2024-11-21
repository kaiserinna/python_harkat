def tiedostoKirjoita(TiedostonNimi):
    Tiedosto = open(TiedostonNimi, 'w', encoding ="utf-8")
    Rivi = "Kissa"
    while (len(Rivi) > 0):
        Rivi = input("Anna tiedostoon tallennettava desimaaliluku (enter lopettaa): ")
        if (len(Rivi) > 0):
            Tiedosto.write(Rivi + "\n")
    Tiedosto.close()
    print("Tiedosto '" + TiedostonNimi + "' kirjoitettu.")
    return None

def paaohjelma():
    TiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    Kirjoittaa = tiedostoKirjoita(TiedostonNimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
