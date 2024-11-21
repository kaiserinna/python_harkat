OIKEALUKU = 42

def tulostaOhjeet():
    print("Tällä ohjelmalla voit arvata lukua.")
    print("Ohjelma kertoo onko arvauksesi pienempi vai suurempi kuin arvattava luku.\n")
    return None

def kysyLuku():
    Luku = int(input("Anna arvauksesi luvusta: "))
    return Luku

def tarkistaLuku(AnnettuLuku, Kierroksia):
    if (AnnettuLuku == OIKEALUKU):
        Kierroksia = Kierroksia + 1
        print("Arvastit oikein! Onneksi olkoon!")
        print("Arvasit", Kierroksia, "kertaa ennen kuin arvasit oikein.")
        return True
    elif (AnnettuLuku <= OIKEALUKU - 10):
        print("Luku on paljon suurempi. Yritä uudelleen.")
    elif (AnnettuLuku >= OIKEALUKU + 10):
        print("Luku on paljon pienempi. Yritä uudelleen.")
    elif (AnnettuLuku > OIKEALUKU - 10) and (AnnettuLuku < OIKEALUKU + 10):
        print("Olet jo lähellä!. Yritä uudelleen.")
    return False
        
def paaohjelma():
    tulostaOhjeet()
    KysyttyLuku = kysyLuku()
    KierrostenMaara = 0
    while (tarkistaLuku(KysyttyLuku, KierrostenMaara) == False):
        KysyttyLuku = kysyLuku()
        KierrostenMaara = KierrostenMaara + 1
    print("Kiitos ohjelman käytöstä.")
    return None
              
paaohjelma()
