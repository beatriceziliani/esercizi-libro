primoc = int (input ("inserisci i voti del primo"))
secondoc = int (input ("inserisci i voti del secondo"))
votitot = primoc + secondoc
perc1 = primoc / votitot * 100
perc2 = secondoc / votitot * 100
if perc1>perc2 :
    print ("il vincitore è il primo col", perc1, "%")
else:
    print ("il vincitore è il secondo col", perc2, "%")
