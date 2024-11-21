Pohjahinta = 9.00
PerhepizzalisäK = float(9.00 * 1.3)
Lisätäyte = 1.00
Kotiinkuljetus1 = 4.50
Hinta1 = 1.00


print("Tämä ohjelma laskee pizzan hinnan.")
Perhepizza = input("Onko kyseessä perhepizza? (k/e): ")
if (Perhepizza == "k") or (Perhepizza == "K"):
    Hinta1 = PerhepizzalisäK
    print("Pizzan hinta nyt:", str(round(Hinta1, 2)), "euroa.\n")
else:
    Hinta1 = Pohjahinta
    print("Pizzan hinta nyt:", str(round(Hinta1, 2)), "euroa.\n")

Täytteet = float(input("Lisätäytteiden määrä: "))
Hinta1 = float(Hinta1 + Lisätäyte * Täytteet)
print("Pizzan hinta nyt:", str(round(Hinta1, 2)), "euroa.\n")

Kotiinkuljetus = input("Kotiinkuljetus? (k/e): ")
if (Kotiinkuljetus == "k") or (Kotiinkuljetus == "K"):
    Hinta1 = float(Hinta1 + Kotiinkuljetus1)
    print("Pizzan hinta nyt:", str(round(Hinta1, 2)), "euroa.\n")
else:
    print("Pizzan hinta nyt:", str(round(Hinta1, 2)), "euroa.\n")

KantaAsiakas = input("Oletko kanta-asiakas? (k/e): ")
if (KantaAsiakas == "k") or (KantaAsiakas == "K"):
    KantaAsiakasAle = float(Hinta1 * 0.9)
    Hinta1 = KantaAsiakasAle
    print("\nPizzan lopullinen hinta valinnoillasi on", str(round(Hinta1, 2)), "euroa.")
else:
    print("\nPizzan lopullinen hinta valinnoillasi on", str(round(Hinta1, 2)), "euroa.")

print("Kiitos ohjelman käytöstä.")

