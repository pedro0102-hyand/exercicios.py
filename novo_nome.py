nome=input("Digite um nome:")
tamanho=len(nome)
indice=0
novo_nome=''
while indice<tamanho:
  letra=nome[indice]
  indice+=1
  novo_nome+=f'*{letra}'
novo_nome+='*'
print(novo_nome)
