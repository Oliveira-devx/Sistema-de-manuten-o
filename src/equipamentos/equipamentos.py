from config.conexao import conectar


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


   