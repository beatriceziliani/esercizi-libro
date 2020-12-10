print("Inserisci una parola")
vocabolo1 = input("Scrivi una parola qualsiasi e vedrai se è palindroma:\n")
vocabolo2 = vocabolo1[::-1]
if vocabolo1 == vocabolo2:
    print("Questa parola è palindroma")
else:
    print("Questa parola NON è palindroma")
