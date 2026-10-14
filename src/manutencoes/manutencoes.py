from config.conexao import conectar
from src.equipamentos.equipamentos import consultar_equipamento_por_nome


def consultar_manutencoes(conexao, nome_equipamento):
    if conexao is None:
        print("Erro: Conexão com o banco de dados não estabelecida.")
        return

    try:
        cursor = conexao.cursor()

        sql =   f"""SELECT
               b.nome,
               a.data_abertura,
               a.problema_apresentado,
               a.prioridade,
               a.diagnostico,
               a.solucao_realizada,
               a.custo,
               a.`status`,
               a.data_fechamento
               FROM manutencoes AS a
                LEFT JOIN equipamentos AS b
                 ON a.id_equipamento = b.id_equipamento
                WHERE b.nome = %s"""

        cursor.execute(sql,(nome_equipamento,))

        resultados = cursor.fetchall()

        for manutencao in resultados:
            print(f"nome_equipamento:     {manutencao[0]}")
            print(f"data_abertura:        {manutencao[1]}")
            print(f"problema_apresentado: {manutencao[2]}")
            print(f"prioridade:           {manutencao[3]}")
            print(f"diagnostico:          {manutencao[4]}")
            print(f"solucao_realizada:    {manutencao[5]}")
            print(f"custo:                {manutencao[6]}")
            print(f"status:               {manutencao[7]}")
            print(f"data_fechamento:      {manutencao[8]}")

        cursor.close()

    except Exception as erro:
        print(f"Erro ao consultar manutenções: {erro}")
