from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shoping = Biblioteca("Biblioteca do shoping")

biblioteca_cidade.alternar_estado()

biblioteca_cidade.receber_avaliacao('Douglas',8.5)
biblioteca_cidade.receber_avaliacao('Paulo',9.5)

def main():
    Biblioteca.listar_biblioteca()

if __name__ == "__main__":
    main()

    

