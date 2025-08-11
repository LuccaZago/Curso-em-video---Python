# - DESAFIO 019: UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO! -

from random import choice

a1 = (input ('INFORME O PRIMEIRO ALUNO: '))
a2 = (input ('INFORME O SEGUNDO ALUNO: '))
a3 = (input ('INFORME O TERCEIRO ALUNO: '))
a4 = (input ('INFORME O QUARTO ALUNO: '))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)

print (f'O ALUNO ESCOLHIDO FOI: {escolhido}!')