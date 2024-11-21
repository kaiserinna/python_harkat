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
# Harjoitustehtävä Perustaso

import time
import sys

VIIKONPAIVAT = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]

class SADEMAARALUOKKA:
    Aika = None # time
    Sademaara = None # float
    Kategoria = None # int 1-4
    Paivia = None # int
    Viikonpaiva = None # int


def kysyTiedosto(Kehote):
    Tiedosto = input(Kehote)
    return Tiedosto

def teeSademaaraolio(Aika, Sademaara):
    Tiedot = SADEMAARALUOKKA()
    Tiedot.Aika = Aika
    Tiedot.Sademaara = Sademaara
    return Tiedot

# Tässä aliohjelmassa tehdään tiedostosta sademäärälista, 
# jossa on tiedot on olioina: Tiedot.Aika ja Tiedot.Sademaara, 
def lueTiedosto(Nimi, Sademaaralista):
    Sademaaralista.clear()
    try:
        Tiedosto = open(Nimi, 'r', encoding="utf-8")
        Tiedosto.readline() #Ekan rivin ohitus
        Rivi = Tiedosto.readline()
        while (len(Rivi) > 0):
            Rivi = Rivi[:-1]
            Alkiot = Rivi.split(";")
            AlkioNolla = Alkiot[0]
            AlkioNollaOikea = AlkioNolla[0:10]
            Aika = time.strptime(AlkioNollaOikea, "%Y.%m.%d")
            Sademaara = float(Alkiot[2])
            Tiedot = teeSademaaraolio(Aika, Sademaara)
            Sademaaralista.append(Tiedot)
            Rivi = Tiedosto.readline()
        Tiedosto.close()
        print("Tiedosto '" + Nimi + "' luettu.")
    except OSError:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return Sademaaralista

def teeListaPvSadeYht(Sademaaralista, PaivSademaaratLista):
    # Ensin tehdään lista, jossa yhdistetty päivät ja jokaisen päivän
    # yhteen kerrytetty sademäärä.
    PaivSademaaratLista.clear()
    EdellinenPaiva = None
    SademaaraYht = 0.0
    for Tiedot in Sademaaralista: # Luetaan lista rivi kerrallaan
        Paiva = Tiedot.Aika
        Sademaara = Tiedot.Sademaara
        if ((Paiva == EdellinenPaiva) or (EdellinenPaiva == None)):
            SademaaraYht += Sademaara
        else:
            Lisays = teeSademaaraolio(EdellinenPaiva, SademaaraYht)
            PaivSademaaratLista.append(Lisays)
            SademaaraYht = Sademaara
        EdellinenPaiva = Paiva
    Lisays = teeSademaaraolio(EdellinenPaiva, SademaaraYht)
    PaivSademaaratLista.append(Lisays)
    return PaivSademaaratLista

def lisaaKategoria(PaivSademaaratLista):
    for Tiedot in PaivSademaaratLista:
        if (Tiedot.Sademaara >= 4.5):
            Tiedot.Kategoria = 1
        elif (Tiedot.Sademaara >= 1.0):
            Tiedot.Kategoria = 2
        elif (Tiedot.Sademaara >= 0.3):
            Tiedot.Kategoria = 3
        else:
            Tiedot.Kategoria = 4
    return PaivSademaaratLista # Sama lista

#Päivittäiset sademäärät
def analysoi(SademaaralistaTiedostosta, KategoriaLista, Nimi):
    KategoriaLista.clear()
    PaivSademaaratLista = []
    # Ensin tehdään oliolista, johon yhdistellään sademäärät yhden päivän alle
    try:
        PaivSademaaratLista = teeListaPvSadeYht(SademaaralistaTiedostosta, PaivSademaaratLista)
            # Nyt mulla on oliolista, jossa on päivä;sademaaraYHT
            # 2016.01.01;0.0
            # 2016.01.04;0.6
            # 2016.01.18;1.6
            # 2016.01.20;1.9
    except Exception:
        print("Tiedoston" + str(Nimi) + "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    try:
        KategoriaLista = lisaaKategoria(PaivSademaaratLista)
            # Nyt lisättiin edelliseen listaan kategoriat näin:
            # 2016.01.01;0.0;4
            # 2016.01.04;0.6;3
            # 2016.01.18;1.6;2
            # 2016.01.20;1.9;2
    except Exception:
        print("Tiedoston" + str(Nimi) + "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    # Listassa on yksi olio yhdelle päivälle, eli päiviä on yhtä monta kuin olioita. Lasketaan oliot:
    print("Päivittäiset summat laskettu " + str(len(KategoriaLista)) + " päivälle.")
    print("Päivät kategorisoitu 4 kategoriaan.")
    return KategoriaLista

def montakopaivaa(KategoriaLista, KategoriaNro):
    Paivia = 0
    for i in (KategoriaLista):
        if (i.Kategoria == KategoriaNro):
            Paivia += 1
    return Paivia

def kirjoitaTiedosto(Nimi, KategoriaLista):
    try:
        Tiedosto = open(Nimi, 'w', encoding="utf-8")
        Tiedosto.write("Kategoria;Päivien lukumäärä:\n")
        for KategoriaNro in range(1,5):
            Paivia = montakopaivaa(KategoriaLista, KategoriaNro)
            Tiedosto.write("Kategoria " + str(KategoriaNro) + ";" + str(Paivia) + "\n")
            # Tiedostossa, ei listassa
            # 1;0
            # 2;2
            # 3;1
            # 4;1
        Tiedosto.write("\nKaikki päivittäiset sademäärät:\nPvm;mm\n")
    except OSError:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    try:
        for i in KategoriaLista:
            Tiedosto.write(str(time.strftime("%d.%m.%Y", i.Aika)) + ";" + str(round(i.Sademaara,1)) + "\n")
        print("Tiedosto '" + Nimi + "' kirjoitettu.")
        Tiedosto.close()
    except OSError:
        print("Tiedosto '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def laskeSadePerPaiva(KategoriaLista, ViikonpaivaNro):
    Sadetta = 0.0
    for i in (KategoriaLista):
        if (i.Viikonpaiva == ViikonpaivaNro):
            Sadetta += i.Sademaara
    return Sadetta
     
def teeTiedostoViikonpaivista(Nimi, KategoriaLista):
    # Ensin muokataan listaan vielä viikonpäivät:
    for i in KategoriaLista:
        i.Viikonpaiva = i.Aika.tm_wday
        # i.Aika;i.Sademaara;i.Kategoria;i.Viikonpaiva# näin:
            # 2016.01.01;0.0;4;0
            # 2016.01.04;0.6;3;2
            # 2016.01.18;1.6;2;2
            # 2016.01.20;1.9;2;6
    try:
        Tiedosto = open(Nimi, 'w', encoding="utf-8")
        Tiedosto.write("Viikonpäivä;Sadekertymä\n")
        for ViikonpaivaNro in range(0,7):
            SadettaPerPaiva = laskeSadePerPaiva(KategoriaLista, ViikonpaivaNro)
            Tiedosto.write(VIIKONPAIVAT[ViikonpaivaNro] + ";" + str(round(SadettaPerPaiva, 1)) + "\n")
        Tiedosto.close()
    except OSError:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None
#eof