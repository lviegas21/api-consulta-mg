from fastapi import APIRouter
from services.cliente_service import ClienteService
from schemas.cliente_schemas import ClientePost
cliente_router = APIRouter(prefix='/cliente')


@cliente_router.post('/create')
async def criar_cliente(clientepost: ClientePost):
    try:
        await ClienteService.create_cliente(name=clientepost.nome, cpf=clientepost.cpf, telefone=clientepost.telefone)
    except:
        print('error')