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
# Tehtävä L08T1Kirjasto.py

VERSIONUMERO = 1.0

EUR2USD = 1.0558
EUR2SEK = 11.6155
USD2SEK = 11.0057

def eurotKruunuiksi(Euro):
    Kruunu = Euro * EUR2SEK
    return Kruunu

def eurotDollareiksi(Euro):
    Dollari = Euro * EUR2USD
    return Dollari

def dollaritEuroiksi(Dollari):
    Euro = Dollari / EUR2USD
    return Euro

def kruunutEuroiksi(Kruunu):
    Euro = Kruunu / EUR2SEK
    return Euro

def dollaritKruunuiksi(Dollari):
    Kruunu = Dollari * USD2SEK
    return Kruunu

def kruunutDollareiksi(Kruunu):
    Dollari = Kruunu / USD2SEK
    return Dollari

# eof