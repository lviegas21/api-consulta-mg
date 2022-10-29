from data.database.banco_de_dados import BancoDeDados
from fastapi import FastAPI, APIRouter
from views.cliente_view import cliente_router
from views.produto_view import produto_router

app = FastAPI()
router = APIRouter()

app.include_router(cliente_router)
app.include_router(produto_router)






