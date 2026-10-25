try:
  a= int(input('Numerador:'))
  b = int(input('Denominador:'))
  r = a/b
except Exception as erro:
  print('o problema encontrado foi{erro.__class__}')
else:
  print(f'o resultado é {r}')
finally:
  print('volte sempre :)')