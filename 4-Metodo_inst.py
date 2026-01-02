class Game:
    def __init__(self,name="",yearLaunch=0,multiplayer=0,note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
    
    def __str__(self):
        return f"Game: {self.name}"
    
    def tecnical_sheet(self):
        print("\n##Dados do Jogo##")
        print(f"O nome do jogo: {self.name}")
        print(f"O ano de lançamento: {self.yearLaunch}")
        print(f"Modo multplayear?: {self.multiplayer}")
        print(f"Avaliação do jogo: {self.note}\n")

game1 = Game("Legends of strone",2017,False,9.5)
game2 = Game("Legends of Black",2019,True,8.0)

game1.tecnical_sheet()
game2.tecnical_sheet()
       

    










        