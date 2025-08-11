#----------------- Desafio 002.5: Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas!----------
print('Qual a sua data de nascimento?')
msg01='Então você nasceu em'
msg02='e já ta acabado assim?'
Dia=input('Dia:')
Mes=input('Mês:')
Ano=input('Ano:')
print(msg01,Dia+'/'+Mes+'/'+Ano,msg02)
#poderia ser print('Então você nasceu em',Dia+'/'+Mes+'/'+Ano,'e já ta acabado assim?')