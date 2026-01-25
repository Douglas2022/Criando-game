from modelos.avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = []
    def __init__(self,nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_biblioteca(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Status'}")
        for biblioiteca in Biblioteca.bibliotecas:
            print(f"{biblioiteca.nome.ljust(25)} | {biblioiteca.ativo}")
    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "Ativado" if self._ativo else "Desativado"
        
    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)


    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao.nota for avaliacao in self._avaliacao )
        media = round(soma / len(self._avaliacao),1)
        return media





# biblioteca_cidade = Biblioteca("Biblioteca da cidade") 
# biblioteca_shoping = Biblioteca("Biblioteca do shoping") 

# biblioteca_cidade.alternar_estado()
# biblioteca_shoping.alternar_estado()


# Biblioteca.listar_biblioteca()










 

        