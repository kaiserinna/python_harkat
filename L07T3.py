######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112372
# Päivämäärä: 25.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot,edellisten viikkojen ohjelmointiopas

# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T3.py
# eof

class TULOS():
    Keskiarvo = None
    PieninArvo = None
    SuurinArvo = None

def valikko():
    print("Valitse haluamasi toiminto:\n1) Lue tiedosto\n2) Analysoi\n3) Kirjoita tiedosto\n0) Lopeta")
    Valinta = int(input("Anna valintasi:"))
    return Valinta


def kysyy(Kehote):
    #tarkistus setelin oikeellisuuteen liittyen. Setelin arvon kysymisessä tulee tarkistaa 
    #onko annettu syöte luku, ennen sen muuttamista kokonaisluvuksim esim .isdigit()
    #ei veislä tarkisteta onko annettu arvo oikea seteli. Mikäli käyttäjä ei anna kokonaislukua,
    #kysy käyttäjältä uudestaan niin kauan kunnes käyttäjä antaa hyväksyttävän arvon eli kokonaisluvun
    
    Syote = input(Kehote)p
    if (Syote.isdigit()):

    return Syote


def lueTiedosto(TiedostonNimi):
    #lisää kaikki numerot ja päivämäärät olioihin, siten että yhdellä rivillä 
    # oleva numero ja pvm ovat yhdessä oliossa kumpikin erillisessä jäsenmuuttujassa
    #Lisää kunkin rivin olion listaan, eli tee oliolista.
    # Lukemisen jälkeen lista palautetaan pääohjelmaan. 
    # Huom lista-rakenne tulee tyhjentää clear()funktiolla
    # ENNEN tietojen lukemista SEKÄ ohjelman päättyessä.


    #Oliolista, jossa kaikki(?) teidot 
    #esimerkki 7.7

    Tiedosto = open(TiedostonNimi, 'r', encoding="utf-8")
    Rivi = Tiedosto.readline()
    while (len(Rivi) > 0):
        Lista.append(Rivi[:-1])
        Rivi = Tiedosto.readline()
        Tiedot = Rivi.split(";")
        Pvm = Tiedot[0]
        Luku = Tiedot[1]


    Tiedosto.close()
    print("Tiedosto '" + TiedostonNimi + "' luettu.")
    Oliolista = []
   # Oliolista.append()
    return #Oliolista

def analysoi(Oliolista):
    #Saa parametrina luetut tiedot sisältävän listan ja tulos-olion.
    #käy listan läpi yhden kerran ja etsii samassa tositorakent4eessa pienimmän ja suurimman arvon
    #sekä laskee tarvittavart lukumäärä- ja summatiedot lukujen keskiarvon selvittämistä varten
    #Analyysin tulokset kirjoitetaan parametrina saadun olion jäsenmuuttujiin ja palautetaan pääohjelmaan
    PieninLuku = None
    SuurinLuku = None
    Keskiarvo = None
    
    Tiedosto = open(TiedostoLue, 'r', encoding="utf-8")
    for i in (Tiedosto):
       Rivi = i.strip()
       if Rivi.isdigit():
        Luku = int(i)
        if (PieninLuku == None) or (Luku < PieninLuku):
            PieninLuku = Luku
            print("Löydettiin uusi pienin luku: " + str(Luku))
        if (SuurinLuku == None) or (Luku > SuurinLuku):
            SuurinLuku = Luku
            print("Löydettiin uusi suurin luku: " + str(Luku))

    Summa = 0
    Alkiot = 0
    while (Rivi != ""):
        Setelit = int(Rivi) * 1000
        Summa = Summa + Setelit
        Alkiot = Alkiot + 1
        Rivi = Tiedosto.readline()
    Keskiarvo = Summa / Alkiot
    Tulos = TULOS()
    Tulos.Keskiarvo = Keskiarvo
    Tulos.PieninArvo =
    Tulos.SuurinArvo


    print("Analyysi suoritettu,", Alkiot, "alkiota analysoitu.")
    return Keskiarvo

def kirjoitaTiedosto(KirjoitettavanTiedostonNimi, SetelinArvo, Keskiarvo):
    Tiedosto = open(KirjoitettavanTiedostonNimi, 'w', encoding="utf-8")
    Tiedosto.write("Analysoitiin {} € seteleiden lukumääriä.\n".format(SetelinArvo))
    Tiedosto.write("Keskimäärin seteleitä oli kuukausittain {} kpl.".format(round(Keskiarvo)))
    Tiedosto.close()
    return None

def tulostaTulokset(Olio): #tulos-olio, setelin arvo ja tiedoston nimi
    print(Parametri)
    return None

def paaohjelma():

    Tulos = TULOS()
    Tulos.Keskiarvo
    Tulos.PieninArvo
    Tulos.SuurinArvo 
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
    AnnettuValinta = valikko()

    while (True):
        if (AnnettuValinta == 1):
            MikaSeteli = kysyy(" Anna analysoitavan setelin arvo: ")
            LuettavanTiedostonNimi = input(" Anna luettavan tiedoston nimi: ")
            #Lista = []?
            Oliolista = lueTiedosto(LuettavanTiedostonNimi, Lista)
        elif (AnnettuValinta == 2):
            #Olio = analysoi(Oliolista, Tulosolio)
        elif (AnnettuValinta == 3):
            KirjoitettavanTiedostonNimi = kysyy(" Anna kirjoitettavan tiedoston nimi: ")
            kirjoitaTiedosto(KirjoitettavanTiedostonNimi, MikaSeteli, Keskiarvo)
            tulostaTulokset("Tiedosto '" + KirjoitettavanTiedostonNimi + "' kirjoitettu.")
        elif (AnnettuValinta == 0):
            tulostaTulokset(" Lopetetaan.")
            print()
            break
        else:
            tulostaTulokset(" Tuntematon valinta, yritä uudestaan.")

        print()
        AnnettuValinta = valikko()

    print("Kiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
