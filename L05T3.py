def valikko():
    print("Valitse haluamasi toiminto:\n1) Kysy setelin arvo\n2) Kysy setelien lukumäärä\n3) Laske kokonaisarvo\n4) Tulosta tulos\n0) Lopeta")
    Valinta = int(input("Anna valintasi:"))
    return Valinta

def kysyLuku(Kehote):
    Syote = int(input(Kehote))
    return Syote

def analysoi(Ekasta, Tokasta):
    Tulo = int(Ekasta * Tokasta)
    return Tulo

def tulostaTulokset(Parametri):
    print(Parametri)
    return None


def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
    AnnettuValinta = valikko()

    while (True):
        if (AnnettuValinta == 1):
            SetelinArvo = kysyLuku(" Anna analysoitavan setelin arvo: ")
            print()
        elif (AnnettuValinta == 2):
            Lukumaara = kysyLuku(" Anna setelien lukumäärä: ")
            print()
        elif (AnnettuValinta == 3):
            tulostaTulokset(" Setelien kokonaisarvo laskettu.")
            print()
        elif (AnnettuValinta == 4):
            TuloLaskettu = analysoi(SetelinArvo, Lukumaara)
            print(" Setelien kokonaisarvo on", TuloLaskettu, "euroa.")
            print()
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
