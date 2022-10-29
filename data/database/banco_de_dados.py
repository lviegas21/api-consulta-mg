from utils.conexao_banco import connectar


class BancoDeDados:
    def __init__(self):
        pass

    def conexao(self):
        self.conn = connectar()

        self.cursor = self.conn.cursor()

    def consulta_todos_clientes(self):
        clientes = {}
        sql = 'SELECT * FROM CLIENTE'

        self.cursor.execute(sql)
        recset = self.cursor.fetchall()
        for rec in recset:

            val = {
                'id': rec[0],
                'nome': rec[1],
                'cpf': rec[2],
                'telefone': rec[2],


            }
            print(val)


            return val

    def consulta_cliente_especifico(self):
        pass

    def deleta_cliente_especifico(self):
        pass

    def inserir_cliente(self):
        pass

    def atualizar_cliente(self):
        pass