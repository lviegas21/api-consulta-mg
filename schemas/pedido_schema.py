import datetime

from pydantic import BaseModel
from datetime import date as date_type
from data.models.clientes_models import Cliente


class PedidoPost(BaseModel):
    quantidade: int
    total: float
    date_pedido: str
    fk_cliente: int
    fk_endereco: int
    fk_produto: int

class PedidoUpdate(BaseModel):
    quantidade: int
    total: float
    date_pedido: str

class PedidoListOutput(BaseModel):
    id: int
    quantidade: int
    total: float
    date_pedido: str

    fk_cliente: int
    fk_endereco: int
    fk_produto: int

    class Config:
        orm_mode = True