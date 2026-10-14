import mysql.connector

def conectar():
    """
    Esta função cria e retorna uma conexão com o banco de dados.
    Ela não fecha a conexão, quem a chamou é quem deve fechá-la.
    """
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="admin",
            database="sistema_manutencao",
            use_pure=True
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"ALERTA DE SISTEMA: não foi possível acessar o banco de dados. verifique se o mysql está ativo. Detalhes: {erro}")
        return None