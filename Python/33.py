''' In un laboratorio di analisi i pazienti sono sottoposti
a un esame specialistico secondo l'ordine di arrivo: scrivi
 il programma che consenta di registrare i nomi dei pazienti 
 man mano che arrivano. Visualizza poi il nome del paziente 
 che deve essere sottoposto all'esame perchè il primo della 
 coda in attesa.'''
exit = False
l_pazienti = []
while not exit:
    paziente = input("Inserisci il nome di un paziente.  ")
    if paziente != "quit":
        l_pazienti.append(paziente)
        
    else:
        exit = True

print(l_pazienti[0])