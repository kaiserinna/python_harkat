def valikko():
    print("Valitse haluamasi toiminto:\n1) Kysy setelin arvo\n2) Lue ja analysoi\n3) Kirjoita tiedosto\n0) Lopeta")
    Valinta = int(input("Anna valintasi:"))
    return Valinta

def kysyTiedosto(Kehote):
    Syote = input(Kehote)
    return Syote

def kysySeteli(Kehote):
    Syote = int(input(Kehote))
    return Syote

def analysoi(TiedostonNimi):
    Summa = 0
    Alkiot = 0
    Tiedosto = open(TiedostonNimi, 'r', encoding="utf-8")
    Rivi = Tiedosto.readline()
    while (Rivi != ""):
        Setelit = int(Rivi) * 1000
        Summa = Summa + Setelit
        Alkiot = Alkiot + 1
        Rivi = Tiedosto.readline()
    Keskiarvo = Summa / Alkiot
    print("Tiedosto '" + TiedostonNimi + "' luettu.")
    print("Analyysi suoritettu,", Alkiot, "alkiota analysoitu.")
    Tiedosto.close()
    return Keskiarvo

def kirjoitaTiedosto(KirjoitettavanTiedostonNimi, SetelinArvo, Keskiarvo):
    Tiedosto = open(KirjoitettavanTiedostonNimi, 'w', encoding="utf-8")
    Tiedosto.write("Analysoitiin {} € seteleiden lukumääriä.\n".format(SetelinArvo))
    Tiedosto.write("Keskimäärin seteleitä oli kuukausittain {} kpl.".format(round(Keskiarvo)))
    Tiedosto.close()
    return None

def tulostaTulokset(Parametri):
    print(Parametri)
    return None

def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
    AnnettuValinta = valikko()

    while (True):
        if (AnnettuValinta == 1):
            MikaSeteli = kysySeteli(" Anna analysoitavan setelin arvo: ")
        elif (AnnettuValinta == 2):
            LuettavanTiedostonNimi = kysyTiedosto(" Anna luettavan tiedoston nimi: ")
            Keskiarvo = analysoi(LuettavanTiedostonNimi)
        elif (AnnettuValinta == 3):
            KirjoitettavanTiedostonNimi = kysyTiedosto(" Anna kirjoitettavan tiedoston nimi: ")
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
