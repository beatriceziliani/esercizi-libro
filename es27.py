lista = []
count = True
ng = 0
ripet = 0
somma = 0
while count == True:
    ng += 1
    ripet += 1
    print("Quanti veicoli sono entrati quel giorno", ng,"? ")
    veic = int(input())
    lista.append(veic)

    if ripet == 3:
        q = int(input("se vuoi uscire scrivi 0, se no premi 1 : "))
        ripeti = 0
        if q == 0:
            count = False
        else:
            pass
for i in lista:
    somma += i
print("In", ng,"giorni, sono passati", somma, "veicoli")
