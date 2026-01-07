class biblioteca:
    nome = ""
    ativo = False

biblioteca_cidade = biblioteca()
biblioteca_cidade.nome = "Biblioteca da cidade"
biblioteca_cidade.ativo =  True
biblioteca_shoping = biblioteca()
bibliotecas = [biblioteca_cidade,biblioteca_shoping]

print(vars(biblioteca_cidade))
print(vars(biblioteca_shoping))

for biblioteca in bibliotecas:
    print(vars(biblioteca))







