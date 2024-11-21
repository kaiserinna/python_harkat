######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kaisa Punakorpi
# Opiskelijanumero:x112372
# Päivämäärä: 25.10.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Luentovideot ja ohjelmointivideot

# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T2.py
# eof


class ELOKUVA():
    Nimi = None
    Pituus = None
    Ohjaaja = None


def sijoitus(O):
    O.Nimi = input("Anna elokuvan nimi: ")
    O.Pituus = input("Anna elokuvan pituus kokonaisina minuutteina: ")
    O.Ohjaaja = input("Anna elokuvan ohjaaja: ")
    return O

def tulostaa(OT):
    print("Elokuvan '" + OT.Nimi + "' on ohjannut " + OT.Ohjaaja + " ja sen kesto on " + OT.Pituus + " minuuttia.")
    return None

def paaohjelma():
    Olio = ELOKUVA()
    Oliovalmis = sijoitus(Olio)
    tulostaa(Oliovalmis)
    print("Kiitos ohjelman käytöstä.")
   
    return None

paaohjelma()
