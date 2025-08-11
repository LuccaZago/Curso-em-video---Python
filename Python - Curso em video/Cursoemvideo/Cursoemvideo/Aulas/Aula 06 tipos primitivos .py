#ANTES DE RODAR O PROGRAMA TEM QUE COLOCAR AS "#" NOS CODIGOS PRA NÃO CAGAR TUDO'
n1=input('Digite o primeiro número')
n2=input('Digite o segundo número')
s=n1+n2
print('a soma vale',s)

#R: a soma vale 'n1n2'
#----------------------------------------------------------------------------------

#Quando eu coloco ''input('X')'' esse valor, mesmo que seja um numero, não é considerado um número
#mas sim um string
#O que tem que ser colocado então é o tipo primitivo int! Assim:
#---------------------------------------------------------------------------------

n1=int(input('Digite o primeiro número'))
n2=int(input('Digite o segundo número'))
s=n1+n2
print(f'A soma vale {s}')

#R: a soma vale 's'
#----------------------------------------------------------------------------

#TIPOS PRIMITIVOS MAIS BÁSICOS: int (Números inteiros),float (Números reais ou de ponto flutuante)
#bool (Valores lógicos ou booleanos),str(Valores caractéres ou strings)
#Exemplos:
#int: 7,-4,0,978894,etc... (Positivos, negativos ou nulos de qualquer valor são inteiros para o Python)
##################################################
#float: Numeros Reais "decimais" (com ponto FLUTUANTE, por isso float))
###################################################
#bool: Valores Lógicos, ou seja, 'True' ou 'False'
#####################################################
#str:Tudo que é "Mensagem", ou seja 'X' é um string. Tanto 'Olá' quanto '8,7' ou "''" (String vazia)
###############################################################
#Juntar um string no outro se chama CONCATENAR
#PARA SABER O TIPO PRIMITIVO DE ALGO: print(type(X))
#EX: n1=input ('digite um numero')
#print(type(n1))

n1=input('Você quer saber a minha class?')
print(type(n1))