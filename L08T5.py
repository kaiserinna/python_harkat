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
# Tehtävä L08T5.py

import L08T5Kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    Valinta1 = int(input("Anna valintasi: "))
    return Valinta1


def paaohjelma():
    TuotetietojenLista = []
    AnalysoituLista = []
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            TiedostonNimi = L08T5Kirjasto.kysyTiedosto("Anna luettavan tiedoston nimi: ")
            TuotetietojenLista = L08T5Kirjasto.lueTiedosto(TiedostonNimi, TuotetietojenLista)
            print("Tiedostosta lisättiin " + str(len(TuotetietojenLista)) + " datariviä listaan.")
        elif (Valinta == 2):
            AnalysoituLista = L08T5Kirjasto.analysoi(TuotetietojenLista, AnalysoituLista)
        elif (Valinta == 3):
            TiedostonNimiKirj = L08T5Kirjasto.kysyTiedosto("Anna kirjoitettavan tiedoston nimi: ")
            L08T5Kirjasto.kirjoitaTiedosto(TiedostonNimiKirj, AnalysoituLista)             
        elif (Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    TuotetietojenLista.clear()
    AnalysoituLista.clear()
    print("Kiitos ohjelman käytöstä.")


paaohjelma()
