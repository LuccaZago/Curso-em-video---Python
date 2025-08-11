# - DESAFIO 016: DIGITE UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA SUA PORÇÃO INTEIRA! -
#EX: DIGITE UM NÚMERO: 6.127; O NÚMERO 6.127 TEM A PARTE INTEIRA 6

from math import trunc

num = float (input ('DIGITE UM NÚMERO COM DECIMAIS PARA QUE EU LHE MOSTRE A PARTE INTEIRA! '))
pi = trunc(num)
print(f'A PARTE INTEIRA DE: {num}\n'
      f'É: {pi}!')

#'''Também é possivel com:
#num = float ('Digite um número: )
#print ('O valor digitado foi {} e a sua parte inteira é:{}'.format(num, int(num)))