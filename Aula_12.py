# Permuta, combinação e produtos cartesianos.
# Biblioteca 'intertools
# import itertools
#

# # elementos = ["A","B","C"]
# # #AB, AC, BC -> 3 combinações
# #
# # permutacoes = permutations (elementos,2)
# # #
# # # for permutacao in permutacoes :
# # #     print(permutacao)
# #
# # from itertools import permutations
# #
# # numeros = [1, 2 , 3, 4 , 5 ,6, 7, 8, 9 ,10]
# # permutacoes = permutations (numeros,4)
# #
# # for permutacao in permutacoes:
# #     print(permutacao)
#
# from itertools import combinations
# numeros_loteria = [1,2,3,4,5,6,7,8,9,10]
# combinacoes = combinations(numeros_loteria,5)
#
# # for combinacao in combinacoes:
# #     print(combinacao)
#
# from itertools import product
# cores = [ "vermelho","verde","azul","amarelo"]
# frutas = ["maça", "banana","limão","abacate"]
# tamanhos =["pequeno", "médio", "grande", "gigante"]
#
# salada_de_fruta = product(cores, frutas,tamanhos)
# for possibilidade_salada in salada_de_fruta:
#     print(possibilidade_salada)

# DICIONÁRIOS

dados_pessoais_pessoa1 = {
    "nome": "João",
    "sobrenome": "Moreira",
    "idade": 44,
    "estado_civil": "Viúvo",
    "endereços":[
    {
        "tipo_endereço": "comercial",
        "rua": "Rua das Flores",
        "numero": 256,
        "bairro": "Centro"
    },
    {
        "tipo_endereço": "residencial",
        "rua": "Rua das Abobora",
        "numero": 123,
        "bairro": "Caiuá"
    }
                  ]

    }


print(dados_pessoais_pessoa1)