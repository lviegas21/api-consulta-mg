from utils.conexao_banco import async_session
from data.models.clientes_models import Cliente
from sqlalchemy.future import select
from sqlalchemy import delete


class ClienteService:
    @staticmethod
    async def create_cliente(nome : str, cpf : str, telefone : str):
        async with async_session() as session:
            session.add(Cliente(nome=nome, cpf=cpf, telefone=telefone))
            await session.commit()
    
    @staticmethod
    async def delete_cliente(cliente_id: int):
        async with async_session() as session:
            await session.execute(delete(Cliente).where(Cliente.id==cliente_id))
            await session.commit()
    
    @staticmethod
    async def list_cliente():
        async with async_session() as session:
            result = await session.execute(select(Cliente))
            return result.scalars().all()
    
    @staticmethod
    async def get_by_id(cliente_id):
        async with async_session() as session:
            result = await session.execute(select(Cliente).where(Cliente.id==cliente_id))
            return result.scalar()