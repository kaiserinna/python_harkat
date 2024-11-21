def tiedostoLue(TiedostonNimi):
    Tiedosto = open(TiedostonNimi, 'r', encoding="utf-8")
    Summa = 0
    Maara = 0
    Rivi = Tiedosto.readline()
    while (Rivi != ""):
        Kasvaa = float(Rivi)
        Summa = Summa + Kasvaa
        Maara = Maara + 1
        Rivi = Tiedosto.readline()
        
    Keskiarvo = Summa / Maara
    print("Tiedostossa '" + TiedostonNimi + "' oli " + str(Maara) + " lukua.")
    print("Lukujen keskiarvo oli", str(round(Keskiarvo, 2)), "ja summa " + str(round(Summa, 2)) + ".")
    Tiedosto.close()
    return None

def paaohjelma():
    TiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    tiedostoLue(TiedostonNimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
