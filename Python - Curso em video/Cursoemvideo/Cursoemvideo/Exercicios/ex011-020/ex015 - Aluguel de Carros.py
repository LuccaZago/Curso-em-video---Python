# - DESAFIO 015: ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM  PERCORRIDOS POR UM CARRO ALUGADO
# E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO; CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA
# R$60 POR DIA E R$0.15 POR KM RODADO

#---------------- CODIGO ANTES DE SABER O ENUNCIADO------------------
#print (f'VOCÊ ESTÁ PLANEJANDO ALUGAR UM CARRO?\n'
#       f'O ALUGUEL É DE 7.5% MENSALMENTE BASEADO NO VALOR DO CARRO, OK?')
#vc = float (input('QUAL O VALOR DO CARRO QUE VOCÊ VAI ALUGAR? '))
#a = float(vc * (7.5/100))
#print (f' O VALOR DO ALUGUEL QUE VOCÊ DEVERÁ PAGAR É DE: R${a:.2f}!')
#-----------------------------------------------------------------------

print (f'VOCÊ ALUGOU UM CARRO E QUER SABER O VALOR QUE IRÁ PAGAR?\n')
km = float (input('QUANTOS KMs FORAM RODADOS? '))
da = int (input('POR QUANTOS DIAS? '))
v_km = km * 0.15
v_da = da * 60
vc = v_km+v_da
print (f'O VALOR TOTAL A PAGAR É DE R${vc:.2f}!')