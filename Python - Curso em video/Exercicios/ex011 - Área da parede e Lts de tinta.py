# - DESAFIO 011: FAÇA UM PROGRAMA QUE LEIA LARGURA E A ALTURA DE UMA PAREDE EM METROS;
#  CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA
#  PINTA UMA ÁREA DE 2M² -
#altura=h
#largura=b
#area=h(altura)*b(largura ou base)
#litro=l
#l=a/2

print(f'ME INFORME A ALTURA E LARGURA DA SUA PAREDE PARA SABER QUANTOS LITROS DE TINTA SERÃO NECESSARIOS PARA PINTA-LA')
h=float(input(f'QUAL É A ALTURA?\n '))
b=float(input(f'QUAL É A LARGURA?\n '))
a=float(h*b)
l=float(a/2)
print(f'A SUA PAREDE TEM A DIMENSÃO DE {h} x {b}! SENDO ASSIM: A AREA DA PAREDE É {a:}m²\n'
      f'SE O LITRO DA TINTA RENDER 2M², VOCÊ PRECISARÁ DE {l}L por demão de tinta!')
