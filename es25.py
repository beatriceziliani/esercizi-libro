
c1 = input("qual è il nome del primo candidato?")
c2 = input("qual è il nome del secondo candidato?")
c1p = int(input("qual è il punteggio del primo candidato?"))
c2p = int(input("qual è il punteggio del secondo candidato?"))
 
lista = [c1, c2] 
sorted(lista,key=len) 
sorted(lista,key=len) 
lista.sort()  
sorted(lista,key=len) 
print("questo è l'ordine alfabetico dei nomi dei 2 candidati:", lista)

if c1p > c2p :
    print("il vincitore è", c1)
    
elif c1p < c2p :
    print("il vincitore è", c2)
    
else :
    print("i candidati hanno ottenuto lo stesso punteggio")
    
