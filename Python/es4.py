class Atleta:
    def __init__(self, nome, age, visitaMedica):
        self.nome = nome
        self.anni = age
        self.visitaMedica = visitaMedica
        self.squadra = ""
    def definisciSquadra(self):
        self.squadra = input("dimmi la squadra dove gioca")
    def effettuaVisita(self):
        self.visitaMedica = True
    def trascrivoDati(self):
        print(self.nome, self.anni, self.visitaMedica, self.squadra)

atleta = Atleta("Marco", 20, True)
atleta2 = Atleta("mario", 19, False)
atleta2.definisciSquadra()
atleta2.trascrivoDati()