
from fastapi import FastAPI, APIRouter
from views.cliente_view import cliente_router
from views.produto_view import produto_router
from views.endereco_view import endereco_router

app = FastAPI()
router = APIRouter()

app.include_router(cliente_router)
app.include_router(produto_router)
app.include_router(endereco_router)






