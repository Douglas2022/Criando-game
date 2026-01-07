class biblioteca:
    bibliotecas = []
    def __init__(self,nome):
        self.nome = nome
        self.ativo = False
        biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
biblioteca_cidade = biblioteca("Biblioteca da cidade")
biblioteca_shoping = biblioteca("Biblioeca do shoping")
print(biblioteca_cidade)
print(biblioteca_shoping)


        







