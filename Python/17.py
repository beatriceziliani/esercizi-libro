''' Costruisci un dizionario ottenuto da quello dell'es precedente invertendo il ruolo di chiave e la capitale come valore. Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale.
'''

def crea_dizionario(nazioni, capitali):
    dizionario = {}
    for i in range(len(nazioni)):
        dizionario[capitali[i]] = nazioni[i]
    return dizionario
    
nazioni = ["Regno Unito", "Francia", "Germania", "Italia", "Olanda", "Belgio", "Spagna", "Svizzera", "Irlanda", "Austria"]
capitali = ["Londra", "Parigi", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Madrid", "Berna", "Dublino", "Vienna"]

dizionario = crea_dizionario(nazioni, capitali)

while True:
    capitale = input("Scrivi una capitale per sapere la sua nazione. ").capitalize()
    nazione = dizionario[capitale]
    print(nazione)