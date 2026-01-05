class Game:
    def __init__(self,Name = "",YearLauch = 0,Multiplayer = 0,Note = 0):
        self.Name = Name
        self.YearLAuch = YearLauch
        self.Multiplayer = Multiplayer
        self.Note = Note
        self.TotalAvaluete = 0
        self.evaluators = 0

    def __str__(self):
        return f"Game: {self.Name}"
    
    def tecnical_sheet(self):
        print(f"###Dados do jogo###")
        print(f"Nome do jogo: {self.Name}")
        print(f"Ano de lançamento: {self.YearLAuch}")
        print(f"Modo multiplayers: {self.Multiplayer}")
        print(f"Avaliação do jogo: {self.Name}\n")

    def Avaluete(self,note):
        self.TotalAvaluete += note
        self.evaluators += 1

    def Averege(self):
        print(f"Media do filme: {self.Name}: {self.TotalAvaluete / self.evaluators}")

Game1 = Game("Game of Strones",2017,False,9.2)
Game2 = Game("Game of Zelda",2017,True,8.0)

Game1.tecnical_sheet()
Game2.tecnical_sheet()
Game1.Avaluete(9.5)
Game1.Avaluete(7.0)
Game1.Averege()

Game2.Avaluete(9.5)
Game2.Avaluete(7.0)
Game2.Averege()












        