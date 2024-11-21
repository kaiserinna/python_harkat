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
# L09T2.py


def valikko():
    try:
        print("Mitä haluat tehdä:")
        print("1) Testaa ValueError")
        print("2) Testaa IndexError")
        print("3) Testaa ZeroDivisionError")
        print("4) Testaa TypeError")
        print("0) Lopeta")
        Valinta = int(input("Valintasi: "))
    except:
        print("Virhe, valinta ei ollut kokonaisluku.")
        Valinta = int(input("Valintasi: "))
    return Valinta

def testaaValueError():
    print("Valikko-ohjelma testaa ValueError'n.")
    return None

def testaaIndexError():
    Lista = [11, 22, 33, 44, 55]
    Indeksi = int(input("Anna indeksi 0-4: "))
    try:
        print("Listan arvo on {0:d} indeksillä {1:d}.".format(Lista[Indeksi], Indeksi))
    except IndexError:
        print("Tuli IndexError, indeksi oli {0:d}.".format(Indeksi))
    return None

def testaaZeroDivisionsError():
    Jakaja = int(input("Anna jakaja: "))
    try:
        Tulos = 12 / Jakaja
        print("12/{0:1d} on {1:.1f}.".format(Jakaja, Tulos))
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja oli {0:d}.".format(Jakaja))
    return None

def testaaTypeError():
    Numero = input("Anna numero: ")
    try:
        Tulos = Numero * Numero
        print("{0:1d}*{0:1d} on {1:.2d}.".format(Numero, Tulos))
    except TypeError:
        print("Tuli TypeError, {0:s}*{0:s} merkkijonoilla ei onnistunut.".format(Numero))
    return None

def paaohjelma():
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            testaaValueError()
        elif (Valinta == 2):
            testaaIndexError()
        elif (Valinta == 3):
            testaaZeroDivisionsError()
        elif (Valinta == 4):
            testaaTypeError()
        elif (Valinta == 0):
            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
#eof