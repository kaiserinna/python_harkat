# (c) LUT 2023 L11T4 Variaatio B - Rami Saarivuori
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
##########################################################################################
# Ohjelma, joka etsii sopivia numeroita

import time
import sys
import math

def hakufunktio(Nimi, Luvut):
    #####################################################
    # Lisää tarvittava koodi tämän kommentin alapuolelle.



    # Lisää tarvittava koodi tämän kommentin yläpuolelle.
    #####################################################
    return Luvut

def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = []
    Kello1 = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    if not Tulokset:
        print("Hakualgoritmi ei löytänyt sopivia lukuja.")
    elif (Aika > 3):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi {} lukua:".format(len(Tulokset)))
        for i in Tulokset:
            print(i, end=", ")
        print()
    print("Kiitos ohjelman käytöstä.")
    Tulokset.clear()
    return None

paaohjelma()
###########################################################################
# eof
