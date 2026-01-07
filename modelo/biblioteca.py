# Metodo de classe
class Biblioteca():
    bibliotecas = []

    def __init__(self,nome):
        self.nome = nome
        self.ativo = False
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    def listar_biblioteca():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome } ! {biblioteca.ativo}")

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shoping = Biblioteca("Biblioteca do shoping")
print(biblioteca_cidade)
print(biblioteca_shoping)

Biblioteca.listar_biblioteca()
