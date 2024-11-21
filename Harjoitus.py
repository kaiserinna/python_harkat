Teksti = input("Anna merkkijono: ")
#for i in range(len(Teksti)):
#       print(Teksti)
#       Pienenee = len(Teksti) -1
# = range(0, len(Teksti) - Pienenee)
Miinustus = 0
for i in range(len(Teksti)):
    print(Teksti[0:len(Teksti) - Miinustus])
    Miinustus = Miinustus + 1

for i in range(len(Teksti), 0, -1):
    print(i)

