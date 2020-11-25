lista = []
count = True
pers = 0
ripet = 0
somma = 0
while count == True:
    pers += 1
    ripet += 1
    print("Quanto è lo stipendio della persona", pers,"? ")
    stipendi = int(input())
    lista.append(stipendi)

    if ripet == 3:
        q = int(input("per uscire digita -1, altrimenti premi 0 : "))
        ripet = 0
        if q == -1:
            count = False
        else:
            pass
for i in lista:
    somma += i
l = len(lista)
print(lista)
mediastip = somma/l
print(mediastip)
