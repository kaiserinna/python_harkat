######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112732
# Päivämäärä: 30.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, python docs,
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# L11T1.py

import math

def kysyluku(Syote):
    Luku = int(input(Syote))
    return Luku

def laskeneper(Luku):
    Neperinluku = 0.0
    for i in range(Luku):
        Neperinluku += 1 / math.factorial(i)
    return Neperinluku

def paaohjelma():
    print("Tämä ohjelma laskee Neperin luvulle desimaaleja.")
    Luku = kysyluku("Anna kierrosten määrä: ")
    Neper = laskeneper(Luku)
    print("Neperin luvun likiarvo annetulla kierrosten määrällä:\n{0:.20g}".format(Neper))
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
#eof