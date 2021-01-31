'''Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista
(nazione e relativa capitale si trovano nella medesima posizione delle rispettive liste),
visualizza la capitale di una nazione della quale viene fornito da tastiera il nome,
segnalando con un messaggio di errore il caso in cui la nazione rihiesta non sia compresa nell'elenco
'''
def trovaCapitale(nat, lN, lC):
    if nat in lN:
        pos = lN.index(nat)
        print(lC[pos])
    else:
        print("nazione non presente")
        
        
        
listaNazioni = ["Regno Unito", "Francia", "Germania", "Italia", "Olanda", "Belgio", "Spagna", "Svizzera", "Irlanda", "Austria"]
listaCapitali = ["Londra", "Parigi", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Madrid", "Berna", "Dublino", "Vienna"]


nat = input("Dimmi nazione").capitalize()
trovaCapitale(nat, listaNazioni, listaCapitali)
