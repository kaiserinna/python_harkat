def kysyNimi(Kehote):
    TiedostonNimi = input(Kehote)
    return TiedostonNimi

def etsiLuku(TiedostoLue):
    PieninLuku = None
    SuurinLuku = None
    Parillisia = 0
    Parittomia = 0
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
        if (Luku % 2 == 0):
            Parillisia = Parillisia + 1
        else:
            Parittomia = Parittomia + 1
    print("Tiedosto '" + TiedostoLue + "' luettu.")
    Tiedosto.close()
    return PieninLuku, SuurinLuku, Parillisia, Parittomia

def kirjoitaTiedosto(KirjoitettavaTiedosto, Pienin, Suurin, Parilliset, Parittomat):
    Tiedosto = open(KirjoitettavaTiedosto, 'w', encoding="utf-8")
    Tiedosto.write("Tiedoston pienin luku oli {}.\n".format(Pienin))
    Tiedosto.write("Tiedoston suurin luku oli {}.\n".format(Suurin))
    Tiedosto.write("Tiedostossa oli {} parillista ja {} paritonta lukua.".format(Parilliset, Parittomat))
    Tiedosto.close()
    print("Tiedosto '" + KirjoitettavaTiedosto + "' kirjoitettu.")
    return None

def paaohjelma():
    LuettavanTiedostonNimi = kysyNimi("Anna luettavan tiedoston nimi: ")
    PieninLuku, SuurinLuku, Parillisia, Parittomia = etsiLuku(LuettavanTiedostonNimi)
    KirjoitettavanTiedostonNimi = kysyNimi("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitaTiedosto(KirjoitettavanTiedostonNimi, PieninLuku, SuurinLuku, Parillisia, Parittomia)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
