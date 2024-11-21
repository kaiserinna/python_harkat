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
# Tehtävä L08T5.py

class LUOKKA:
    Koodi = None
    Nimike = None
    Tuonti = None
    Vienti = None

def kysyTiedosto(Kehote):
    Tiedosto = input(Kehote)
    return Tiedosto

def teeOlio(Rivi):
    Tuote = LUOKKA()
    Alkiot = Rivi.split(';')
    Tuote.Koodi = Alkiot[0]
    Tuote.Nimike = Alkiot[1]
    Tuote.Tuonti = Alkiot[2]
    Tuote.Vienti = Alkiot[3]
    return Tuote
   
def teeOliolista(Lista, Tuote):
    Lista.append(Tuote)
    return Lista


#Tässä luetaan tiedosto ja tehdään siitä oliolista
def lueTiedosto(Nimi, Lista):
    Lista.clear()
    Tiedosto = open(Nimi, 'r', encoding="utf-8")
    Tiedosto.readline() #Ekan rivin ohitus
    Rivi = Tiedosto.readline()
    while (len(Rivi) > 0):
        Tuote = teeOlio(Rivi)
        Lista = teeOliolista(Lista, Tuote)
        Rivi = Tiedosto.readline()
    Tiedosto.close()
    print("Tiedosto '" + Nimi + "' luettu.")
    return Lista


def analysoi(Lista, Analyysilista):
   #Lista, jossa jokainen indeksi on olio, jossa kaikki tiedo.
   # kaikissa tieodt koodi, nimi, tuonti, vienti
    #Tehdään uusi lista: Analyysilista = [], jossa 
    # loopissa kaikkien aiemman listan rivien läpikäynti, josta jokaisella rivillä
    Analyysilista.clear()
    KauppataseYht = 0
    for Tuote in Lista:
        Kauppatase = int(Tuote.Vienti) - int(Tuote.Tuonti)
        KauppataseYht = KauppataseYht + Kauppatase
        if (Kauppatase != 0):
            Merkkijono = str(Tuote.Koodi) + ";" + str(Kauppatase)
            Analyysilista.append(Merkkijono)                            
    print("Tiedot analysoitu, kauppataseen arvo on yhteensä " + str(KauppataseYht) + " euroa.")
    return Analyysilista

def kirjoitaTiedosto(Nimi, Lista):
    Tiedosto = open(Nimi, 'w', encoding="utf-8")
    for Rivi in Lista:
        Tiedosto.write(Rivi + "\n")
    Tiedosto.close()
    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None
    





