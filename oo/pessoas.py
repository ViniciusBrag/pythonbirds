class Pessoa():
    def __init__(self, nome = None, idade = 23):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá mundo'





if __name__ == '__main__':
    p = Pessoa('Luciano')
    p.nome = 'Vinicius'
    print(p.nome)
    print(p.idade)



