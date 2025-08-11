# PARA EU INCLUIR ALGO, TENHO QUE ADICIONAR O COMANDO import (importa o módulo ou biblioteca)
#EX: HÁ TRES BIBLIOTECAS:
#DOCES
#BEBIDAS
#COMIDAS
#PARA EU IMPORTAR UM DELAS: import bebida (IMPORTA TODAS AS FUNCIONALIDADES DO MÓDULO)
#PARA IMPORTAR APENAS UM ITEM DESTA BIBLIOTECA: from bebida import suco (IMPORTA APENAS AS FUNCIONALIDADES ESCOLHIDAS)

#BIBLIOTECA math:
# ceil ( ARREDONDAMENTO PRA CIMA )
# floor ( ARREDONDAMENTO PRA BAIXO )
# trunc "truncate" ( ELIMINAR DEPOIS DA VIRGULA )
# pow "power" (POTENCIAÇÃO)
# sqrt "Square root" (RAIZ QUADRADA)
# factorial (FATORIAL)

#DICA: É POSSIVEL RENOMEAR UM METODO COM O COMANDO "as"
# EX:from math import sqrt as raizquadrada (OU QUALQUER OUTRA COISA)

#import math #OU from math import sqrt
#num = int (input('DIGITE UM NÚMERO! '))
#raiz = math.sqrt(num) #COM "from math import sqrt NÃO É NECESSARIO UTILIZAR O "math."
#print(f'A RAIZ QUADRADA DE {num} É {raiz}!')


import random
num = random.randint (1, 10)
print(num)