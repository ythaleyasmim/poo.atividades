import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def exibir(self):
        x = self.x
        y = self.y
        print(f'{x}, {y}')

    def distancia(self, outro: Ponto):
        dx = self.x - outro.x
        dy = self.y - outro.y
        d = math.sqrt(dx**2 + dy**2)
        return d

    def move(self,dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distancia_origem(self):
        d = math.sqrt(self.x**2 + self.y**2)
        return d

    


print('criando pontos')
p = Ponto(2, 3)
a = Ponto(0, 0)

print(a)
print(p.x, p.y)

p.exibir()
a.exibir()

print(p.distancia(a))

p.move(10, 20)
p.exibir()



print('distancia origem')
print(p.distancia_origem())
