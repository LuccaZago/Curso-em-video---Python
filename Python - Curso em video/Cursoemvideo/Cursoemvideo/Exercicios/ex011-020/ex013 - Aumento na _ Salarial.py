# - DESAFIO 013: FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
# E MOSTRE A ELE SEU NOVO SALÁRIO COM 15% DE AUMENTO -
salario=s=(float(input(f'ME INFORME O SEU SALÁRIO PARA QUE EU POSSA CALCULA-LO COM UM AUMENTO DE 15%!')))
percent=p=(float(15/100))
aumento=a=(float(s*p))
novo_salario=n=(float(s+a))
print(f'O SEU SALÁRIO DE R${s:.2f} COM UM AUMENTO DE 15% FICA NO VALOR DE R${n:.2f}')
