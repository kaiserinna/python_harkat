Nimi = input("Anna nimesi: ")
print("Huomenta " + Nimi + ". Kerro mikä olet.")
Olet = input("Olen: ")
Himokyy = "himokyy"

while (True):
    if (Olet != Himokyy):
        Olet = input("Eeeei, yritäs uudelleen. Olen: ")
    else:
        print("Jep jep <3")
        break
