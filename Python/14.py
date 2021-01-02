'''Crea un programma che scriva la differenza di due numeri a e b se il loro prodotto è maggiore di 10,
oppure la loro somma se il prodotto è minore o uguale a 10. 
Esegui poi il programma con diverse coppie di valori per a e b:
(-5, 2); (5, -5); (10, 2); (-4, -5); (5, 4); (-3, -2)'''

Alista = [-5, 5, 10, -4, 5, -3]
Blista = [2, -5, 2, -5, 4, -2]
for i in range(len(Alista)):
    if Alista[i]*Blista[i] > 10:
        print("Il prodotto della coppia", [i+1], "è maggiore di 10. Quindi la differenza della coppia", [i+1],"è: ", Alista[i]-Blista[i])
    elif Alista[i]*Blista[i] <= 10:
        print("Il prodotto della coppia", [i+1], "è minore di 10. Quindi la somma della coppia", [i+1],"è: ", Alista[i]+Blista[i])
