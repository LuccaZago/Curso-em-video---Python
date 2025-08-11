# - DESAFIO 018: FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE O VALOR DE SENO, COSSENO E TANGENTE
#  DESTE ANGULO! -

from math import sin, cos, tan, radians

x = float(input ('DIGITE UM ÂNGULO PARA SABER OS VALORES DE SEN, COS E TAN: '))
#O SENO, COSSENO E TANGENTE, NÃO VEM CONVERTIDOS PARA RADIANOS POR ISSO O COMANDO "radians"
s = sin (radians(x))
c = cos (radians(x))
t = tan (radians(x))

print (f'O VALOR DE SEN, COS E TAN PARA O ÂNGULO DE {x}º SÃO:\n'
      f'SEN: {s:.2f}!\n'
      f'COS: {c:.2f}!\n'
      f'TAN: {t:.2f}!\n')