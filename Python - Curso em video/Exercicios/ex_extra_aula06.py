#FAÇA UMA SOMA NA QUAL A FRASE DE RESULTADO SEJA "A SOMA ENTRE X E Y É Z"

print('QUAL NUMERO VOCÊ QUER QUE EU SOME AGORA?')
n1=int(input('Me fala o primeiro!'))
n2=int(input('Agora me fala o segundo!'))
s=n1+n2
print(f'A soma entre {n1}+{n2} é {s},tonto')


# OU: print(f'A soma entre {n1}+{n2},é',s,'tonto')

# OU: print('A soma entre {} e {} vale {}'.format(n1,n2,s))