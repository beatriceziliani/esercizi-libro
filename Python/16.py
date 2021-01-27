'''Risolvi il problema precedente partendo da due liste che generano un dizionario
con la nazione come chiave e la capitale come valore. Successivamente interroga il dizionario
per visualizzare la capitale di una nazione
'''
def dictionary(Nazioni, Capitali, dizionario={}):
    for i in range(len(Nazioni)):
        dizionario[Nazioni[i]] = Capitali[i]
    return dizionario

def main():
    Nazioni = ["Regno Unito", "Francia", "Germania", "Italia", "Olanda", "Belgio", "Spagna", "Svizzera", "Irlanda", "Austria"]
    Capitali = ["Londra", "Parigi", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Madrid", "Berna", "Dublino", "Vienna"]
    d = dictionary(Nazioni, Capitali)
    while True:
        print("Inserisci il nome di una nazione per conoscere la sua capitale: ")
        naz = input()
        naz = naz.capitalize()
        if naz not in d:
            print("La nazione non è stata trovata. Premere 0 per stoppare il programma o qualsiasi altro comando per reinserire una nazione: ")
            controllo = input()
            if controllo == "0":
                break
        else:
            cap = d.get(naz)
            print("La capitale è:", cap, "Premere 0 per stoppare il programma o qualsiasi altro comando per reinserire una nazione: ")
            controllo2 = input()
            if controllo2 == "0":
                break

main()