print("Inserisci tutte le parole polindrome")
stri = input("Scrivi una parola qualsiasi e vedrai se è polindroma:\n")
stri2 = stri[::-1]
if stri == stri2:
    print("Questa parola è polindroma")
else:
    print("Questa parola NON è polindroma")
