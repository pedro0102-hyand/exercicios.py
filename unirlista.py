def zipper(lista1,lista2):
    inter_max=min(len(lista1),len(lista2))
    return [
       (lista1[i],lista2[i])  for i in range(inter_max)
    ]
l1=['New York','Sao Paulo', 'Paris']
l2=['USA', 'Brazil', 'France', 'Belgium']
print(zipper(l1,l2))
