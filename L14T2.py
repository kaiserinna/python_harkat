######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero: 001080362
# Päivämäärä: 30.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, python docs,
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# L14T2.py

import string
import random

KIRJAIMET = string.ascii_letters
NUMEROT = string.digits
ERIKOISMERKIT = string.punctuation

def valikko():
    print("Luo salasana käyttäen:")
    print("1) Kirjaimia\n2) Kirjaimia ja numeroita\n3) Kirjaimia, numeroita ja erikoismerkkejä\n0) Lopeta")
    Valinta = int(input("Valintasi: "))
    return Valinta

def luoSalasana(Pituus, Merkit):
    Salasana = ""
    for i in range (Pituus):
        Salasana += random.choice(Merkit)
    return Salasana

def paaohjelma():
    random.seed(8989)
    print("Tämä ohjelma luo satunnaisia salasanoja.")
    while (True):
        Valinta = valikko()
        if (Valinta == 1):       
            Pituus = int(input("Anna luotavan salasanan pituus: "))
            Salasana = luoSalasana(Pituus, KIRJAIMET)
        elif (Valinta == 2):
            Pituus = int(input("Anna luotavan salasanan pituus: "))
            Salasana = luoSalasana(Pituus, KIRJAIMET + NUMEROT)
        elif (Valinta == 3):
            Pituus = int(input("Anna luotavan salasanan pituus: "))
            Salasana = luoSalasana(Pituus, KIRJAIMET + NUMEROT + ERIKOISMERKIT)
        elif (Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta.")
        print("Luotiin {0:d} merkkiä pitkä salasana:\n{1:s}\n".format(Pituus, Salasana))
    print()
    print("Kiitos ohjelman käytöstä.")
            
    return None

paaohjelma()


# eof
