'''Si definisca una funzione che preso un dizionario di studenti e voti, restituisca
un dizionario con gli studenti suddivisi per intervalli di media di voto: k1
(18,23), k2(24,26) e k3(27,30).
Nel calcolo della media la lode permette di arrotondare all’intero successivo,
nel caso in cui nella lista dei voti non sia presente una lode l’arrotondamento è
per difetto. '''

from math import floor, ceil

def ordine(d1, d2):
    for k in d1:
        media = 0
        lode = False
        if "l" in d1[k]:
            lode = True
            for v in range(len(d1[k])-1):
                media += d1[k][v]
        else:
            for v in range(len(d1[k])):
                media += d1[k][v]
        if lode:
            media = ceil(media/(len(d1[k])-1))
        else:
            media = floor(media/len(d1[k]))
        print(media)
        if media >= k1 and media < k2:
            d2[(k1, k2-1)].append(k)
        elif media >= k2 and media < k3:
            d2[(k2, k3-1)].append(k)
        elif media >= k3 and media <= massimo:
            d2[(k3, massimo)].append(k)
    return d2
d1 = {
    "Dante" : [30,30,28,"l"],
    "Schopenhauer" : [27,26,24],
    "Milton" : [18,25,26],
    "Goethe" : [29,26,30,"l"]
}
k1 = 18
k2 = 24
k3 = 28
massimo = 30
d2 = {
    (k1, k2-1): [],
    (k2, k3-1): [],
    (k3, massimo): []
}
print(ordine(d1,d2))