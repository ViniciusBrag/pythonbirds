class Pessoa():
    def __init__(self, *filhos, nome = None, idade = 23):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá mundo'





if __name__ == '__main__':
   vinicius = Pessoa(nome='Vinicius')
   luciano = Pessoa(vinicius, nome='Luciano')
   print(luciano.nome)
   print(luciano.idade)
   print(luciano.filhos)
   for filho  in luciano.filhos:
       print(filho.nome)




