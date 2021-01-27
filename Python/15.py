'''Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista
(nazione e relativa capitale si trovano nella medesima posizione delle rispettive liste),
visualizza la capitale di una nazione della quale viene fornito da tastiera il nome,
segnalando con un messaggio di errore il caso in cui la nazione rihiesta non sia compresa nell'elenco
'''

listaNazioni = ["Regno Unito", "Francia", "Germania", "Italia", "Olanda", "Belgio", "Spagna", "Svizzera", "Irlanda", "Austria"]
listaCapitali = ["Londra", "Parigi", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Madrid", "Berna", "Dublino", "Vienna"]
while True:
    nazione = input("Digitare il nome di una nazione per sapere la sua capitale: ")
    nazione = nazione.capitalize()
    if nazione in listaNazioni:
        i = listaNazioni.index(nazione)
        print(listaCapitali[i])
        print("Per stoppare il programma premi stop, per continuare digitare qualsiasi altro comando: ")
        ripetitore = input()
        if ripetitore == "stop":
            break
    else:
        print(nazione, "Non si trova nell'elenco delle nazioni registrate. Per stoppare il programma premi stop, per continuare digitare qualsiasi altro comando: ")
        ripetitore2 = input()
        if ripetitore2 == "stop":
            break