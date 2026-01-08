# Metodo de classe
class Biblioteca():
    bibliotecas = []

    def __init__(self,nome):
        self.nome = nome
        self._ativo = False
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    def listar_biblioteca():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome } ! {biblioteca.ativo}")

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
       return "Ativado" if self._ativo else "Desativada"

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
# biblioteca_cidade = True
biblioteca_shoping = Biblioteca("Biblioteca do shoping")

print(biblioteca_cidade)
print(biblioteca_shoping)

Biblioteca.listar_biblioteca()
