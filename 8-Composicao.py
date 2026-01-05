
class Game:
    total_game = 0 #Variável de classe para contar o número total de jogos
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

class GameStdio:
    def __init__(self,name=""):
        self.name = name
        self.games = []
    
    def add_game(self,game):
        self.games.append(game)

    def evaluete_studio_equality(self):
        total_games = sum(game.Note for game in self.games)
        nun_games = len(self.games)
        if nun_games == 0:
            print(f"O estudio {self.name} ainda não lancou o jogo")
        else:
           everege_note = total_games / nun_games
           print(f"Avaliação média dos jogos do estudio {self.name} : {everege_note:.2f}")
 
game1 = Game("Legends of Zelda",2017,False,9.5)
game2 = Game("FortNite",2017,True,8.0)
game3 = Game("The last of us",2020,False,9.0)

studio = GameStdio("Awesone Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluete_studio_equality()

for game in studio.games:
    game.tecnical_sheet()




        



        
