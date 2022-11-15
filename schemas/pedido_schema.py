import datetime

from pydantic import BaseModel

from data.models.clientes_models import Cliente


class PedidoPost(BaseModel):
    quantidade: int
    total: float
    data_pedido: datetime.date
    fk_cliente: int
    fk_endereco: int
    fk_produto: int

class PedidoUpdate(BaseModel):
    quantidade: int
    total: float
    data_pedido: datetime.date

class PedidoListOutput(BaseModel):
    id: int
    quantidade: int
    total: float
    data_pedido: datetime.date

    fk_cliente: int
    fk_endereco: int
    fk_produto: int

    class Config:
        orm_mode = True