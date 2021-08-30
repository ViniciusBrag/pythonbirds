class Pessoa():
    olhos = 2
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
   for filho  in luciano.filhos:
       print(filho.nome)

   luciano.sobrenome = 'Braga'
   print(luciano.sobrenome)
   del luciano.filhos
   luciano.olhos = 1
   del luciano.olhos
   print(luciano.__dict__)
   print(vinicius.__dict__)
   Pessoa.olhos = 3
   print(Pessoa.olhos)
   print(luciano.olhos)
   print(vinicius.olhos)
   print(id(Pessoa.olhos)),print(id(luciano.olhos)), print(id(vinicius.olhos))





