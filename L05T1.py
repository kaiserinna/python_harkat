def tulostaOhjeet():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.")
    print("Anna ensin kaksi lukua.")
    return None

def kysyLuku(Kehote):
    print("Tämä aliohjelma kysyy luvun.")
    Luku = int(input(Kehote))
    return Luku

def tulostaTulokset(Luku1, Luku2):
    print("Tämä aliohjelma tulostaa luvut ja niiden parillisuuden.")
    if (Luku1 % 2 == 0):
        print(Luku1, "on parillinen luku.")
    else:
        print(Luku1, "ei ole parillinen luku.")

    if (Luku2 % 2 == 0):
        print(Luku2, "on parillinen luku.")
    else:
        print(Luku2, "ei ole parillinen luku.")
    return None

def paaohjelma():
    tulostaOhjeet()
    Luku1 = kysyLuku("Anna ensimmäinen luku: ")
    Luku2 = kysyLuku("Anna toinen luku: ")
    tulostaTulokset(Luku1, Luku2)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    
