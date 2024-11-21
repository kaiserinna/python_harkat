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
# Tehtävä L08T1.py

import math
import time

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Laske kertoma")
    print("2) Laske suurin yhteinen tekijä")
    print("3) Laske sini ja kosini")
    print("4) Muunna aika")
    print("5) Tulosta pii")
    print("0) Lopeta")
    Valinta1 = int(input("Anna valintasi: "))
    return Valinta1

def laskeKertoma(Luku):
    Kertoma1 = math.factorial(Luku)
    return Kertoma1

def laskeSuurinYhteinen(Parametri1, Parametri2, Parametri3):
    SuurinYhteinenTekija = math.gcd(Parametri1, Parametri2, Parametri3)
    return SuurinYhteinenTekija

def laskeSini(SinLuku): 
    Sini = math.sin(SinLuku)
    return Sini

def laskeKosini(CosLuku):
    Cosini = math.cos(CosLuku)
    return Cosini

def muunnaAika(AikaInput):
    AnnettuAikaVert = time.strptime(AikaInput, "%d.%m.%Y %H:%M")
    AnnettuAikaMuunnettu = time.strftime("%Y.%m.%d", AnnettuAikaVert)
    print("Antamasi päivämäärä vuosi ensin: " + AnnettuAikaMuunnettu)
    AattoSTR = "24.12.2030 17:00"
    AattoVert = time.strptime(AattoSTR,"%d.%m.%Y %H:%M")
    if (AnnettuAikaVert > AattoVert):
        print("Antamasi aika on jouluaaton 2030 klo 17 jälkeen.")
    else:
        print("Antamasi aika on ennen jouluaattoa 2030 klo 17.")
    return None

def tulostaPii():
    print("Pythonin math-kirjastosta saatu piin arvo: " + str(math.pi))
    return None

def paaohjelma():
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            Luku = int(input("Anna kokonaisluku: "))            
            Kertoma = laskeKertoma(Luku)
            print("Luvun " + str(Luku) + " kertoma on " + str(Kertoma) + ".")
        elif (Valinta == 2):
            Luku1 = int(input("Anna 1. kokonaisluku: "))
            Luku2 = int(input("Anna 2. kokonaisluku: "))
            Luku3 = int(input("Anna 3. kokonaisluku: "))
            SuurinYhteinen = laskeSuurinYhteinen(Luku1, Luku2, Luku3)
            print("Lukujen " + str(Luku1) + ", " + str(Luku2) + " ja " + str(Luku3) + " suurin yhteinen tekijä on " + str(SuurinYhteinen) + ".")
        elif (Valinta == 3):
            Desimaaliluku = float(input("Anna desimaaliluku: "))
            Sini = laskeSini(Desimaaliluku)
            Kosini = laskeKosini(Desimaaliluku)
            print("Luvun " + str(Desimaaliluku) + " sini on " + str(round(Sini, 5)) + " ja kosini " + str(round(Kosini, 5)) + ".")
        elif (Valinta == 4):
            Aika = input("Anna aika muodossa 'DD.MM.YYYY hh:mm': ")
            muunnaAika(Aika)
        elif (Valinta == 5):
            tulostaPii()
        elif (Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof