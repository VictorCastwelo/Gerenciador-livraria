#Espaço para funções
def cadastrar_livro(id): #Função para cadastrar livros
    id = id_global #o id atribuido ao livro cadastrado recebe o valor da variável id_global

    print(f'Id do livro: {id}') #impressão do id referente ao livro que está sendo cadastrado

    #inputs para obter informações do livro cadastrado
    livro = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o autor do livro: ').lower()
    editora = input('Por favor entre com a editora do livro: ')

    cadastro = { #Dicionário de cadastro do livro escolhido
        'Id': id,
        'Nome': livro,
        'Autor': autor,
        'Editora': editora
    }


    lista_livro.append(cadastro) #adição do dicionário de cadastro a lista de livros

    print('')
    print('Livro cadastrado! Retornando ao menu principal...')
    print('')

def consultar_livro(): #Função para realizar consultas de livro
    while True:
        #Pequeno menu com laço de repetição que só se encerra se o usuário digitar 4

        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os Livros')
        print('2 - Consultar Livro por id')
        print('3 - Consultar Livro(s) por autor')
        print('4 - Retornar ao menu')

        escolha = int(input('Qual a opção desejada? '))

        #Abaixo teremos condicionais para cada opção que o usuário possa optar
        if escolha == 1: #consulta todos os livros
            for cadastro in lista_livro:
                print(cadastro) #aqui o programa imprimirá a lista de todos livros cadastrados
                print('')

        elif escolha == 2: #Aqui o programa irá imprimir somente o livro selecionado por id
            id = int(input('Digite o id do livro: '))
            print(lista_livro[id - 1]) #impressão dos dados do livro referente ao seu id (para acessar índice de listas sempre será necessário subtrair 1 do índice que buscamos)
            print('')

        elif escolha == 3: #Aqui será realizada uma busca por autor
            busca = input('Digite o autor do(s) livro(s): ').lower()

            #Abaixo foi realizada uma varredura dentro da lista e dentro dos dicionários de livros cadastrados

            for cadastro in lista_livro: #varredura pelos índices cadastrados na lista
                if cadastro['Autor'] == busca: #condição para imprimir somente o cadastro solicitado
                    print(cadastro)
                    print('')

        elif escolha == 4: #retornará ao menu principal com um break do laço da função
            break #laço encerrado
            
        elif escolha <= 0 or escolha > 4: #caso usuário digite uma opção inválida
            print('Opção inválida. Tente novamente!')
            continue

def remover_livro(): #função referente a remoção de livros
    #usei except para reportar ao usuário caso ele digite número id que não exista na lista de livros
    try:
        remocao = int(input('Digite o id do livro a ser removido: '))
        del lista_livro[remocao - 1] #remoção do dicionário de livro cadastrado (os índices de uma lista é sempre subtraido por 1)

        print('')
        print('Livro removido com sucesso!')
        print('')

        if remocao <= 0: #caso o usuário digite número negativo
            print('Id inválido, tente novamente')
            remocao = int(input('Digite o id do livro a ser removido: '))

    except: #caso id não exista na lista
        print('Id inválido, tente novamente')
        remocao = int(input('Digite o id do livro a ser removido: '))


#Programa principal (MAIN)

lista_livro = [] #lista que receberá os dicionários de cadastros
id_global = 0 #id global que receberá cada livro cadastrado (antes de chamar uma função, é acrescentado 1 ao valor original dessa variável)

while True: #laço infinito do menu principal
    print('Bem vindo a Livraria do Victor Castelo Branco Miranda')
    print('-' * 60)
    print('-' * 20, 'MENU PRINCIPAL', '-' * 24 )
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')

    print('')

    op = int(input('Digite sua opção: '))

    #Condicionais para possíveis escolhas do usuário
    if op == 1: #cadastra livro
        id_global += 1 #acrescenta-se 1 ao id para que o primeiro livro não comece com 0
        cadastrar_livro(id_global) #chama função de cadastro

    elif op == 2: #consulta livro e chama função
        consultar_livro()

    elif op == 3: #remove livro e chama sua função
        remover_livro()

    elif op == 4: #encerra programa e roda o break com uma mensagem de encerrando
        print('Encerrando...')
        break

    elif op < 1 or op > 4: #caso usuário não digite valores disponíveis
        print('Opção inválida, tente novamente')
        op = int(input('Digite sua opção: '))
