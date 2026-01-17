from modelos.avaliacao import Avaliacao

class Biblioteca:
    Bibliotecas = []

    def __init__(self,nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        Biblioteca.Bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_biblioteca(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Status'}")
        for biblioteca in Biblioteca.Bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo}")

    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
       return "Ativado" if self._ativo else "Desativado"

# Biblioteca_cidade = Biblioteca("Biblioteca da cidade")
# Biblioteca_shoping = Biblioteca("Biblioteca do shoping")

# Biblioteca_cidade.alternar_estado()
# Biblioteca_shoping.alternar_estado()

# Biblioteca.listar_biblioteca()

    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)

        
        



    
