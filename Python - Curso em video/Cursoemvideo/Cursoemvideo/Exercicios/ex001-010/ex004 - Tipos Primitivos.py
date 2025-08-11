# - DESAFIO 004: FAÇA UM PROGRAMA QUE LEIA ALGO DO TECLADO E MOSTRE SEU TIPO PRIMITIVO
# E TODAS AS INFORMAÇÕES POSSIVEIS!-

x=(input('Vamos destrinchar isso aí, meu parça! Quer saber sobre oque?'))
print(x)
print('CLASS:',type(x))
print('ALPHA:',x.isalpha())
print('APLHANUM:',x.isalnum())
print('LOWER:',x.islower())
print('DECIMAL:',x.isdecimal())
print('LOWER:',x.islower())
print('ELE É A PORRA DE UM SUPPER?:',x.isupper())
print('SPACE:',x.isspace())
print('DIGIT:',x.isdigit())
print('PRINTABLE:',x.isprintable())
print('ESTÁ CAPITALIZADO?', x.istitle())

# "x" NESTE CASO É UM OBJETO (POSSUI CARACTERISTICAS E REALIZA FUNCIONALIDADES)
# TODOS ESSES COM () DEPOIS DO NOME SÃO CHAMADOS DE MÉTODOS (TODO STRING TEM MÉTODOS)

