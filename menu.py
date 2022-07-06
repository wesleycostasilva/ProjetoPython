import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ""

def menu():
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Cadastrar\n'                        +
          '2. Consultar\n'                        +
          '3. Nome\n'                             +
          '4. Atualizar Telefone\n'               +
          '5. Atualizar Endereço\n'               +
          '6. data de Nascimento\n'               +
          '7. dataDeBatismo\n'                    +
          '8. nomeDoPastor \n'                    +
          '9. estadocivil\n'                      +
          '10.nomeDaIgreja\n'                     +
          '11.endereco\n'                         +
          '12. Excluir\n'                         +
          '0.Sair\n')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe seu nome: ')
            nome = input()
            print('Informe o nome da igreja: ')
            igreja = input()
            print('Informe o nome do Pastor: ')
            pastor = input()
            print('Informe estado cívil')
            estadocívil = input ()
            print('Informe a data do Batismo')
            batismo = input()
            print('Informe seu telefone: ')
            telefone = input()
            print('Informe seu endereço: ')
            endereco = input()
            print('Informe sua data de nascimento: ')
            dataDeNascimento = input()
            #Chamar o método inserir
            operacoes.inserir(nome, telefone, endereco,igreja,pastor,estadocívil,batismo,dataDeNascimento )
        elif this.opcao == 2:
            operacoes.consultar()
        elif this.opcao == 3:
            print("Informe o nome")
            this.codigo=int(input())
            print("informe o novo nome: ")
            this.campo = input()
            operacoes.atualizar(this.codigo, 'nome', this.campo)
        elif this.opcao == 4:
            print("Informe o telefone")
            this.codigo = int(input())
            this.campo = input()
            operacoes.atualizar(this.codigo, 'telefone', this.campo)
        elif this.opcao == 5:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            print("informe o novo endereço: ")
            this.campo = input()
            operacoes.atualizar(this.codigo, 'endereco', this.campo)
        elif this.opcao == 6:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            print("informe a nova data de nascimento: ")
            this.campo = input()
            operacoes.atualizar(this.codigo, 'dataDeNascimento', operacoes.tratarData(this.campo))
        elif this.opcao == 7:
             print("Informe o código que deseja atualizar")
             this.codigo = int(input())
             operacoes.atualizar(this.codigo, 'dataDeBatismo', operacoes.tratarData(this.canpo))
        elif this.opcao == 8:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            operacoes.atualizar(this.codigo, 'nomeDoPastor', operacoes.tratarData(this.campo))
        elif this.opcao == 9:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            operacoes.atualizar(this.codigo, 'estadocivil', operacoes.tratarData(this.campo))
        elif this.opcao == 10:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            operacoes.atualizar(this.codigo, 'nomeDaIgreja', operacoes.tratarData(this.campo))
        elif this.opcao == 11:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            operacoes.atualizar(this.codigo, 'endereco', operacoes.tratarData(this.campo))
        elif this.opcao == 12:
            print("Informe o código para a exclusão do dado")
            this.codigo = int(input())
            operacoes.excluir(this.codigo)
        else:
            print('Opção escolhida não é válida!')

