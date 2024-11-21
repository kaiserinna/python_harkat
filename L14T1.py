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
# L14T1.py

def valikko():
    print("Valitse auton käyttövoima:")
    print("1) Bensiini\n2) Sähkö\n3) Maa- tai biokaasu\n0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def kysyMatka():
    Matka = float(input("Anna matkan pituus kilometreinä: "))
    return Matka

def kysyKeskikulutus(Yksikkö):
    Keskikulutus = float(input("Anna keskimääräinen kulutus ({0:s} per 100 km): ".format(Yksikkö)))
    return Keskikulutus

def AnnaHinta(Valinta, Yksikkö):
    Hinta = float(input("Anna {0:s} hinta euroina per {1:s}: ".format(Valinta, Yksikkö)))
    return Hinta

def laske(Matka, Keskikulutus, Hinta):
    Tulos = Matka/100 * Keskikulutus * Hinta
    print("{0:.1f} kilometrin matkan hinnaksi muodostuisi noin {1:.2f} euroa.".format(Matka,Tulos))
    return None

def paaohjelma():
    print("Tämä ohjelma laskee auton matkakustannuksia eri käyttövoimilla.")
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            Käyttövoima = "bensan"
            Yksikkö = "litra"
            Matka = kysyMatka()
            Keskikulutus = kysyKeskikulutus(Yksikkö)
            Hinta = AnnaHinta(Käyttövoima, Yksikkö)
            laske(Matka, Keskikulutus, Hinta)
        elif (Valinta == 2):
            Käyttövoima = "sähkön"
            Yksikkö = "kWh"
            Matka = kysyMatka()
            Keskikulutus = kysyKeskikulutus(Yksikkö)
            Hinta = AnnaHinta(Käyttövoima, Yksikkö)
            laske(Matka, Keskikulutus, Hinta)
        elif (Valinta == 3):
            Käyttövoima = "kaasun"
            Yksikkö = "kg"
            Matka = kysyMatka()
            Keskikulutus = kysyKeskikulutus(Yksikkö)
            Hinta = AnnaHinta(Käyttövoima, Yksikkö)
            laske(Matka, Keskikulutus, Hinta)
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