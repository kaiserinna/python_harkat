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

import time

class TUULILUOKKA:
    Aika = None # time
    Tuuli = None # float

def kysyy(Kehote):
    Nimi = input(Kehote)
    return Nimi

def kysypaiva():
        Pvm = input("Anna analysoitava päivä muodossa'DD.MM.YYY': ")
        Paiva = time.strptime(Pvm, "%d.%m.%Y")
        return Paiva

def teeTuuliOlio(Rivi):
    Alkiot = Rivi.split(";")
    Tiedot = TUULILUOKKA()
    AlkiotNolla = Alkiot[1]
    AlkiotNollaOikea = AlkiotNolla[0:10]
    Tiedot.Aika = time.strptime(AlkiotNollaOikea, "%d.%m.%Y")
    Tiedot.Tuuli = Alkiot[2]
    return Tiedot

def lueTiedostoListaan(Lista, TiedostonNimi):
    Tiedosto = open(TiedostonNimi, 'r', encoding="utf-8")
    try:
        Tiedosto.readline() #ekarivi
        Rivi = Tiedosto.readline()
        RiviSiivottu = Rivi[-1]
        while (RiviSiivottu > 0):
            Tiedot = teeTuuliOlio(RiviSiivottu)
            Lista.append(Tiedot)
    except:
        print("Ei analysoitavia tietoja, lue tiedot ensin.")
    return Lista

def analysoi(Lista, Paiva):
    Lista.clear()
    try:
        TuuliYht = 0
        Alkioita = 0
        for i in Lista:
            if (Paiva == Lista.Aika):
                TuuliYht += Lista.Tuuli
                Alkioita += 1
        Keskiarvo = TuuliYht / Alkioita
        print("Analyysi suoritettu, {0:d} alkiota analysoitu.".format(Alkioita))
        print("Tuulen nopeuden keskiarvo oli {0:d} metriä sekunnissa {1:d}.".format(Keskiarvo, TuuliYht))
    except:
        print("Annettua päivää ei löydy syötetystä datasta.")
    Lista.clear()

#eof