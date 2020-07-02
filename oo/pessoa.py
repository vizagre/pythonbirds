class Pessoa:
    def __init__(self, nome=None, idade=0):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}, você tem {self.idade} anos.'

if __name__ == '__main__':
    p = Pessoa()
    p.nome="Leonardo"
    p.idade=49
    print(p.cumprimentar())