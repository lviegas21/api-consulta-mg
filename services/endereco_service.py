from utils.conexao_banco import async_session
from data.models.endereco_model import Endereco
from sqlalchemy.future import select
from sqlalchemy import delete


class EnderecoService:
    @staticmethod
    async def create_endereco( rua:str, numero:int, bairro: str, cep: str, complemento:str, fk_cliente:int):
        async with async_session() as session:
            session.add(Endereco(rua=rua, numero=numero, bairro=bairro, cep=cep, complemento=complemento, fk_cliente=fk_cliente))
            await session.commit()
    
    # @staticmethod
    # async def atualizar_produto(id : int, descricao : str, preco : float):
    #     async with async_session() as session:
    #         session.update(Produto(id=id, descricao=descricao, preco=preco))
    #         await session.commit()
    
    @staticmethod
    async def delete_endereco(endereco_id: int):
        async with async_session() as session:
            await session.execute(delete(Endereco).where(Endereco.id==endereco_id))
            await session.commit()
    
    @staticmethod
    async def list_endereco():
        async with async_session() as session:
            result = await session.execute(select(Endereco))
            return result.scalars().all()
    
    @staticmethod
    async def get_by_id(endereco_id):
        async with async_session() as session:
            result = await session.execute(select(Endereco).where(Endereco.id==endereco_id))
            return result.scalar()