print("Anna kaksi kokonaislukua.")
Luku1 = int(input("Anna luku 1: "))
Lukuyksi = str(Luku1)
Luku2 = int(input("Anna luku 2: "))
Lukukaksi = str(Luku2)

print("Selvitetään, ovatko antamasi luvut parillisia.")
if Luku1 % 2 == 0:
    print("Luku", Lukuyksi, "on parillinen.")
else:
    print("Luku", Lukuyksi, "on pariton.")

if Luku2 % 2 == 0:
    print("Luku", Lukukaksi, "on parillinen.")
else:
    print("Luku", Lukukaksi, "on pariton.")

print("Selvitetään, kumpi antamistasi luvuista on suurempi.")
if Luku1 > Luku2:
    print("Luku", Lukuyksi, "on suurempi.")
elif Luku1 == Luku2:
    print("Luvut", Lukuyksi, "ja", Lukukaksi, "ovat yhtä suuria.")
else:
    print("Luku", Lukukaksi, "on suurempi.")

print("Kiitos ohjelman käytöstä.")
