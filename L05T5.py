# Tämä aliohjelma laskee Collatz-jakson parametrina annetulle luvulle käyttäen yllä olevaa kaavaa 
# ja palauttaa sen pituuden.
def laskeJakso(LaskettavaLuku):
    Termi = 0
    while (LaskettavaLuku != 1):
        if (LaskettavaLuku % 2 == 0):
            LaskettavaLuku = LaskettavaLuku / 2
            Termi = Termi + 1
        elif (LaskettavaLuku % 2 == 1):
            LaskettavaLuku = 3 * LaskettavaLuku +1
            Termi = Termi + 1
    Termi = Termi + 1
    return Termi

# Tämä aliohjelma pyytää käyttäjältä luvun parametrina annetun
# kehotteen mukaisesti.
def kysyLuku(Kehote):
    Syote = int(input(Kehote))
    return Syote

#Tämä aliohjelma saa parametrina käyttäjän antamat luvut ja sisältää
#toistorakenteen, joka käy luvut läpi. Jokaisella kierroksella kutsutaan laskeJakso-aliohjelmaa.
#Mikäli jakson pituus ylittää tähän mennessä saadun pisimmän, tallennetaan jakson pituus ja
#sen alkuluku muuttujiin. Lopuksi aliohjelma tulostaa pisimmän jakson ja jakson alkuluvun.
def etsiPisin(Alku, Loppu):
    Pisin = 0
    Jakso = 0
    for i in range(Alku, Loppu + 1):
        Pituus = laskeJakso(i)
        if (Pituus > Pisin):
            Pisin = Pituus
            Jakso = i
    print("Suurin Collatz-jakso oli luvulla " + str(Jakso) + ".")
    print("Jakson pituus oli", Pisin, "termiä.")
    return None

# Pääohjelma kutsuu kahdesti lukua kysyvää aliohjelmaa ja välittää luvut pisimmän
# jakson etsivälle aliohjelmalle.
def paaohjelma():
    print("Tämä ohjelma etsii pisimmän Collatz-jakson annetulla välillä.")
    Luku1 = kysyLuku("Anna lukualueen alku: ")
    Luku2 = kysyLuku("Anna lukualueen loppu: ")
    etsiPisin(Luku1, Luku2)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
