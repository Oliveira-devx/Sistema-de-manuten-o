from conexao import conectar


def listar_equipamentos():
    conexao = conectar()

    if conexao is None:
        print("Não foi possível listar os equipamentos pois a conexão falhou.")
        return

    try:
        cursor = conexao.cursor()
        sql = "SELECT nome, situacao, valor FROM equipamentos"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        for equipamento in resultados:
            print(f"Nome: {equipamento[0]}")
            print()

        cursor.close()
        conexao.close()

    except Exception as erro:
        print(f"Erro ao consultar equipamentos: {erro}")


def consultar_equipamento_por_nome(nome):
    conexao = conectar()

    if conexao is None:
        print("Conexão falhou.")
        return None

    try:
        cursor = conexao.cursor()
        sql = "SELECT nome, situacao, valor FROM equipamentos WHERE nome = %s"
        cursor.execute(sql, (nome,))
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        return resultado

    except Exception as erro:
        print(f"Erro ao consultar equipamento: {erro}")
        return None


# --- Menu principal ---
print("Escolha uma opção:")
print("1. Listar equipamentos")
print("2. Consultar equipamento por nome")

opcao = input("Opção: ")

if opcao == "1":
    listar_equipamentos()

elif opcao == "2":
    while True:
        equipamento = input("Digite o nome do equipamento: ")
        resultado = consultar_equipamento_por_nome(equipamento)

        if resultado is None:
            print("Equipamento não encontrado. Por favor, tente novamente.")
        else:
            print(f"Nome: {resultado[0]}")
            print(f"Situação: {resultado[1]}")
            print(f"Valor: R$ {resultado[2]}")
            break   