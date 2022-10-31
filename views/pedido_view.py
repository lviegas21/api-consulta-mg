from fastapi import APIRouter, HTTPException
from typing import List

from services.pedido_service import PedidoService
from schemas.pedido_schema import (PedidoPost, PedidoListOutput)
from schemas.base_shema import (StandardOutput, ErrorOutput)

pedido_router = APIRouter(prefix='/api/pedido')


@pedido_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def criar_produto(pedidoPost: PedidoPost):
    try:
        await PedidoService.create_pedido(
            quantidade=pedidoPost.quantidade,
            total=pedidoPost.total,
            data=pedidoPost.data,
            fk_cliente=pedidoPost.fk_cliente,
            fk_produto=pedidoPost.fk_produto,
            fk_endereco=pedidoPost.fk_endereco,
        )
        return StandardOutput(message='Criado com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@pedido_router.delete('/{pedido_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def produto_delete(pedido_id: int):
    try:
        await PedidoService.delete_pedido(pedido_id)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@pedido_router.get('/all', response_model=List[PedidoListOutput], responses={400: {'model': ErrorOutput}})
async def produto_all():
    try:
        return await PedidoService.list_pedido()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@pedido_router.get('/{pedido_id}', response_model=PedidoListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary(pedido_id: int):
    try:
        return await PedidoService.get_by_id(pedido_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

