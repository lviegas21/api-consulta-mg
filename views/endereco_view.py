from fastapi import APIRouter, HTTPException
from typing import List

from services.endereco_service import EnderecoService
from schemas.endereco_schema import (EnderecoPost, EnderecoListOutput, EnderecoUpdate)
from schemas.base_shema import (StandardOutput, ErrorOutput)

endereco_router = APIRouter(prefix='/api/endereco')


@endereco_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def criar_endereco(enderecoPost: EnderecoPost):
    try:
        await EnderecoService.create_endereco(rua=enderecoPost.rua, numero=enderecoPost.numero, bairro=enderecoPost.bairro, cep=enderecoPost.cep, complemento=enderecoPost.complemento, fk_cliente=enderecoPost.fk_cliente)
        return StandardOutput(message='Criado com sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@endereco_router.delete('/{endereco_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def endereco_delete(endereco_id: int):
    try:
        await EnderecoService.delete_endereco(endereco_id)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@endereco_router.get('/all', response_model=List[EnderecoListOutput], responses={400: {'model': ErrorOutput}})
async def endereco_all():
    try:
        return await EnderecoService.list_endereco()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@endereco_router.get('/{endereco_id}', response_model=EnderecoListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary(endereco_id: int):
    try:
        return await EnderecoService.get_by_id(endereco_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

# @endereco_router.put('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
# async def atualizar_produto(produtoupdate: ProdutoUpdate):
#     try:
#         await ProdutoService.atualizar_produto(id=produtoupdate.id, descricao=produtoupdate.descricao, preco=produtoupdate.preco)
#         return StandardOutput(message='Atualizado com sucesso') 
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))