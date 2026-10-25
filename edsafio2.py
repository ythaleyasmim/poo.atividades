import urllib.request

try:
  urllib.request.urlopen("https://pudim.com.br")
  print("consigo acessar o site do pudim com sucesso")
except:
  print("nao consigo acessar o site pudim")
