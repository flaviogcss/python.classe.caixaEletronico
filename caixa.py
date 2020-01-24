from classes import Cliente, Conta

#funções do caixa eletronico

class CaixaEletronico():

  def __init__(self):
    nome = input('Qaul o seu nome')
    cpf = input('Digite seu cpf')
    cliente = Cliente(nome, cpf)
    self.conta = Conta(cliente)
    print(f'Olá {self.conta.titular.nome}, sua conta é: {self.conta.numero}')

  def menu(self):    
    print('1- Consultar/n 2- Depositar/n 3- Sacar/n')
    opcao = input('Digite uma opção: ')

    if opcao == '1':
      self.conta.consultar_saldo()
      print(f'Seu saldo é: {self.conta.saldo}')

    elif opcao == '2':
      valor = float(input('Valor a ser depositado: '))      
      self.conta.deposito(valor)
      print(f'Deposito efetuado. Seu novo saldo é de: {self.conta.saldo}')

    elif opcao == '3':
      valor = float(input('Digite um valor'))

      if self.conta.sacar(valor):
        saldo_atualizado = self.conta.saldo - valor
        print(f'Saque efetuado com sucesso. Seu novo saldo é: {saldo_atualizado}')

      else:
        print('Saldo insuficiente')
         
    else:
      print('opcao invalida')

