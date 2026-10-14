from src.equipamentos.equipamentos import listar_equipamentos, consultar_equipamento_por_nome
from src.colaboradores.colaboradores import cadastrar_colaborador

def menu():

    while True:

        print("\n==============================")
        print(" SISTEMA DE CONTROLE")
        print("==============================")
        print("1. Listar equipamentos cadastrados")
        print("2. Consultar equipamento por nome")
        print("3. Sair")
        print("==============================")
        print("4. Cadastrar colaborador")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opcao == 1:
           print(listar_equipamentos())
        elif opcao == 2:
            nome = input("Digite o nome do equipamento: ")
            print(consultar_equipamento_por_nome(nome))
        elif opcao == 3:
            print("Saindo...")
            break
        elif opcao == 4:
            cadastrar_colaborador()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
