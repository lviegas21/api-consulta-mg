import datetime

from utils.conexao_banco import async_session
from data.models.pedido_model import Pedido
from sqlalchemy.future import select
from sqlalchemy import delete


class PedidoService:
    @staticmethod
    async def create_pedido(quantidade: int, total: float, data: datetime.date, fk_cliente, fk_produto, fk_endereco):
        async with async_session() as session:
            session.add(Pedido(quantidade=quantidade, total=total, data=data, fk_cliente=fk_cliente, fk_produto=fk_produto, fk_endereco=fk_endereco))
            await session.commit()



    @staticmethod
    async def delete_pedido(pedido_id: int):
        async with async_session() as session:
            await session.execute(delete(Pedido).where(Pedido.id == pedido_id))
            await session.commit()

    @staticmethod
    async def list_pedido():
        async with async_session() as session:
            result = await session.execute(select(Pedido))
            return result.scalars().all()

    @staticmethod
    async def get_by_id(pedido_id):
        async with async_session() as session:
            result = await session.execute(select(Pedido).where(Pedido.id == pedido_id))
            return result.scalar()

    # @staticmethod
    # async def atualizar_produto(id : int, descricao : str, preco : float):
    #     async with async_session() as session:
    #         session.update(Produto(id=id, descricao=descricao, preco=preco))
    #         await session.commit()