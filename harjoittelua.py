#kommentti
HINTA = 12

def kysyRyhmakoko():
    Ryhmakoko = int(input("Anna ryhmän koko väliltä 1-10 henkilöä (0 lopettaa): "))
    return Ryhmakoko

def laskeeTuoton(Ryhmakoko):
    Tuotto = HINTA * Ryhmakoko
    return Tuotto

def laskeeKeskiarvon(Ryhmakoko, Montakoryhmaa):
    KeskiarvoTarkka = Ryhmakoko / Montakoryhmaa
    Keskiarvo = round(KeskiarvoTarkka, 0)
    return Keskiarvo

def paaohjelma():
    TuottoYHT = 0
    RyhmakokoYHT = 0
    MontakoRyhmaa = 0
    while(True):
        Ryhmakoko = kysyRyhmakoko()
        if ((Ryhmakoko > 0) and (Ryhmakoko < 10)):
            RyhmakokoYHT += Ryhmakoko
            MontakoRyhmaa += 1
        elif (Ryhmakoko == 0):
            break
        else:
            print("Syöte ei ole annetulla välillä, yritä uudestaan.")
    Tuotto = laskeeTuoton(RyhmakokoYHT)
    Keskiarvo = int(laskeeKeskiarvon(RyhmakokoYHT, MontakoRyhmaa))
    print("Päivän tuotto oli {0:d} euroa.".format(Tuotto))
    print("Ryhmän keskimääräinen koko oli {0:d} henkilöä.".format(Keskiarvo))
    return None

paaohjelma()

#eof
