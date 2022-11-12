from fastapi import APIRouter, HTTPException
from typing import List

from services.estoque_service import EstoqueService
from schemas.estoque_schema import (EstoquePost, EstoqueListOutput, EstoqueUpdate)
from schemas.base_shema import (StandardOutput, ErrorOutput)

estoque_router = APIRouter(prefix='/api/estoque')


@estoque_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def criar_pedido(estoquePost: EstoquePost):
    try:
        await EstoqueService.create_estoque(
            quantidade=estoquePost.quantidade,
            fk_produto=estoquePost.fk_produto,

        )
        return StandardOutput(message='Criado com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


# @estoque_router.delete('/{estoque_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
# async def estoque_delete(estoque_id: int):
#     try:
#         await EstoqueService.detele_estoque(estoque_id)
#         return StandardOutput(message='Ok')
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))

@estoque_router.put('/{estoque_id}', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def atualizar_estoque(estoque_id: int, estoqueUpdate: EstoqueUpdate):
    try:
        await EstoqueService.atualizar_estoque(id=estoque_id, quantidade=estoqueUpdate.quantidade)
        return StandardOutput(message='Atualizado com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@estoque_router.get('/all', response_model=List[EstoqueListOutput], responses={400: {'model': ErrorOutput}})
async def estoque_all():
    try:
        return await EstoqueService.list_estoque()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@estoque_router.get('/{estoque_id}', response_model=EstoqueListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary(estoque_id: int):
    try:
        return await EstoqueService.get_by_id(estoque_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))