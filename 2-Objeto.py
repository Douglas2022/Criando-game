class Game:
    name = ""
    yearLauch = 0
    multiplayear = False
    note = 0        

# 1- Primeiro jogo
game1 = Game()
game1.name = "Legends of Zelda: Breath of the wild"
game1.yearLauch = 2017
game1.multiplayear = False
game1.note = 9.5

# 2- Segundo jogo
game2 = Game()
game2.name = "Fort-Nite"
game2.yearLauch = 2017
game2.multiplayear = True
game2.note = 8.0

# 2-Terceiro jogo
game3 = Game()
game3.name = " Residente Evil 50"
game3.yearLauch = 2018
game3.multiplayear = True
game3.note = 9,9

# 2-Terceiro jogo
game4 = Game()
game4.name = "Soul Heavy"
game4.yearLauch = 2019
game4.multiplayear = False
game4.note = 7.5

print("\n###Dados do Jogo###")
print(f"\nNome do jogo: {game1.name}\nAno de laçamento: {game1. yearLauch}")
print(f"\nNome do jogo: {game2.name}\nAno de laçamento: {game2. yearLauch}")
print(f"\nNome do jogo: {game3.name}\nAno de laçamento: {game3. yearLauch}")
print(f"\nNome do jogo: {game4.name}\nAno de laçamento: {game4. yearLauch}")