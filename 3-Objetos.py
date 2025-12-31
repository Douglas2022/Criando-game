class Game:
    def __init__(self,name = "",yearLauch = 0,multiplayear = 0,note = 0):
        self.name = name
        self.yearLauch = yearLauch
        self.multiplayear = multiplayear
        self.note = note

    def __str__(self):
        return f"Game:{self.name}"
    
game1 = Game("Legends of League",2017,False,9.5)
game2 = Game("Fort-Nite",2010,True,8.5)

print("\n###Dados do Jogo###")
print(f"\nNome do jogo: {game1.name}\nAno de laçamento: {game1. yearLauch}")
print(f"\nNome do jogo: {game2.name}\nAno de laçamento: {game2. yearLauch}")
