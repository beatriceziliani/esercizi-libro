'''Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è 0)'''

Ninserito = int(input("Inserisci un numero intero per sapere se è pari o dispari. Il numero è: "))
if Ninserito%2 == 0:
    print("Il numero inserito, (", Ninserito, "), è pari")
else:
    print("Il numero che hai inserito, (", Ninserito, "), è dispari")
