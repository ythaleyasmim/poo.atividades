def cadastrar():
    nome = input('Nome: ')
    idade = input('Idade: ')

    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome};{idade}\n')

    print('Pessoa cadastrada com sucesso!')


def listar():
    try:
        with open('pessoas.txt', 'r') as arquivo:
            pessoas = arquivo.readlines()

            if len(pessoas) == 0:
                print('Nenhuma pessoa cadastrada.')
            else:
                for pessoa in pessoas:
                    nome, idade = pessoa.strip().split(';')
                    print(f'{nome} tem {idade} anos.')

    except FileNotFoundError:
        print('Nenhuma pessoa cadastrada.')
while True:
    print('\n1 - Cadastrar pessoa')
    print('2 - Listar pessoas')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        break
    else:
        print('Opção inválida!')