######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112732
# Päivämäärä: 30.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, python docs
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Harjoitustehtävä Perustaso

import HTPerusKirjasto

def valikko():

    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset sademäärät")
    print("0) Lopeta")
    try:
        Valinta1 = int(input("Anna valintasi: "))
    except ValueError:
        print("Virhe, valinta ei ollut kokonaisluku.")
        Valinta1 = int(input("Anna valintasi: "))
    return Valinta1
    

def paaohjelma():
    SadetietojenLista = []
    AnalysoituLista = []
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            TiedostonNimi = HTPerusKirjasto.kysyTiedosto("Anna luettavan tiedoston nimi: ")
            SadetietojenLista = HTPerusKirjasto.lueTiedosto(TiedostonNimi, SadetietojenLista)
            print("Tiedostosta lisättiin " + str(len(SadetietojenLista)) + " datariviä listaan.")
        elif (Valinta == 2):
            if (len(SadetietojenLista) > 0):
                AnalysoituLista = HTPerusKirjasto.analysoi(SadetietojenLista, AnalysoituLista, TiedostonNimi)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        elif (Valinta == 3):
            if (len(AnalysoituLista) > 0):
                TiedostonNimi = HTPerusKirjasto.kysyTiedosto("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.kirjoitaTiedosto(TiedostonNimi, AnalysoituLista) 
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
        elif (Valinta == 4):
            if (len(AnalysoituLista) > 0):
                ViikonpvtiedostonNimi = HTPerusKirjasto.kysyTiedosto("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.teeTiedostoViikonpaivista(ViikonpvtiedostonNimi, AnalysoituLista)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        elif (Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    SadetietojenLista.clear()
    AnalysoituLista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
