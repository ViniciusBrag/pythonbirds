class Pessoa():
    def cumprimentar(self):
        return f'Olá mundo'





if __name__ == '__main__':
    p = Pessoa()
    print(id(p))
    print(p.cumprimentar())



