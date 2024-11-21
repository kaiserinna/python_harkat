######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112732
# Päivämäärä: 12.11.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, ohjelmointiopas
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# L09T3Kirjasto.py

import L09T3Kirjasto

def valikko():
    try:
        print("Mitä haluat tehdä:")
        print("1) Lue tiedosto")
        print("2) Analysoi")
        print("0) Lopeta")
        Valinta = int(input("Valintasi: "))
    except:
        print("Virhe, valinta ei ollut kokonaisluku.")
        Valinta = int(input("Valintasi: "))
    return Valinta

def paaohjelma():
    Lista = []
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            TiedostonNimi = L09T3Kirjasto.kysyy("Anna luettavan tiedoston nimi: ")
            Lista = L09T3Kirjasto.lueTiedostoListaan(Lista, TiedostonNimi)
        elif (Valinta == 2):
            Paiva =  L09T3Kirjasto.kysypaiva()
            L09T3Kirjasto.analysoi(Lista, Paiva)
        elif (Valinta == 0):
            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
#eof