print("Tämä ohjelma laskee tuotteen hinnan keskiarvon neljän kaupan hinnoista.")
Hintayksi = input("Anna hinta ensimmäisessä kaupassa: ")
Hinta1 = float(Hintayksi)
Hintakaksi = input("Anna hinta toisessa kaupassa: ")
Hinta2 = float(Hintakaksi)
Hintakolme = input("Anna hinta kolmannessa kaupassa: ")
Hinta3 = float(Hintakolme)
Hintanelja = input("Anna hinta viimeisessä kaupassa: ")
Hinta4 = float(Hintanelja)

Summa1 = Hinta1 + Hinta2 + Hinta3 + Hinta4
Summa = str(Summa1)

Yhteensa1 = int(4)
Keskiarvo1 = Summa1 / Yhteensa1
Keskiarvo10 = int(Keskiarvo1 * 10)
KeskiarvoOikea = float(Keskiarvo10) / 10
Keskiarvo = str(KeskiarvoOikea)

Kokonaisluku11 = Summa1 // Yhteensa1
Kokonaisluku1 = int(Kokonaisluku11)
Kokonaisluku = str(Kokonaisluku1)

print("\nAntamiesi hintojen summa on " + Summa + ".\nAntamiesi hintojen keskiarvo on " + Keskiarvo + ".\nKeskiarvo on kokonaislukuna " + Kokonaisluku + ".\nKiitos ohjelman käytöstä.")
