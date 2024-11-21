######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero: x112732
# Päivämäärä: 27.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Kurssin videot
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T5.py


class TUOTTEET:
    Nimi = str()
    Hinta = float()


# Tässä tehdään olio käyttäjän antamista tuotetiedoista
# lisätään ne listaan ja palautetaan kutsuvaan ohjelmaan listan
#
def lisaaTuote(Lista):
    Tuote = TUOTTEET()
    Tuote.Nimi = input("Anna tuotteen nimi: ")
    Tuote.Hinta = input("Anna tuotteen hinta (e): ")
    Lista.append(Tuote)
    return Lista


# Tässä muutetaan tiedoston rivi TUOOTTEET olioksi
# privissä alkioiden erottajana puoiipiste ja lopussa rivinvaihto
# palauttaa olion
#
def teeTuoteOlioRivista(Rivi):
    Rivi = Rivi[:-1]
    Alkiot = Rivi.split(';')
    Tuote = TUOTTEET()
    Tuote.Nimi = Alkiot[0]
    Tuote.Hinta = Alkiot[1]
    return Tuote


# tässä tehdään lista, joka koostuu olioista, jotka tehdään tiedoston teidoista. 
# Tiedoston eka rivi ohitetaan, jokaisella rivillä rivivaihto lopussa pitää poistaa
#
def lueTiedosto(Nimi, Lista):
    #Lista.clear()
    Tiedosto = open(Nimi, 'r', encoding="utf-8")
    Tiedosto.readline() #ohita rivi
    Rivi = Tiedosto.readline()
    while(len(Rivi) > 0):
        Tuotetiedot = teeTuoteOlioRivista(Rivi)
        Lista.append(Tuotetiedot)
        Rivi = Tiedosto.readline()
    print("Tiedosto", Nimi, "luettu.")
    Tiedosto.close()
    return Lista

# tässä tulostetaan lista niin, että sen 
# oliot jäsenmuuttujineen tulee yksi yhdelle riville
#2
def tulostaTiedot(Lista):
    print("Listalta löytyy seuraavat tuotteet ja hinnat:")
    for Tuote in Lista:
        print(Tuote.Nimi, Tuote.Hinta)
    return None


# Tässä kirjoitetaan teidosto, jolla käyttäjän antama nimi
# Tiedostoon tallennetaan aiemmin luotu lista
# Tiedoston muoto on samanlainen kuin tiedosto, josta tiedot saatiin2
# eli alkioiden erotin on ;
# 
def tallennaTiedostoon(Nimi, Lista):
    Tiedosto = open(Nimi, 'w', encoding="utf-8")
    Tiedosto.write("Tuotteen nimi;Tuotteen hinta\n")
    for Tuote in Lista:
        Tiedosto.write(Tuote.Nimi + ";" + Tuote.Hinta + "\n")
    print("Tiedot kirjoitettu tiedostoon '" + Nimi + "'.")
    return None 


#Tässä tulostetaan ohjelman valikko
# 
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna uuden tuotteen tiedot")
    print("2) Lue tiedot tiedostosta")
    print("3) Tulosta tiedot listalta")
    print("4) Tallenna listan tiedot tiedostoon")
    print("0) Lopeta")
    Valinta1 = int(input("Anna valintasi: "))
    return Valinta1


# Pääohjelmassa looppi valikkovalinnoille ja niiden toiminnoille
#
def paaohjelma():
    print("Tämä ohjelma hallitsee tuotteiden tietoja listalla.")
    Valinta = None
    Tuotelista = []
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            Tuotelista = lisaaTuote(Tuotelista)
        elif (Valinta == 2):
            TiedostonNimi = input("Anna luettavan tiedoston nimi: ")
            Tuotelista = lueTiedosto(TiedostonNimi, Tuotelista)
        elif (Valinta == 3):
            tulostaTiedot(Tuotelista)
        elif (Valinta == 4):
            TiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")
            tallennaTiedostoon(TiedostonNimi, Tuotelista)
        elif (Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    Tuotelista.clear()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof
