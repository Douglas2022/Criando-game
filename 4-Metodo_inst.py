class Game:
    def __init__(self, nome="", lancamento=0, multiplayer=False, nota_inicial=0):
        self.nome = nome
        self.lancamento = lancamento
        self.multiplayer = multiplayer
        self.nota_inicial = nota_inicial
        self.totalNota = 0
        self.qtdAvaliacoes = 0

    def __str__(self):
        return f"Game: {self.nome}"
    
    def ficha_tecnica(self):
        print("\n## Dados do jogo ##")
        print(f"O nome do jogo: {self.nome}")
        print(f"O ano de lançamento: {self.lancamento}")
        print(f"Modo multiplayer: {self.multiplayer}")
        print(f"Avaliação inicial: {self.nota_inicial}")

    def avaliacao(self, nota):
        self.totalNota += nota
        self.qtdAvaliacoes += 1

    def media(self):
        if self.qtdAvaliacoes > 0:
            media = self.totalNota / self.qtdAvaliacoes
            print(f"A média do jogo {self.nome}: {media:.2f}")
        else:
            print(f"O jogo {self.nome} não possui avaliações")


game1 = Game("Legends of Stone", 2017, False, 9.5)
game2 = Game("Legends of Black", 2019, True, 8.0)

game1.ficha_tecnica()
game2.ficha_tecnica()

game1.avaliacao(9.0)
game1.avaliacao(7.5)
game1.media()

game2.avaliacao(7.0)
game2.avaliacao(6.0)
game2.media()
