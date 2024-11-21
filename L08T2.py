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

import L08T2Kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Muunna eurot Ruotsin kruunuiksi")
    print("2) Muunna eurot Yhdysvaltain dollareiksi")
    print("3) Muunna Yhdysvaltain dollarit euroiksi")
    print("4) Muunna Ruotsin kruunut euroiksi")
    print("5) Muunna Yhdysvaltain dollarit Ruotsin kruunuiksi")
    print("6) Muunna Ruotsin kruunut Yhdysvaltain dollareiksi")
    print("0) Lopeta")
    Valinta1 = int(input("Anna valintasi: "))
    return Valinta1

def paaohjelma():
    print("Käytetään kirjaston versiota " + str(L08T2Kirjasto.VERSIONUMERO))
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            EuroDesim = float(input("Anna rahamäärä: "))
            KruunuDesim = L08T2Kirjasto.eurotKruunuiksi(EuroDesim)
            print(str(EuroDesim) + " euroa on " + str(round(KruunuDesim, 2)) + " Ruotsin kruunua.")
        elif (Valinta == 2):
            EuroDesim = float(input("Anna rahamäärä: "))
            DollariDesim = L08T2Kirjasto.eurotDollareiksi(EuroDesim)
            print(str(EuroDesim) + " euroa on " + str(round(DollariDesim, 2)) + " Yhdysvaltain dollaria.")
        elif (Valinta == 3):
            DollariDesim = float(input("Anna rahamäärä: "))
            EuroDesim = L08T2Kirjasto.dollaritEuroiksi(DollariDesim)
            print(str(DollariDesim) + " Yhdysvaltain dollaria on " + str(round(EuroDesim, 2)) + " euroa.")
        elif (Valinta == 4):
            KruunuDesim = float(input("Anna rahamäärä: "))
            EuroDesim = L08T2Kirjasto.kruunutEuroiksi(KruunuDesim)
            print(str(KruunuDesim) + " Ruotsin kruunua on " + str(round(EuroDesim, 2)) + " euroa.")
        elif (Valinta == 5):
            DollariDesim = float(input("Anna rahamäärä: "))
            KruunuDesim = L08T2Kirjasto.dollaritKruunuiksi(DollariDesim)
            print(str(DollariDesim) + " Yhdysvaltain dollaria on " + str(round(KruunuDesim, 2)) + " Ruotsin kruunua.")
        elif (Valinta == 6):
            KruunuDesim = float(input("Anna rahamäärä: "))
            DollariDesim = L08T2Kirjasto.kruunutDollareiksi(KruunuDesim)
            print(str(KruunuDesim) + " Ruotsin kruunua on " + str(round(DollariDesim, 2)) + " Yhdysvaltain dollaria.")
        elif (Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")


paaohjelma()