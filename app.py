from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shoping = Biblioteca("Biblioteca do shoping")

biblioteca_cidade.alternar_estado()

def main():
    Biblioteca.listar_biblioteca()

if __name__ == "__main__":
    main()

    

