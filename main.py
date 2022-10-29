from data.database.banco_de_dados import BancoDeDados
from fastapi import FastAPI, APIRouter
from views.cliente_view import cliente_router

app = FastAPI()
router = APIRouter()

app.include_router(cliente_router)






