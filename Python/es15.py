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