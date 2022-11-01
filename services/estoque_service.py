from utils.conexao_banco import async_session
from data.models.estoque_model import Estoque
from sqlalchemy.future import select
from sqlalchemy import delete


class EstoqueService:
    @staticmethod
    async def create_estoque(quantidade: int, fk_produto):
        async with async_session() as session:
            session.add(Estoque(quantidade=quantidade,  fk_produto=fk_produto))
            await session.commit()

    @staticmethod
    async def detele_estoque(estoque_id: int):
        async with async_session() as session:
            await session.execute(delete(Estoque).where(Estoque.id == estoque_id))
            await session.commit()

    @staticmethod
    async def list_estoque():
        async with async_session() as session:
            result = await session.execute(select(Estoque))
            return result.scalars().all()

    @staticmethod
    async def get_by_id(estoque_id):
        async with async_session() as session:
            result = await session.execute(select(Estoque).where(Estoque.id == estoque_id))
            return result.scalar()

    @staticmethod
    async def atualizar_estoque(id : int, quantidade : str, fk_produto):
        async with async_session() as session:
            session.update(Estoque(id=id, quantidade=quantidade, fk_produto=fk_produto))
            await session.commit()