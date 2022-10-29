from utils.conexao_banco import async_session
from data.models.produto_model import Produto
from sqlalchemy.future import select
from sqlalchemy import delete


class ProdutoService:
    @staticmethod
    async def create_produto(descricao : str, preco : float):
        async with async_session() as session:
            session.add(Produto(descricao=descricao, preco=preco))
            await session.commit()
    
    # @staticmethod
    # async def atualizar_produto(id : int, descricao : str, preco : float):
    #     async with async_session() as session:
    #         session.update(Produto(id=id, descricao=descricao, preco=preco))
    #         await session.commit()
    
    @staticmethod
    async def delete_produto(produto_id: int):
        async with async_session() as session:
            await session.execute(delete(Produto).where(Produto.id==produto_id))
            await session.commit()
    
    @staticmethod
    async def list_produto():
        async with async_session() as session:
            result = await session.execute(select(Produto))
            return result.scalars().all()
    
    @staticmethod
    async def get_by_id(produto_id):
        async with async_session() as session:
            result = await session.execute(select(Produto).where(Produto.id==produto_id))
            return result.scalar()