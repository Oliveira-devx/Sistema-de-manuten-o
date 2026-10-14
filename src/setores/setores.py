# Módulo de Setores
# Finalidade: Organizar os equipamentos por setores da empresa.
# Futuras Implementações:
# - Cadastro de setores (CRUD)
# - Relatórios de manutenções por setor


from config.conexao import conectar
from src import setores

def listar_setores():
    conexao = conectar()
    if conexao is None:
        return

    cursor = None

    try:
        print("Listando os setores cadastrados...")

        cursor = conexao.cursor()
        sql = "SELECT DISTINCT setor FROM setores"
        cursor.execute(sql)

        setores = cursor.fetchall()

        print("Quantidade de setores:", len(setores))

        for setor in setores:
            print(setor[0])
        return setores


    except Exception as erro:
        print(f"Erro ao listar setores: {erro}")
        return []

    finally:
        if cursor is not None:
            cursor.close()
        conexao.close()


if __name__ == "__main__":
    listar_setores()