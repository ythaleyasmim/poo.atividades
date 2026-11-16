class Gafanhoto:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")


# Objetos desenvolvidos durante a aula
G1 = Gafanhoto("João", 20)
G2 = Gafanhoto("Maria", 18)

G1.mensagem()
G2.mensagem()

G1.aniversario()
G1.mensagem()


# Meu objeto pessoal
class Pessoa:
    def __init__(self, nome, idade, curso, hobbies):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.hobbies = hobbies

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}.")
        print(f"Tenho {self.idade} anos.")
        print(f"Estudo {self.curso}.")
        print(f"Meus hobbies são: {self.hobbies}.")


Ythale = Pessoa(
    "Ythale",
    16,
    "Informática",
    "desenhar, escrever, ouvir música e ler"
)

Ythale.apresentar()