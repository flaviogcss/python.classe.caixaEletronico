from caixa import CaixaEletronico

# arquivo que vai rodar no terminal

caixaeletronico = CaixaEletronico()

resposta = ''

while resposta != 's':
    resposta = input('Digite e para entrar, s para sair')
    if resposta == 'e':
        caixaeletronico.menu()
    elif resposta != 'e' and resposta != 's':
        print('Resposta Invalida')

