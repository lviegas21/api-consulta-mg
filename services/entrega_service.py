from utils.conexao_banco import async_session
from data.models.entrega_model import Entrega
from sqlalchemy.future import select
from sqlalchemy import delete


class EntregaService:
    @staticmethod
    async def create_entrega(status: str, fk_pedido):
        async with async_session() as session:
            session.add(Entrega(status=status,  fk_pedido=fk_pedido))
            await session.commit()

    @staticmethod
    async def detele_entrega(entrega_id: int):
        async with async_session() as session:
            await session.execute(delete(Entrega).where(Entrega.id == entrega_id))
            await session.commit()

    @staticmethod
    async def list_entrega():
        async with async_session() as session:
            result = await session.execute(select(Entrega))
            return result.scalars().all()

    @staticmethod
    async def get_by_id(entrega_id):
        async with async_session() as session:
            result = await session.execute(select(Entrega).where(Entrega.id == entrega_id))
            return result.scalar()

