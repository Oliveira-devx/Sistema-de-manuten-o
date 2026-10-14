import mysql.connector

def conectar():
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
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None