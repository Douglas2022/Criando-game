from modelo.biblioteca import Biblioteca
from modelos.Itens.livro import livro
from modelos.Itens.revista import revista

biblioteca_cidade = Biblioteca("Biblioteca cidade")
biblioteca_shoping = Biblioteca("Biblioteca shoping")

livro1 = livro("1989","George Owel",30.0,"084-3245")
revista1 = revista("National Geograph","Jhon doe","15.00","Quinta")


# biblioteca_cidade.alternar_estado()

# biblioteca_cidade.receber_avaliacao('Fulano',8.5)
# biblioteca_cidade.receber_avaliacao('Ciclano',9.5)


def main():
    # Biblioteca.listar_biblioteca()
    print(vars(livro1))
    print(vars(revista1))
    
    

if __name__ == "__main":
   main()