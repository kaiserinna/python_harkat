######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112732
# Päivämäärä: 30.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, python docs, googletus olio-ohjelmoinnista 
# VSCoden debugging selvittänyt hyvin listojen sisältöjä
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# L10T2.py

import sys

class YHTEYSTIEDOT:
    Nimi = None # str
    Puhelinnumero = None # str
    Osoite = None # str

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lisää osoitekirjaan")
    print("2) Poista osoitekirjasta")
    print("3) Tulosta osoitekirja")
    print("0) Lopeta")
    try:
        Valinta1 = int(input("Anna valintasi: "))
    except ValueError:
        print("Virhe, valinta ei ollut kokonaisluku.")
        Valinta1 = int(input("Anna valintasi: "))
    return Valinta1

def lisaaOsoitekirjaan(Lista):
    print("Anna lisättävän henkilön tiedot.")
    try:
        Tiedot = YHTEYSTIEDOT()
        Tiedot.Nimi = input("Nimi: ")
        Tiedot.Puhelinnumero = input("Puhelinnumero: ")
        Tiedot.Osoite = input("Osoite: ")
        Lista.append(Tiedot)
    except OSError:
        print("Listan käsittelyssä tapahtui virhe, lopetetaan")
        sys.exit(0)
    print("Henkilö '{0:s}' lisätty osoitekirjaan.".format(Tiedot.Nimi))
    return Lista
    

def poistaYhteystieto(Lista):
    Nimi = input("Anna poistettavan henkilön nimi: ")
    Löytyi = False
    for i in Lista:
        if (Nimi == i.Nimi):
            Lista.remove(i)
            Löytyi = True
            print("Henkilö '{0:s}' poistettu osoitekirjasta.".format(Nimi))
    if (Löytyi == False):
        print("Henkilöä '{0:s}' ei löydy osoitekirjasta.".format(Nimi))      
    return Lista

def tulostaOsoitekirja(Lista):
    Nimi = input("Anna tulostettavan henkilön nimi tai jätä tyhjäksi: ")
    Löytyi = False
    try:
        if (Nimi == ""):
            print("Osoitekirjassa on seuraavat henkilöt:")
            for i in Lista:
                print("Nimi: {0:s}".format(i.Nimi))
                print("Puhelinnumero: {0:s}".format(i.Puhelinnumero))
                print("Osoite: {0:s}".format(i.Osoite))
                print()
        else:
            for i in Lista:
                if (i.Nimi == Nimi):
                    print("Nimi: {0:s}".format(i.Nimi))
                    print("Puhelinnumero: {0:s}".format(i.Puhelinnumero))
                    print("Osoite: {0:s}".format(i.Osoite))  
                    Löytyi = True 
            if (Löytyi == False):
                print("Henkilöä '{0:s}' ei löydy osoitekirjasta.".format(Nimi))          
    except Exception:
        print("Henkilöä '{0:s}' ei löydy osoitekirjasta.".format(Nimi))
    return None

def paaohjelma():
    Lista = []
    Sanakirja = {}
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            lisaaOsoitekirjaan(Lista)
        elif (Valinta == 2):
            if (len(Lista) > 0):
                Lista = poistaYhteystieto(Lista)
            else:
                print("Osoitekirja on tyhjä.")
        elif (Valinta == 3):
            if (len(Lista) > 0):
                tulostaOsoitekirja(Lista)
            else:
                print("Osoitekirja on tyhjä.")
        elif (Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    Lista.clear()
    Sanakirja.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
#eof