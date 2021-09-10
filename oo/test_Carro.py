from unittest import TestCase

from oo.Carro import *


class CarroTesteCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def teste_girar_a_direita(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)


    def teste_girar_a_esquerda(self):
        direcao = Direcao()
        self.assertEqual('Oeste', direcao.valor)