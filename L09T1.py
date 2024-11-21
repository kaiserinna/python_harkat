######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112732
# Päivämäärä: 10.11.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, ohjelmointiopas
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# L09T1.py

import sys

def lueTiedostoListaan(Nimi, Lista):
    Lista.clear()
    try:
        Tiedosto = open(Nimi, 'r')
        Rivi = Tiedosto.readline()
        while (len(Rivi) > 0):
            RiviSiivottu = Rivi[:-1]
            Lista.append(RiviSiivottu)
            Rivi = Tiedosto.readline()
        Tiedosto.close()
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)
    print("Tiedosto '{0:s}' luettu.".format(Nimi))
    return Lista

def kirjoitaTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, 'w')
        for Rivi in Lista:
            Tiedosto.write(str(Rivi) + "\n")
        Tiedosto.close()
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)
    print("Tiedoston '{0:s}' kirjoittaminen onnistui.".format(Nimi))
    Lista.clear()
    return None

def paaohjelma():
    Lista = []
    TiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    Lista = lueTiedostoListaan(TiedostonNimi, Lista)
    KTiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitaTiedosto(KTiedostonNimi, Lista)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

#eof