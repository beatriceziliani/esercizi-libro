print("Inserisci la lunghezza delle parole")
N = int(input("Inserisci il numero delle parole da scrivere: "))
A = []
B = []
n = 1
while True:
    p = input("sInserisci parola: ")
    A.append(p)
    B.append(len(p))
    if N == n:
        print("Questo è il numero di lettere: ",B)
        break
    n = n + 1
