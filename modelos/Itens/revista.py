from modelos.Itens.intems_biblioteca import intems_bibloteca

class revista(intems_bibloteca):
    def __init__(self, titulo, autor, preco,edicao):
        super.__init__(titulo,autor,preco)
        self.edicao = edicao 

        