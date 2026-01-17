from modelo.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca cidade")
biblioteca_shoping = Biblioteca("Biblioteca shoping")

biblioteca_cidade.alternar_estado()

def main():
    Biblioteca.listar_biblioteca()

if __name__ == "__main":
   main()