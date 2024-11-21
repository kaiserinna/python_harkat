######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112732
# Päivämäärä: 30.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot, python docs, googletus olio-ohjelmoinnista 
# VSCoden debugging selvittänyt hyvin listojen sisältöjä
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# L10T1.py

import sys


# Aliohjelma saa parametrina tyhjän listan, joka varmuuden vuoksi 
# tyhjennetään aluksi. Aliohjelma tekkee listan, joka koo

def lueTiedostoListaan(Nimi, Lista):
    Lista.clear()
    Tiedosto = open(Nimi, 'r', encoding="utf-8")
    Tiedosto.readline()
    Rivi = Tiedosto.readline()
    while (len(Rivi) > 0):
        Alkiot = Rivi.split(";")
        Syy = Alkiot[2]
        Lista.append(Syy)
        Rivi = Tiedosto.readline()
    return Lista

def montakoHeittoa(Lista, Syy):
    Heittoja = 0
    for i in Lista:
        if (i == Syy):
            Heittoja += 1
    return Heittoja

    #lajittelee syyt listasta sanakirjaan
def analysoi(Lista, Sanakirja, Jarjestetty): 
    Jarjestetty.clear()
    Sanakirja.clear()
    Heittoja = 0
    for i in Lista:
        Heittoja = montakoHeittoa(Lista, i)
        Sanakirja[i] = Heittoja
    # Nyt lista luettiin sanakirjaan, joka on karsittu niin, jossa (eri syyt, heitot yht)
    Jarjestetty = sorted(Sanakirja.items(), key=lambda Sanakirja:Sanakirja[0])
    return Jarjestetty

def kirjoitaTiedosto(Nimi, Jarjestetty):
    HeitotYht = 0
    for i in Jarjestetty:
        HeitotYht += i[1]
    Tiedosto = open(Nimi, 'w', encoding="utf-8")
    Tiedosto.write("Tunnistettiin {0:d} erilaista syytä ja {1:d} heittoa:\n".format(len(Jarjestetty), HeitotYht))
    for i in Jarjestetty:
        if (i[1] == 1):
            Tiedosto.write("{0:s}: {1:d} heitto\n".format(i[0], i[1]))
        else:
            Tiedosto.write("{0:s}: {1:d} heittoa\n".format(i[0], i[1]))
    Tiedosto.close
    return Jarjestetty

def tulostaTiedosto(Nimi):
    Tiedosto = open(Nimi, 'r', encoding="utf-8")
    Rivi = Tiedosto.readline()
    while (len(Rivi) > 0):
        RiviSiivottu = Rivi[:-1]
        print(RiviSiivottu)
        Rivi = Tiedosto.readline()
    Tiedosto.close()
    return None

def paaohjelma():
    Lista = []
    Sanakirja = {}
    Jarjestetty = []
    LuettavanNimi = input("Anna luettavan tiedoston nimi: ")
    try:
        Lista = lueTiedostoListaan(LuettavanNimi, Lista)
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(LuettavanNimi))
        sys.exit(0)
    try:
        Jarjestetty = analysoi(Lista, Sanakirja, Jarjestetty)
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(LuettavanNimi))
        sys.exit(0)
    KirjoitettavanNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        kirjoitaTiedosto(KirjoitettavanNimi, Jarjestetty)
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(KirjoitettavanNimi))
        sys.exit(0)
    try:
        tulostaTiedosto(KirjoitettavanNimi)
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(KirjoitettavanNimi))
        sys.exit(0)
    print("Kiitos ohjelman käytöstä.")
    Lista.clear()
    Sanakirja.clear()
    Jarjestetty.clear()
    return None

paaohjelma()

