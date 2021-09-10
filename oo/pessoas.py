class Pessoa():
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 23):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá mundo meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42


    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f' {cls} - olhos {cls.olhos}'

class Homen(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f' {cumprimentar_da_classe } Aperto de mão'


class Mutante(Pessoa):
    olhos = 3




if __name__ == '__main__':
   vinicius = Mutante(nome='Vinicius')
   luciano = Homen(vinicius, nome='Luciano')
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
   print(Pessoa.olhos)
   print(luciano.olhos)
   print(vinicius.olhos)
   print(id(Pessoa.olhos)),print(id(luciano.olhos)), print(id(vinicius.olhos))
   print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
   print(Pessoa.nome_e_atributos_de_classes(), luciano.nome_e_atributos_de_classes())
   pessoa = Pessoa('anonimo')
   print(isinstance(pessoa, Pessoa))
   print(isinstance(pessoa, Homen))
   print(isinstance(vinicius, Pessoa))
   print(isinstance(vinicius, Homen))
   print(vinicius.olhos)
   elisa = Pessoa(nome='Elisa')
   print(elisa.olhos)
   print(luciano.cumprimentar())
   print(vinicius.cumprimentar())










