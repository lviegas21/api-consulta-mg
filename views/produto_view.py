from fastapi import APIRouter, HTTPException
from typing import List

from services.produto_service import ProdutoService
from schemas.produto_schema import (ProdutoPost, ProdutoListOutput)
from schemas.base_shema import (StandardOutput, ErrorOutput)

produto_router = APIRouter(prefix='/api/produto')


# @produto_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
# async def criar_cliente(clientepost: ClientePost):
#     try:
#         print(clientepost)
#         await ClienteService.create_cliente(nome=clientepost.nome, cpf=clientepost.cpf, telefone=clientepost.telefone)
#         return StandardOutput(message='Criado com sucesso') 
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))
    

# @produto_router.delete('/{cliente_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
# async def cliente_delete(cliente_id: int):
#     try:
#         await ClienteService.delete_cliente(cliente_id)
#         return StandardOutput(message='Ok') 
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))


@produto_router.get('/all', response_model=List[ProdutoListOutput], responses={400: {'model': ErrorOutput}})
async def produto_all():
    try:
        return await ProdutoService.list_produto()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


# @produto_router.get('/{cliente_id}', response_model=ClienteListOutput, responses={400: {'model': ErrorOutput}})
# async def day_summary(cliente_id: int):
#     try:
#         return await ClienteService.get_by_id(cliente_id)
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))