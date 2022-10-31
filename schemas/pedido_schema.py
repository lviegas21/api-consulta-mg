from pydantic import BaseModel

class PedidoPost(BaseModel):
    quantidade: str
    total: str
    data: str
    fk_cliente: str
    fk_endereco: str
    fk_produto: str

class PedidoListOutput(BaseModel):
    id: int
    quantidade: str
    total: str
    data: str
    fk_cliente: str
    fk_endereco: str
    fk_produto: str

    class Config:
        orm_mode = True