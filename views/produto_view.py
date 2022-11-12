from fastapi import APIRouter, HTTPException
from typing import List

from services.produto_service import ProdutoService
from schemas.produto_schema import (ProdutoPost, ProdutoListOutput, ProdutoUpdate)
from schemas.base_shema import (StandardOutput, ErrorOutput)

produto_router = APIRouter(prefix='/api/produto')


@produto_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def criar_produto(produtopost: ProdutoPost):
    try:
        await ProdutoService.create_produto(descricao=produtopost.descricao, preco=produtopost.preco)
        return StandardOutput(message='Criado com sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

# @produto_router.delete('/{produto_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
# async def produto_delete(produto_id: int):
#     try:
#         await ProdutoService.delete_produto(produto_id)
#         return StandardOutput(message='Ok')
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))

@produto_router.get('/all', response_model=List[ProdutoListOutput], responses={400: {'model': ErrorOutput}})
async def produto_all():
    try:
        return await ProdutoService.list_produto()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@produto_router.get('/{produto_id}', response_model=ProdutoListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary(produto_id: int):
    try:
        return await ProdutoService.get_by_id(produto_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@produto_router.put('/{produto_id}', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def atualizar_produto(produto_id: int, produtoupdate: ProdutoUpdate):
    try:
        await ProdutoService.atualizar_produto(id=produto_id, descricao=produtoupdate.descricao, preco=produtoupdate.preco)
        return StandardOutput(message='Atualizado com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))