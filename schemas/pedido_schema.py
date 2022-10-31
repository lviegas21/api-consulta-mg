import datetime

from pydantic import BaseModel

class PedidoPost(BaseModel):
    quantidade: int
    total: float
    data: datetime.date
    fk_cliente: int
    fk_endereco: int
    fk_produto: int

class PedidoListOutput(BaseModel):
    id: int
    quantidade: int
    total: float
    data: datetime.date
    fk_cliente: int
    fk_endereco: int
    fk_produto: int

    class Config:
        orm_mode = True