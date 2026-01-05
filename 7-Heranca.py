#Classe Superclasse - Classe generalizada
class Game:
    Total_games = 0
    def __init__(self,Name = "",YearLauch = 0,Multiplayer = 0,Note = 0):
        self.Name = Name
        self.YearLAuch = YearLauch
        self.Multiplayer = Multiplayer
        self.Note = Note
        Game.Total_games +=1
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
        print(f"Media do jogo: {self.Name}: {self.TotalAvaluete / self.evaluators}")

#Classe derivada(Subclasse) - Especializado
class Single_players(Game):
    def __init__(self, Name="", YearLauch=0,Note=0,storyLine = ""):
        super().__init__(Name,YearLauch,Multiplayer=False,Note=Note)
        self.storyLine = storyLine

    def tecnical_sheet(self):
        super().tecnical_sheet()
        print(f"Enredo: {self.storyLine}\n")

mult_game = Game("Fortnite",2017,True,8.0)
mult_game.tecnical_sheet()

sing_game = Single_players("The last of Us ",2018,9.5,"Emocionante hitória de sobrevivência e vigança! ")
sing_game.tecnical_sheet()



       










        