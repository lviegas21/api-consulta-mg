from utils.conexao_banco import async_session
from data.models.clientes_models import Cliente


class ClienteService:
    @staticmethod
    async def create_cliente(name, cpf, telefone):
        async with async_session() as session:
            session.add(Cliente(name=name, cpf=cpf, telefone=telefone))
            await session.commit()