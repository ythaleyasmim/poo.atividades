try:
  a= int(input('Numerador:'))
  b = int(input('Denominador:'))
  r = a/b
except (ValueError, TypeError):
  print('tivemos um problema com o dado que foi digitado')
except ZeroDivisionError:
  print('impossivel dividir por zero!')
except KeyboardInterrupt:
  print('O usuario preferiu evitar os dados')
else:
  print(f'o resultado é {r}')
finally:
  print('volte sempre :)')