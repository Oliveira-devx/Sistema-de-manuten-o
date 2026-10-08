from contruindo.conexao import conectar


def listar_fornecedores():

    conexao = conectar()

    if conexao is None:
      print("Não foi possível estabelecer a conexão com o banco de dados.")
      return

    try:
     
      cursor = conexao.cursor()

      sql = "SELECT razao_social, representantes, telefone, email, cidade, estado FROM fornecedores"

      cursor.execute(sql)

      resultados = cursor.fetchall()

      for fornecedores in resultados:
          print(f"razao_social:{fornecedores[0]}")
          print(f"representante:{fornecedores[1]}")
          print(f"telefone:{fornecedores[2]}")
          print(f"email:{fornecedores[3]}")
          print(f"cidade:{fornecedores[4]}")
          print(f"estado:{fornecedores[5]}")
          print()

      cursor.close()
      conexao.close()

    except Exception as erro:
        print(f"Erro ao consultar fornecedores: {erro}")        


listar_fornecedores()

     

    
      
