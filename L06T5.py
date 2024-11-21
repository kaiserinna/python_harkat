def tyhjentaaTiedoston(Nimi):
    Tiedosto = open(Nimi, 'w', encoding="utf-8")
    Tiedosto.close()
    return None

def tietojenTallennus(Nimi, Noppa, Heittoja):
    Tiedosto = open(Nimi, 'a', encoding="utf-8")
    Tiedosto.write("Noppaa {} heitettiin {} kertaa.\n".format(Noppa.strip(), Heittoja))
    Tiedosto.close()
    return None

def paaohjelma():
    print("Tämä ohjelma analysoi nopan heittoja.")
    NimiLuettava = input("Anna luettavan tiedoston nimi: ")
    NimiKirjoitettava = input("Anna kirjoitettavan tiedoston nimi: ")
    tyhjentaaTiedoston(NimiKirjoitettava)
    Tiedosto = open(NimiLuettava, 'r', encoding="utf-8")

    Tiedosto = open(NimiLuettava, 'r', encoding="utf-8")
    Tiedosto.readline()
    Rivi = Tiedosto.readline()
    NoppaEdellinen = Rivi[12:15]
    Noppa = None
    UusiHeitto = 0
    HeittojaYht = 0
    KaikkiHeitot = 0
    while (len(Rivi) > 0):
        Noppa = Rivi[12:15]
        UusiHeitto = int(Rivi[10:11])
        KaikkiHeitot = KaikkiHeitot + UusiHeitto
        if (Noppa == NoppaEdellinen):
            HeittojaYht = HeittojaYht + UusiHeitto
        else:
            tietojenTallennus(NimiKirjoitettava, NoppaEdellinen, HeittojaYht)
            NoppaEdellinen = Noppa
            HeittojaYht = UusiHeitto
        Rivi = Tiedosto.readline()
    tietojenTallennus(NimiKirjoitettava, NoppaEdellinen,HeittojaYht)
    Tiedosto.close()
    print("Tiedosto '{}' luettu.".format(NimiLuettava))
    print("Analysoitiin {} nopan heittoa.".format(str(KaikkiHeitot)))
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
