from database.banco_de_dados import BancoDeDados

if __name__ == '__main__':
    bd = BancoDeDados()
    bd.conexao()
    bd.consulta_todos_clientes()
