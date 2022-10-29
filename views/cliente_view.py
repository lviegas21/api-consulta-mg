from fastapi import APIRouter, HTTPException
from typing import List

from services.cliente_service import ClienteService
from schemas.cliente_schemas import (ClientePost, ClienteListOutput)
from schemas.base_shema import (StandardOutput, ErrorOutput)

cliente_router = APIRouter(prefix='/api/cliente')


@cliente_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def criar_cliente(clientepost: ClientePost):
    try:
        print(clientepost)
        await ClienteService.create_cliente(nome=clientepost.nome, cpf=clientepost.cpf, telefone=clientepost.telefone)
        return StandardOutput(message='Criado com sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@cliente_router.delete('/{cliente_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def cliente_delete(cliente_id: int):
    try:
        await ClienteService.delete_cliente(cliente_id)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@cliente_router.get('/all', response_model=List[ClienteListOutput], responses={400: {'model': ErrorOutput}})
async def cliente_all():
    try:
        return await ClienteService.list_cliente()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@cliente_router.get('/{cliente_id}', response_model=ClienteListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary(cliente_id: int):
    try:
        return await ClienteService.get_by_id(cliente_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))