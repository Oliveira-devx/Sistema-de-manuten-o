# Módulo de Colaboradores
# Finalidade: Gerenciar os colaboradores que solicitam manutenções.
# Futuras Implementações:
# - Cadastro de colaboradores (CRUD)
# - Histórico de solicitações por colaborador

from config.conexao import conectar
import src.setores.setores as setores


confirmacao = ["s", "n"]

def cadastrar_colaborador():
    conexao = conectar()


    nome = input("Digite o nome do colaborador: ")
    cargo = input("Digite o cargo do colaborador: ")
    cpf = int(input("Digite o cpf do colaborador: "))
    setor = input("Digite o setor do colaborador: ")

    listar_setores = [setor[0] for setor in listar_setores]
    listar_setores = setores.listar_setores()
    print(f"Lista para validação: {listar_setores}")
    

    while setor not in setores.listar_setores():
        print("Setor inválido. Por favor, digite um setor válido.")
        setor = input("Digite o setor do colaborador: ")
    

    colaborador = {
        "nome": nome,
        "cargo": cargo,
        "cpf": cpf,
        "setor": setor}
    
    print(f"deseja cadastrar o colaborador {nome} com cargo {cargo} e cpf {cpf} e setor {setor}?") 

    confirmacao = input("Digite 's' para confirmar ou 'n' para cancelar: ")
    
    while confirmacao not in ["s", "n"]:
           print("opção inválida, digite 's' para confirmar ou 'n' para cancelar: ")

    try:
          if confirmacao == "s":
                cursor = conexao.cursor()
                sql = "insert into colaboradores (nome, cargo, cpf) values (%s, %s, %s)"
                valores = (nome, cargo, cpf)
                cursor.execute(sql, valores)

    except Exception as erro:
     print(f"Erro ao cadastrar colaborador: {erro}")

lista_colaboradores_cadastrados = []
cadastrar_colaborador()