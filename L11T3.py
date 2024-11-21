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
# L11T3.py

import sys

def kysyluku(Syote):
    Luku = int(input(Syote))
    return Luku

def laskefibonacci(Luku):
    if (Luku == 0) or (Luku == 1):
        return Luku
    else:
        return laskefibonacci(Luku - 1) + laskefibonacci(Luku - 2)

def paaohjelma():
    print("Tämä ohjelma laskee Fibonaccin luvun rekursiivisesti.")
    Luku = kysyluku("Anna luku, jolle Fibonaccin luku lasketaan: ")
    if (Luku < 0 ):
        print("Luvun tulee olla positiivinen kokonaisluku.")
        sys.exit(0)
    else:
        Fibonacci = laskefibonacci(Luku)
        print("Fibonaccin luku luvulle {0:d} on {1:d}.".format(Luku, Fibonacci))
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
#eof