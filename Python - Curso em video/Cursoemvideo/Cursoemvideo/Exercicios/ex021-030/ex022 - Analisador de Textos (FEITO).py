# DESAFIO 022: - CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# a) O NOME COM TODAS AS LETRAS MAIÚSCULAS
# b) O NOME COM TODAS MINÚSCULAS
# c) QUANTAS LETRAS AO TOTAL (SEM CONSIDERAR ESPAÇOS)
# d) QUANTAS LETRAS TEM O PRIMEIRO NOME -

nome = input('QUAL É O SEU NOME COMPLETO? ')
nome_dividido = nome.split()
print (f'O SEU NOME EM DIFERENTES FORMATOS:\n'
       f'UPPER:{nome.upper()}!\n'
       f'LOWER:{nome.lower()}!\n'
       f'LENGTH (TAMANHO):{(len(nome.strip()))}!\n'
       f'TAMANHO DO SEU PRIMEIRO NOME:{len(nome_dividido[0])}!')
