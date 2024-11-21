######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112372
# Päivämäärä:23.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Video luennosta ja ohjelmointivideot
# python Help > .isnumeric
# python tutorial visual run
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T1.py
# eof

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lisää tehtävä listaan")
    print("2) Poista tehtävä listalta")
    print("3) Tulosta tehtävälista")
    print("0) Lopeta")
    Valinta = input("Valintasi: ")
    return Valinta

def lisaaTehtavan(Lista, Lisays):
    Lista.append(Lisays)
    
    return Lista

def poistaaTehtavan(Lista, Nro):
    
    if (Nro.isnumeric()):        
        if ((int(Nro) >= 1) and (int(Nro) <= len(Lista))):
            Indeksi = int(Nro) - 1
            del Lista[Indeksi]
        else:
            print("Listalta ei löydy tietoja järjestysnumerolla " + str(Nro) + ".")
            print("Järjestysnumerot ovat väliltä 1-" + str(len(Lista)) + ".")
    else:
        print("Tuntematon valinta.")
        
    return Lista

def tulostaaTehtavan(Lista):
    Kierros = 1
    for i in (Lista):
        print(str(Kierros) + ". " + str(i))
        Kierros += 1
    return None

def paaohjelma():
    Tehtavalista = []
    Valinta = valikko()
    Uusitehtava = None
    PoistettavanNro = None
    while (True):            
        if (Valinta == "1"):
            Uusitehtava = input("Anna lisättävä tehtävä: ")
            Tehtavalista = lisaaTehtavan(Tehtavalista, Uusitehtava)
        elif (Valinta == "2"):
            print("Tehtävälistassasi on " + str(len(Tehtavalista)) + " tehtävää.")
            PoistettavanNro = input("Anna poistettavan tehtävän järjestysnumero: ")
            Tehtavalista = poistaaTehtavan(Tehtavalista, PoistettavanNro)            
        elif (Valinta == "3"):
            print("Tehtävälistassasi on seuraavat tehtävät:")
            tulostaaTehtavan(Tehtavalista)
        elif (Valinta == "0"):
            if (len(Tehtavalista) == 0):
                print("Lopetetaan.")
            else:
                print("Sinulta jäi tekemättä seuraavat tehtävät:")
                tulostaaTehtavan(Tehtavalista)
                print("Lopetetaan.")
            break        
        else:
            print("Tuntematon valinta.")
            
        print()
        Valinta = valikko()
    Tehtavalista.clear()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

    
