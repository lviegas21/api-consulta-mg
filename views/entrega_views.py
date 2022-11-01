from fastapi import APIRouter, HTTPException
from typing import List

from services.entrega_service import EntregaService
from schemas.entrega_schema import (EntregaPost, EntregaListOutput)
from schemas.base_shema import (StandardOutput, ErrorOutput)

entrega_router = APIRouter(prefix='/api/entrega')


@entrega_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def criar_pedido(entregaPost: EntregaPost):
    try:
        await EntregaService.create_entrega(
            status=entregaPost.status,
            fk_pedido=entregaPost.fk_pedido,

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


@entrega_router.get('/all', response_model=List[EntregaListOutput], responses={400: {'model': ErrorOutput}})
async def estoque_all():
    try:
        return await EntregaService.list_entrega()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@entrega_router.get('/{entrega_id}', response_model=EntregaListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary(estoque_id: int):
    try:
        return await EntregaService.get_by_id(estoque_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))