######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä:
# Opiskelijanumero: x112732
# Päivämäärä: 27.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentomateriaali
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T4.py


def paaohjelma():
    
    class RIVILUOKKA:
        Sessio = None
        Hahmo = None
        NoppienMaara = None
        Noppa = None
        NoppienSilmaluvut = None

    TiedostonNimi = input("Anna tiedoston nimi: ")
    print("Nopanheiton tulokset ovat seuraavat:")
    Tiedosto = open(TiedostonNimi, 'r', encoding="utf-8")
    Tiedosto.readline() #ohitetaan eka rivi
    Rivi = Tiedosto.readline()
    while (len(Rivi) > 0):
        Tiedot = Rivi.split(";")
        Hahmo = str(Tiedot[1])
        Noppa = str(Tiedot[3])
        NoppienSilmaluvut = str((Tiedot[4])[:-1])
        Heitot = str(len(NoppienSilmaluvut.split(",")))
        print("Pelaaja '" + Hahmo + "' heitti " + Heitot + " kertaa noppaa " + Noppa + " ja sai silmäluvut '" + NoppienSilmaluvut + "'.")
        Rivi = Tiedosto.readline()
        Tiedot.clear()
    Tiedosto.close()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof
