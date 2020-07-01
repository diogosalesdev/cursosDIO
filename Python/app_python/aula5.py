lista  = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista)
print(lista_animal[1])

for x in lista_animal:
  print(x)

soma = 0
for x in lista:
  print(x)
  soma += x
print(soma)

print(sum(lista))
print(max(lista))
print(min(lista))
print(min(lista_animal))


if 'gato' in lista_animal:
  print('Existe um gato na lista')
else:
  print('Não existe um gato na lista') 

if 'lobo' in lista_animal:
  print('Existe um lobo na lista')
else:
  print('Não existe um lobo na lista. Será incluído')
  lista_animal.append('lobo')
  print(lista_animal) 