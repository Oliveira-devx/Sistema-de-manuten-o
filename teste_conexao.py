from contruindo.conexao import conectar

print("Testando conexão...")
conn = conectar()

if conn:
    print("Conexão estabelecida com sucesso!")
    conn.close()
else:
    print("Falha na conexão.")