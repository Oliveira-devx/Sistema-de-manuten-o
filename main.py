from contruindo.equipamentos import listar_equipamentos, consultar_equipamento_por_nome


def menu():

    while True:

        print("\n==============================")
        print(" SISTEMA DE CONTROLE")
        print("==============================")
        print("1. Listar equipamentos cadastrados")
        print("2. Consultar equipamento por nome")
        print("3. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
           print(listar_equipamentos())
        elif opcao == 2:
            nome = input("Digite o nome do equipamento: ")
            print(consultar_equipamento_por_nome(nome))
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
