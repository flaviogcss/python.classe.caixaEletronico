from random import randint


class Cliente:

class Conta:
    def __init__(self, cliente):
        
    self.numero = self._gerar()
    self._saldo = 0

    def extrato(self):
        print(f'Numero: {self.numero}\nSaldo: {self._saldo}')


    def _gerar(self):
    self.random_numero = f'{randint(1000, 9999)}-{randint(1, 9)}'
    return self.random_numero
