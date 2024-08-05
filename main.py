nomes = []

while True:
    print('1 - para inserir nome.')
    print('2 - para sair.')

    op = input('Digite o numero da opção desejada: ')

    match op:
        case '1':
            novo_nome = input('Informe um nome: ').capitalize()
            nomes.append(novo_nome)
            print('Esses sãos os nome que voce digitou: \n')
            for nome in nomes:
                print(f'- {nome}.')
        case '2':
            break
        case _: 
            print('Opção inválida.')