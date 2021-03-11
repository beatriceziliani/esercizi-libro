class Prodotto:
    def __init__(self, nome, prezzo, seInSconto, sconto = 0):
        self.nome = nome
        self.prezzo = prezzo
        self.seInSconto = seInSconto
        self.sconto = sconto
    def assegnaPrezzo(self):
        self.prezzo -= self.prezzo*(self.sconto/100)
        print(self.prezzo)

prodotto = Prodotto("Astuccio", 20, False)
prodotto.assegnaPrezzo()