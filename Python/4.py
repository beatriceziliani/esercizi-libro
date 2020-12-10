print("Calcola l'area del quadrato")
l_quadrato = int(input("Inserisci il lato del quadrato: "))
A_quadrato = l_quadrato ** 2
print("L'area del quadrato scelto è:", A_quadrato)

print("Calcola l'area del rettangolo")
h_rettangolo = int(input("scrivi l'altezza del rettangolo: "))
b_rettangolo = int(input("scrivi la base del rettangolo: "))
A_rettangolo = h_rettangolo * b_rettangolo
print("L'area del rettangolo scelto è:", A_rettangolo)

print("Calcola l'area del tringolo")
h_triangolo = int(input("Inserisci l'altezza del triangolo: "))
b_triangolo = int(input("Inserisci la base del triangolo: "))
A_triangolo = (h_triangolo * b_triangolo) / 2
print("L'area del triangolo scelto è:", A_triangolo)

print("Calcola l'area del cerchio")
r_cerchio = int(input("Inserisci la misura del raggio del cerchio: "))
A_cerchio = (r_cerchio ** 2) * 3.14
print("L'area del cerchio scelto è:", A_cerchio)
