class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}, você tem {self.idade} anos.'


if __name__ == '__main__':
    f1 = Pessoa(nome="Amanda", idade=24)
    f2 = Pessoa(nome="Filho Virtual", idade=5)
    p = Pessoa(f1, f2, nome="Leonardo", idade=49)

    print(p.cumprimentar())

    for filho in p.filhos:
        print("Nome dependente: {} - Idade: {}".format(filho.nome, filho.idade))
