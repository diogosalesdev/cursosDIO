a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))
if a>b and a>c:
  print('O maior número é {}'.format(a))
elif b>a and b>c:
  print('O maior número é {}'.format(b))
elif c>a and c>b:
  print('O maior número é {}'.format(c))
print('FIM')