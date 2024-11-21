def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna merkkijono")
    print("2) Tulosta merkkijono kasvaen")
    print("3) Tulosta merkkijono pienentyen")
    print("0) Lopeta")
    Valitse = int(input("Anna valintasi: "))
    return Valitse

def kysyMerkkijono():
    Merkkijono = input("Anna merkkijono: ")
    return Merkkijono
    
def tulostaMerkkijonoKasvaen(merkkijono):
    Kasvaa = 1
    for i in range(0, len(merkkijono)):
        print(merkkijono[0: Kasvaa])
        Kasvaa = Kasvaa + 1
    return None
    

def tulostaMerkkijonoPienentyen(merkkijono):
    Miinustus = 0
    for i in range(0, len(merkkijono)):
        print(merkkijono[0: len(merkkijono) - Miinustus])
        Miinustus = Miinustus + 1
    return None

def paaohjelma():
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")
    Teksti = ""
    Valinta = None
    while (True):
        Valinta = valikko()
        if (Valinta == 0):
            print("Lopetetaan.")
            print()
            break
        elif (Valinta == 1):
            Teksti = kysyMerkkijono()
        elif (Valinta == 2):
            tulostaMerkkijonoKasvaen(Teksti)
        elif (Valinta == 3):
            tulostaMerkkijonoPienentyen(Teksti)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()  
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
