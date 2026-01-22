from .intems_biblioteca import intems_bibloteca

class livro(intems_bibloteca):
    def __init__(self,titulo,autor,preco,isbn):
        super().__init__(titulo,autor,preco)
        self.isbn = isbn


        
   