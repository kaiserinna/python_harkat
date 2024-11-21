######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112732
# Päivämäärä: 23.11.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, python docs,
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# L11T2.py


def kysyluku(Syote):
    Luku = int(input(Syote))
    return Luku

def laskePell(Luku):
    if (Luku == 0) or (Luku == 1):
        return Luku
    else:
        return 2 * laskePell(Luku - 1) + laskePell(Luku - 2)

def paaohjelma():
    print("Tämä ohjelma laskee Pell'n lukusarjaa.")
    Luku = kysyluku("Anna laskettavien lukujen määrä: ")
    if (Luku < 1 ):
        print("Kierroksia on oltava vähintään 1 kpl.")
    else:
        print("{0:d}. ensimmäistä Pell'n lukua:".format(Luku))
        for i in range(1, Luku +1):
            print("{0:d}. Pell'n luku: {1:d}".format(i, laskePell(i-1)))
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
#eof